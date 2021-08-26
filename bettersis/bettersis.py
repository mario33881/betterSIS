#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
**BETTERSIS**: The modern shell for SIS
"""

__author__ = "Zenaro Stefano"

import logging
import logging.handlers
import platform
import re
import os

import siswrapper
import blifparser.blifparser as blifparser
from prompt_toolkit import PromptSession
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import FileHistory

try:
    from ._version import __version__  # noqa: F401
    import bettersis.siscompleter as siscompleter
    import bettersis.update_checker as update_checker
    import bettersis.texteditor as texteditor
    import bettersis.history_utils as history_utils
    import bettersis.web_utils as web_utils

except ImportError:
    from _version import __version__  # noqa: F401
    import siscompleter
    import update_checker
    import texteditor
    import history_utils
    import web_utils

boold = False
github_repository_url = "https://github.com/mario33881/betterSIS"
bettersis_cmds = [
    "edit",
    "cd",
    "ls",
    "bsis_documentation",
    "bsis_tutorials",
    "bsis_releases",
    "bsis_checkblif",
    "help",
]

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def show_ghissues_msg():
    """
    Shows the "please, report this to the developer" message.
    """
    print("\nPlease, (if someone didn't post this error already) create a Github Issue here: '{}'\n"
          "and share the '/var/log/pybettersis/pybettersis.log' log file\n"
          "to help the developer to fix the problem\n".format(github_repository_url + "/issues"))
    print("> If you are using the PyInstaller build, execute this command:")
    print("> 'cat /var/log/syslog | grep \"bettersis\" > pybettersis.log'\n"
          "to create the log file inside the current directory.")


class Bettersis:
    """
    Shows bettersis' interactive shell.

    After the creation of an instance
    a SIS process is ready to receive commands.

    .. note:: The SIS process is started and controlled by
              the `siswrapper <https://github.com/mario33881/siswrapper>`_. library

    Shared variables:

    - ``res``: dictionary with results of the start operation (success, errors, stdout)
    - ``sis``: connection to SIS's process
    - ``lastcmd``: contains the last command
    - ``lastcmd_success``: boolean that is set to True if the last command execution was successfull
    - ``history_file_path``: path to the history file (used when ``BSIS_HISTORY_ENABLED`` environment variable is "true")
    """
    def __init__(self):
        self.res = {"success": False, "errors": [], "stdout": None}
        self.sis = siswrapper.Siswrapper()
        self.lastcmd = "FIRSTCOMMAND"
        self.lastcmd_success = False
        self.history_file_path = os.path.join(os.path.expanduser("~"), ".bsis_history")

        if self.sis.res["success"]:
            self.show_msg_on_startup()

            updates_res = update_checker.check_updates("https://api.github.com/repos/mario33881/bettersis/releases",
                                                       __version__.split(" ")[1])
            if updates_res["success"]:
                if updates_res["update_available"]:
                    print("\nNew Update Available! (latest: {})".format(updates_res["update_version"]))
                    print("Type the 'bsis_releases' command to open the download webpage for the last release!")
            else:
                for error in updates_res["errors"]:
                    logger.warning("[ERROR-UPDATE] {}".format(error), exc_info=True)

            self.main()
        else:
            for error in self.sis.res["errors"]:
                self.res["errors"].append("[ERROR][INIT] Error during SIS startup: " + error)

    def show_msg_on_startup(self):
        """
        Shows the message at the shell startup.
        """

        try:
            print("                                                                       ")
            print(" ██████╗ ███████╗████████╗████████╗███████╗██████╗ ███████╗██╗███████╗ ")
            print(" ██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██║██╔════╝ ")
            print(" ██████╔╝█████╗     ██║      ██║   █████╗  ██████╔╝███████╗██║███████╗ ")
            print(" ██╔══██╗██╔══╝     ██║      ██║   ██╔══╝  ██╔══██╗╚════██║██║╚════██║ ")
            print(" ██████╔╝███████╗   ██║      ██║   ███████╗██║  ██║███████║██║███████║ ")
            print(" ╚═════╝ ╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝ ")
        except UnicodeEncodeError:
            # The user probably didn't set an UTF-8 language 
            # in the $LANG environment variable
            pass

        print("                                                                       ")
        print(" ===================================================================== ")
        print("                                                                       ")
        print("                              DISCLAIMER:                              ")
        print(" BetterSIS, this software, controls SIS in the background and tries to ")
        print(" provide modern features                                               ")
        print(" (such as command history, suggestions and autocompletion)             ")
        print(" and small improvements to SIS itself. (like the simulate improvement) ")
        print(" > SIS is a tool for synthesis and optimization of sequential circuits ")
        print("                                                                       ")
        print(" I'm not affiliated with the SIS developers in any way.                ")
        print(" You can read more about SIS here:                                     ")
        print(" https://jackhack96.github.io/logic-synthesis/sis.html                 ")
        print("                                                                       ")
        print(" ===================================================================== ")
        print("                                                                       ")
        print(" BetterSIS version:    {}".format(__version__))
        print(" BetterSIS repository: {}".format(github_repository_url))
        print(" Siswrapper version:   {}".format(siswrapper.__version__))
        print(" Running in the background: ", self.sis.res["stdout"])

        logger.info("[STARTUP_MESSAGE] Showing software versions "
                    "(BetterSIS: %s, Siswrapper: %s, SIS: %s)" % (__version__,
                                                                  siswrapper.__version__,
                                                                  self.sis.res["stdout"]))

    def main(self):
        """
        Starts the interactive shell.
        """
        # create a Session to memorize user commands
        session = PromptSession()

        # if the BSIS_HISTORY_ENABLED environment variable is set to "true",
        # use a history file inside the home directory
        if self.manage_history_file():
            history_file = FileHistory(self.history_file_path)
            session = PromptSession(history=history_file)

        # get the first command to show the custom toolbar
        try:
            command = session.prompt('bsis> ',
                                     completer=siscompleter.get_siscompleter(),  # use completer from siscompleter.py
                                     complete_in_thread=True,                    # better performance for autocompletion
                                     bottom_toolbar="")                          # empty toolbar

        except (KeyboardInterrupt, EOFError):
            # user pressed Ctrl+C or Ctrl+D
            logger.debug("[MAIN] User wants to exit the software (at least one command has been executed before)")
        else:
            # keep getting commands from the user
            while True:
                try:
                    logger.debug("[MAIN] User executed command: " + command.strip())
                    if command.strip() in ["exit", "quit"]:
                        break

                    self.manage_multiple_commands(command.strip())

                    print("")
                    command = session.prompt('bsis> ',
                                             completer=siscompleter.get_siscompleter(),  # use completer from siscompleter.py
                                             complete_in_thread=True,                    # better performance autocompletion
                                             auto_suggest=AutoSuggestFromHistory(),      # suggest rest of command from history
                                             bottom_toolbar=self.bottom_toolbar)         # add toolbar at the bottom

                except (KeyboardInterrupt, EOFError):
                    # user pressed Ctrl+C or Ctrl+D
                    logger.debug("[MAIN] User wants to exit the software (at least one command has been executed before)")
                    break

        # control, if necessary, the size of the history file before closing betterSIS
        self.manage_history_file()

        # stop sis process
        self.sis.stop()

    def manage_history_file(self):
        """
        Manages the history file size and usage.

        Checks if the ``BSIS_HISTORY_ENABLED`` environment variable is set to true:
        if is is set to true the function returns True and betterSIS
        will use the history file,
        else the history will expire at the end of the session.

        Then, if a history file already exists, checks the ``BSIS_HISTORY_SIZELIMIT`` environment:
        if the value is a number it is used as a size limit,
        else the limit is the default one (0.1 MB)
        """
        default_size = 0.1 * 1000 * 1000
        history_file_enabled = False

        if os.getenv("BSIS_HISTORY_ENABLED"):
            logger.debug("[MANAGE_HISTORY_FILE] The BSIS_HISTORY_ENABLED "
                         "env. variable is set to '{}'".format(os.getenv("BSIS_HISTORY_ENABLED")))

            if os.getenv("BSIS_HISTORY_ENABLED") == "true":
                history_file_enabled = True

                # if the history file exists, manage its size
                if os.path.isfile(self.history_file_path):
                    logger.debug("[MANAGE_HISTORY_FILE] The history file exists, controlling its size...")
                    if os.getenv("BSIS_HISTORY_SIZELIMIT"):
                        # try to use custom size limit (use default one on error)
                        try:
                            size = int(os.getenv("BSIS_HISTORY_SIZELIMIT"))
                            logger.debug("[MANAGE_HISTORY_FILE] Using custom size limit: '{}' bytes".format(size))
                            history_utils.limit_history_size(self.history_file_path, size)
                        except ValueError:
                            logger.debug("[MANAGE_HISTORY_FILE] Using default size limit: '{}' bytes "
                                         "(BSIS_HISTORY_SIZELIMIT is invalid)".format(default_size))
                            warning_msg = "<b><yellow>[Warning]</yellow></b> The BSIS_HISTORY_SIZELIMIT env. variable value" \
                                          " ('{}') is invalid: " \
                                          "it needs to be a number".format(os.getenv("BSIS_HISTORY_SIZELIMIT"))

                            print_formatted_text(warning_msg)

                            history_utils.limit_history_size(self.history_file_path, default_size)
                    else:
                        # use default size limit
                        logger.debug("[MANAGE_HISTORY_FILE] Using default size limit: '{}' bytes".format(default_size))
                        history_utils.limit_history_size(self.history_file_path, default_size)
        else:
            logger.debug("[MANAGE_HISTORY_FILE] The BSIS_HISTORY_ENABLED env. variable is NOT set, using normal session")

        return history_file_enabled

    def bottom_toolbar(self):
        """
        Returns message to show inside the toolbar at the bottom.

        :return str toolbar: toolbar message
        """
        toolbar_msg = ""
        toolbar = None

        if self.lastcmd != "":
            toolbar_msg = f'Executing <b>{self.lastcmd}</b> command... '

            if self.lastcmd_success:
                toolbar_msg += '<style bg="green">Done</style>'
            else:
                toolbar_msg += '<style bg="red">Error</style>'

            toolbar = HTML(toolbar_msg)

        logger.debug("[BOTTOM_TOOLBAR] %s" % toolbar)

        return toolbar

    def manage_multiple_commands(self, t_commands):
        """
        Executes the command(s) <t_commands>.

        :param str t_commands: command(s) to execute (using SIS or special bSIS commands)
        """
        # loop for each command separated by ";"
        for command in t_commands.split(";"):
            if command.strip().split(" ")[0] in bettersis_cmds:
                # intercept betterSIS commands
                self.manage_bsis_command(command.strip())
            else:
                # manage SIS commands
                self.manage_command(command.strip())

    def manage_bsis_command(self, t_command):
        """
        Executes the ``<t_command>`` command betterSIS.

        :param str t_command: custom betterSIS command to execute
        """
        # memorize command to show it on the toolbar
        command = t_command.split(" ")[0]
        self.lastcmd = command

        cd_matches = re.match(r"cd[\s]*[(\")*(\')*]*([^\"']*)[(\")*(\')*]*", t_command)
        ls_matches = re.match(r"ls[\s]*[(\")*(\')*]*([^\"']*)[(\")*(\')*]*", t_command)
        edit_matches = re.match(r"edit[\s]*[(\")*(\')*]*([^\"']*)[(\")*(\')*]*", t_command)
        checkblif_matches = re.match(r"bsis_checkblif[\s]*[(\")*(\')*]*([^\"']*)[(\")*(\')*]*", t_command)

        logger.debug("[%s-BSIS_COMMAND] %s" % (self.lastcmd, t_command))

        # cd command
        if cd_matches:
            if cd_matches.groups()[0].strip() != "":
                self.bsiscmd_cd(cd_matches.groups()[0])
                logger.debug("[%s-EXECUTED_CD_BSIS_COMMAND] %s" % (self.lastcmd, t_command))
            else:
                logger.debug("[%s-EXECUTED_INCOMPLETE_BSIS_COMMAND] %s" % (self.lastcmd, t_command))
                error_msg = "<b><red>[ERROR]</red></b> Incomplete cd command (need to specify the directory)"
                print_formatted_text(HTML(error_msg))
                self.lastcmd_success = False

        # ls command
        elif t_command == "ls":
            self.bsiscmd_ls("")
            logger.debug("[%s-EXECUTED_LS_BSIS_COMMAND] %s" % (self.lastcmd, t_command))

        elif ls_matches:
            if ls_matches.groups()[0].strip() != "":
                self.bsiscmd_ls(ls_matches.groups()[0])
                logger.debug("[%s-EXECUTED_LS_BSIS_COMMAND] %s" % (self.lastcmd, t_command))
            else:
                error_msg = "<b><red>[ERROR]</red></b> Incomplete ls command"
                logger.debug("[%s-EXECUTED_INCOMPLETE_BSIS_COMMAND] %s" % (self.lastcmd, t_command))
                print_formatted_text(HTML(error_msg))
                self.lastcmd_success = False

        # edit command
        elif edit_matches:
            if edit_matches.groups()[0].strip() != "":
                self.bsiscmd_edit(edit_matches.groups()[0])
                logger.debug("[%s-EXECUTED_EDIT_BSIS_COMMAND] %s" % (self.lastcmd, t_command))
            else:
                error_msg = "<b><red>[ERROR]</red></b> Incomplete edit command (need to specify the filename to edit)"
                logger.debug("[%s-EXECUTED_INCOMPLETE_BSIS_COMMAND] %s" % (self.lastcmd, t_command))
                print_formatted_text(HTML(error_msg))
                self.lastcmd_success = False

        # bsis_documentation command
        elif t_command == "bsis_documentation":
            url = "https://bettersis.readthedocs.io/en/latest/readme.html"
            self.lastcmd_success = web_utils.open_browser(url, "documentation")
            logger.debug("[%s-EXECUTED_BSIS_DOCUMENTATION_BSIS_COMMAND] %s" % (self.lastcmd, t_command))

        # bsis_tutorials command
        elif t_command == "bsis_tutorials":
            url = "https://bettersis.readthedocs.io/en/latest/tutorials/tutorials.html"
            self.lastcmd_success = web_utils.open_browser(url, "tutorials")
            logger.debug("[%s-EXECUTED_BSIS_TUTORIALS_BSIS_COMMAND] %s" % (self.lastcmd, t_command))

        # bsis_releases command
        elif t_command == "bsis_releases":
            url = "https://github.com/mario33881/betterSIS/releases/latest"
            self.lastcmd_success = web_utils.open_browser(url, "Github releases")
            logger.debug("[%s-EXECUTED_BSIS_RELEASES_BSIS_COMMAND] %s" % (self.lastcmd, t_command))

        # bsis_checkblif command
        elif checkblif_matches:
            filepath = checkblif_matches.groups()[0]
            filepath = filepath.strip()

            if filepath != "":
                # user specified the input path
                if os.path.isfile(filepath):
                    blif = blifparser.BlifParser(filepath).blif

                    print("\nISSUES LIST:\n")

                    for problem in blif.problems:
                        print(problem)

                    print("=" * 50)
                    print("\n{} issues found".format(len(blif.problems)))
                    self.lastcmd_success = True
                else:
                    print_formatted_text(HTML("<b><red>[ERROR]</red></b> bsis_checkblif input file doesn't exist: "
                                              "please specify a correct path OR "
                                              "call bsis_checkblif (with no parameters) AFTER using the read_blif command"))
                    self.lastcmd_success = False
            else:
                # user didn't specify input path: using the file read using the read_blif command (if available)
                if self.sis.read_path is not None:
                    blif = blifparser.BlifParser(self.sis.read_path).blif

                    print("\nISSUES LIST:\n")

                    for problem in blif.problems:
                        print(problem)

                    print("=" * 50)
                    print("\n{} issues found".format(len(blif.problems)))
                    self.lastcmd_success = True
                else:
                    print_formatted_text(HTML("<b><red>[ERROR]</red></b> no file was specified for the bsis_checkblif command: "
                                              "please specify a correct path as a parameter OR call bsis_checkblif "
                                              "(with no parameters) AFTER using the read_blif command"))
                    self.lastcmd_success = False

        # help command
        elif t_command == "help":
            print("\nSIS COMMANDS:")
            self.manage_command(t_command)

            print("\nBETTERSIS COMMANDS:\n")
            print("* edit : opens a file with a simple CLI text editor")
            print("* cd : changes current working directory")
            print("* ls : shows the content of the current working directory")
            print("* bsis_documentation : opens the website with the betterSIS documentation")
            print("* bsis_tutorials : opens the website with SIS/betterSIS tutorials")
            print("* bsis_releases : opens the betterSIS's download page")
            print("* bsis_checkblif : BLIF parser/validation tool")
            print("* bsis_script : executes optimization and mapping commands in one command "
                  "(needs parameters to specify the type of circuit to optimize/map)")

            print("\n> If you would like to know more about these commands, "
                  "execute the 'bsis_documentation' command to open the documentation website")
            self.lastcmd_success = True

        # unexpected bsis command
        else:
            self.lastcmd_success = False
            error_msg = "<b><red>[ERROR]</red></b> Unexpected betterSIS command ('" + t_command + "')..."
            show_ghissues_msg()
            logger.critical("[%s-UNKNOWN_BSIS_COMMAND] %s" % (self.lastcmd, t_command), exc_info=True)
            print_formatted_text(HTML(error_msg))

    def bsiscmd_cd(self, t_path):
        """
        Changes current directory to the ``<t_path>`` directory.

        :param str t_path: new working path
        """
        if os.path.isdir(t_path):
            os.chdir(t_path)
            self.lastcmd_success = True
        else:
            self.lastcmd_success = False
            error_msg = "<b><red>[ERROR]</red></b> '" + t_path + "' folder doesn't exist"
            print_formatted_text(HTML(error_msg))

    def bsiscmd_ls(self, t_path):
        """
        Lists files and directories inside the ``<t_path>`` folder.

        :param str t_path: path in which to execute the "ls" command
        """
        if t_path == "":
            # show files and directories inside the current folder
            print_formatted_text(HTML("<orange>(F)iles</orange> and <blue>(D)irectories</blue> inside '" + os.getcwd() + "'"))
            print("-" * 50)
            self.lastcmd_success = True
            for el in os.listdir():
                if os.path.isdir(el):
                    print_formatted_text(HTML("<blue>(D) " + el + "</blue>"))
                else:
                    print_formatted_text(HTML("<orange>(F) " + el + "</orange>"))

        elif os.path.isdir(t_path):
            # show files and directories inside the specified folder
            print_formatted_text(HTML("<orange>(F)iles</orange> and <blue>(D)irectories</blue> inside '" + t_path + "'"))
            print("-" * 50)
            self.lastcmd_success = True
            for el in os.listdir(t_path):
                if os.path.isdir(el):
                    print_formatted_text(HTML("<blue>(D) " + el + "</blue>"))
                else:
                    print_formatted_text(HTML("<orange>(F) " + el + "</orange>"))
        else:
            self.lastcmd_success = False
            error_msg = "<b><red>[ERROR]</red></b> '" + t_path + "' folder doesn't exist"
            print_formatted_text(HTML(error_msg))

    def bsiscmd_edit(self, t_path):
        """
        Opens the ``<t_path>`` file with the text editor.

        :param str t_path: path of the file to open.
        """
        directory = os.path.dirname(os.path.abspath(t_path))
        if os.path.isdir(directory):
            self.lastcmd_success = True

            # the directory exists, make sure that the file exists
            with open(t_path, "a") as _:
                pass

            # open it with the text editor
            texteditor.SimpleTextEditor(t_path)
        else:
            error_msg = "<b><red>[ERROR]</red></b> '" + directory + "' folder doesn't exist (can't open/create file)"
            print_formatted_text(HTML(error_msg))
            self.lastcmd_success = False

    def manage_command(self, t_command):
        """
        Executes the ``<t_command>`` command using SIS.

        :param str t_command: command to execute using SIS
        """
        # memorize command to show it on the toolbar
        command = t_command.split(" ")[0]
        self.lastcmd = command

        # try to execute the best possible method
        # to parse the command output
        cmd_res = self.sis.parsed_exec(t_command)

        if boold:
            print_formatted_text(HTML("<b><skyblue>[DEBUG]</skyblue></b> Executed command: '%s'" % t_command))
            print_formatted_text(HTML("<b><skyblue>[DEBUG]</skyblue></b> Returned: %s" % cmd_res))

        logger.debug("[%s-EXECUTED_COMMAND] %s" % (self.lastcmd, t_command))
        logger.debug("[%s-SISWRAPPER_RETURN] %s" % (self.lastcmd, cmd_res))

        # set success status (used for the bottom toolbar)
        self.lastcmd_success = cmd_res["success"]

        # if stdout is present, go to newline and show messages that are not warnings
        # > warnings are shown now only if the output parser didn't work
        if cmd_res["stdout"] is not None:
            print("")
            for line in cmd_res["stdout"].split("\r\n"):
                if not line.startswith("Warning:") or "warnings" not in cmd_res.keys():
                    print(line)
                    logger.debug("[%s-STDOUT] %s" % (self.lastcmd, line))

        # if the command returns warnings, show the warnings
        if "warnings" in cmd_res.keys():
            if len(cmd_res["warnings"]) > 0:
                print_formatted_text(HTML("\n<b>Command execution returned some "
                                          "warnings (which can probably be ignored):</b>"))
                for warning in cmd_res["warnings"]:
                    formatted_warning = HTML(warning.replace("Warning:", "<b><yellow>[Warning]</yellow></b>"))
                    print_formatted_text(formatted_warning)
                    logger.debug("[%s-WARNINGS] %s" % (self.lastcmd, formatted_warning))

        # if the command returns errors, show the errors
        if len(cmd_res["errors"]) > 0:
            print_formatted_text(HTML("\n<b>Command execution returned some ERRORS:</b>"))
            for error in cmd_res["errors"]:
                error_msg = error.replace("[ERROR]", "<b><red>[ERROR]</red></b>")

                if not error_msg.startswith("<b><red>[ERROR]</red></b>"):
                    error_msg = "<b><red>[ERROR]</red></b> " + error_msg

                print_formatted_text(HTML(error_msg))
                logger.debug("[%s-ERRORS] %s" % (self.lastcmd, error_msg))


def main():
    """
    Main function: sets up the logger, calls betterSIS and manages exceptions
    """
    # remove NullHandler
    logger.removeHandler(logger.handlers[0])

    # create syslog handler
    handler = logging.handlers.SysLogHandler(address='/dev/log', facility='local5')
    logger.addHandler(handler)

    # set handler's output format
    formatter = logging.Formatter('bettersis[%(process)d]: %(levelname)s: [%(asctime)s]%(message)s')
    handler.setFormatter(formatter)

    if boold:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    logger.addHandler(handler)
    logger.info("[PLATFORM] Using OS: %s" % platform.platform())
    logger.info("[PLATFORM] OS version: %s" % platform.version())
    logger.info("[PLATFORM] Python version: %s" % platform.python_version())

    bettersis = None

    try:
        bettersis = Bettersis()

        # show errors (if present)
        for error in bettersis.res["errors"]:
            print_formatted_text(HTML(error.replace("[ERROR]", "<b><red>[ERROR]</red></b>")))

    except Exception as e:
        logger.critical("[MAIN] This error was unexpected and interrupted the program: ", exc_info=True)
        print_formatted_text(HTML("<red>Exception:</red> {}".format(e)))
        show_ghissues_msg()

    # stop SIS's process if it is still running
    if bettersis is not None:
        if bettersis.sis.started:
            bettersis.sis.stop()


if __name__ == "__main__":
    main()
