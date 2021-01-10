#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BETTERSIS: The modern shell for SIS
"""

__author__ = "Zenaro Stefano"

import logging
import logging.handlers
import platform

import siswrapper
from prompt_toolkit import PromptSession
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

try:
    from ._version import __version__  # noqa: F401
except ImportError:
    from _version import __version__  # noqa: F401

import siscompleter
import update_checker

boold = False
github_repository_url = "https://github.com/mario33881/betterSIS"
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Bettersis:
    """
    Shows bettersis' interactive shell.

    After the creation of an instance
    a SIS process is ready to receive commands.
    > The SIS process is started and controlled by the siswrapper library

    Shared variables:
    * res: dictionary with results of the start operation (success, errors, stdout)
    * sis: connection to SIS's process
    * lastcmd: contains the last command
    * lastcmd_success: boolean that is set to True if the last command execution was successfull
    """
    def __init__(self):
        self.res = {"success": False, "errors": [], "stdout": None}
        self.sis = siswrapper.Siswrapper()
        self.lastcmd = "FIRSTCOMMAND"
        self.lastcmd_success = False

        if self.sis.res["success"]:
            self.show_msg_on_startup()

            updates_res = update_checker.check_updates("https://api.github.com/repos/mario33881/bettersis/releases",
                                                       __version__.split(" ")[1])
            if updates_res["success"]:
                if updates_res["update_available"]:
                    print("\nNew Update Available! (latest: {})".format(updates_res["update_available"]))

            self.main()
        else:
            for error in self.sis.res["errors"]:
                self.res["errors"].append("[ERROR][INIT] Error during SIS startup: " + error)

    def show_msg_on_startup(self):
        """
        Shows the message at the shell startup.
        """
        print("                                                                       ")
        print(" ██████╗ ███████╗████████╗████████╗███████╗██████╗ ███████╗██╗███████╗ ")
        print(" ██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██║██╔════╝ ")
        print(" ██████╔╝█████╗     ██║      ██║   █████╗  ██████╔╝███████╗██║███████╗ ")
        print(" ██╔══██╗██╔══╝     ██║      ██║   ██╔══╝  ██╔══██╗╚════██║██║╚════██║ ")
        print(" ██████╔╝███████╗   ██║      ██║   ███████╗██║  ██║███████║██║███████║ ")
        print(" ╚═════╝ ╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝ ")
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

        logger.debug("[STARTUP_MESSAGE] Showing software versions "
                     "(BetterSIS: %s, Siswrapper: %s, SIS: %s)" % (__version__,
                                                                   siswrapper.__version__,
                                                                   self.sis.res["stdout"]))

    def main(self):
        """
        Starts the interactive shell.
        """
        # create a Session to memorize user commands
        session = PromptSession()

        # get the first command to show the custom toolbar
        try:
            command = session.prompt('bsis> ',
                                     completer=siscompleter.siscompleter,  # use completer from siscompleter.py
                                     complete_in_thread=True,              # better performance for autocompletion
                                     bottom_toolbar="")                    # empty toolbar

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
                                             completer=siscompleter.siscompleter,    # use completer from siscompleter.py
                                             complete_in_thread=True,                # better performance for autocompletion
                                             auto_suggest=AutoSuggestFromHistory(),  # suggest rest of command from history
                                             bottom_toolbar=self.bottom_toolbar)     # add toolbar at the bottom

                except (KeyboardInterrupt, EOFError):
                    # user pressed Ctrl+C or Ctrl+D
                    logger.debug("[MAIN] User wants to exit the software (at least one command has been executed before)")
                    break

        # stop sis process
        self.sis.stop()

    def bottom_toolbar(self):
        """
        Returns message to show inside the toolbar at the bottom.
        :return toolbar: toolbar message
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
        :param str t_commands: command(s) to execute using SIS
        """
        # loop for each command separated by ";"
        for command in t_commands.split(";"):
            self.manage_command(command.strip())

    def manage_command(self, t_command):
        """
        Executes the <t_command> command using SIS.
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


if __name__ == '__main__':

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
        print("\nPlease, (if someone didn't post this error already) create a Github Issue here: '{}'\n"
              "and share the '/var/log/pybettersis/pybettersis.log' log file\n"
              "to help the developer to fix the problem\n".format(github_repository_url + "/issues"))
        print("> If you are using the PyInstaller build, execute this command:")
        print("> 'cat /var/log/syslog | grep \"bettersis\" > pybettersis.log'\n"
              "to create the log file inside the current directory.")

    # stop SIS's process if it is still running
    if bettersis is not None:
        if bettersis.sis.started:
            bettersis.sis.stop()
