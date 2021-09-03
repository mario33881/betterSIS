#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**BETTERSIS.SISCOMPLETER**:
Defines an object that helps for autocompletion of commands.
"""

__author__ = "Zenaro Stefano"

import os
import logging
from prompt_toolkit.completion import NestedCompleter

import siswrapper

try:
    from ._version import __version__  # noqa: F401
except ImportError:
    from _version import __version__  # noqa: F401

boold = False
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def get_files():
    """
    Returns a dictionary with the files
    in the current directory.

    :return dict res: dictionary with files (the keys are filename, value is None)
    """
    res = {}
    for f in os.listdir():
        if os.path.isfile(f):
            res[f] = None
    return res


def get_folders():
    """
    Returns a dictionary with the folders
    in the current directory.

    :return dict res: dictionary with directories (the keys are directory names, value is None)
    """
    res = {}

    res[".."] = None

    for f in os.listdir():
        if os.path.isdir(f):
            res[f] = None

    return res


def get_act_map_params():
    """
    Returns parameters for the act_map command.

    :return dict params: dictionary with command parameters
    """
    files = get_files()
    params = {}
    params.update({
        "-h": None,
        "-n": None,
        "-f": None,
        "-g": None,
        "-d": None,
        "-r": files,
        "-M": None,
        "-q": None,
        "-o": None,
        "-l": None,
        "-D": None,
        "-s": None,
        "-v": None,
        })

    return params


def get_read_blif_params():
    """
    Returns parameters for the read_blif command.

    :return dict params: dictionary with command parameters
    """
    files = get_files()

    params = {
        "-a": files
    }

    params.update(files)
    return params


def get_read_eqn_params():
    """
    Returns parameters for the read_eqn command.

    :return dict params: dictionary with command parameters
    """
    files = get_files()

    params = {
        "-a": files
    }

    params.update(files)
    return params


def get_commands():  # noqa: C901
    """
    Returns commands.

    .. note:: TODO: Probably should put a similar function inside the siswrapper library

    :return dict commands: dictionary with commands
    """
    params = None

    sis = siswrapper.Siswrapper()
    if sis.res["success"]:
        params = {}
        help_res = sis.exec("help")

        commands = help_res["stdout"].split("\r\n")

        # get index of the start of the commands
        # > can't split on spaces because the longest command collides
        # > with the one after it
        isspace = False
        indexes = []
        for index, letter in enumerate(commands[0]):
            if letter == " ":
                isspace = True
            elif letter != " " and isspace is True:
                isspace = False
                indexes.append(index)

        if indexes[-1] != len(commands[0]) - 1:
            indexes.append(len(commands[0]) - 1)

        # repeat this for the second line
        # (just to be sure that the longest command is not on the first line)
        isspace = False
        indexes_secondline = []
        for index, letter in enumerate(commands[1]):
            if letter == " ":
                isspace = True
            elif letter != " " and isspace is True:
                isspace = False
                indexes_secondline.append(index)

        if indexes_secondline[-1] != len(commands[1]) - 1:
            indexes_secondline.append(len(commands[1]) - 1)

        if boold:
            print("GET_COMMANDS:")
            print("indexes line one: ", indexes)
            print("indexes line two: ", indexes_secondline)

        # get the line with the most commands separated by spaces
        correct_indexes = indexes_secondline
        if len(indexes) > len(indexes_secondline):
            correct_indexes = indexes

        # loop for each command and prepare the bettersis parameters
        for line in commands:
            previndex = 0
            for index in correct_indexes:
                command = line[previndex:index].strip()
                params[command] = None

                if boold:
                    print("Element from position {} to {}: {}".format(previndex, index, command))

                previndex = index

    return params


def get_source_params():
    """
    Returns parameters for the source command.

    :return dict params: dictionary with command parameters
    """
    files = get_files()

    params = {
        "script": None,
        "script.boolean": None,
        "script.algebraic": None,
        "script.rugged": None,
        "script.delay": None
    }

    params.update(files)
    return params


def get_siscompleter():
    """
    Returns the siscompleter object.

    :return prompt_toolkit.completion.nested.NestedCompleter siscompleter: contains SIS commands with their parameters
    """
    commands = {
        "act_map": get_act_map_params(),
        "add_inverter": None,
        "alias": None,
        "astg_add_state": None,
        "astg_contract": None,
        "astg_current": None,
        "astg_encode": None,
        "astg_lockgraph": None,
        "astg_marking": None,
        "astg_persist": None,
        "astg_print_sg": None,
        "astg_print_stat": None,
        "astg_slow": None,
        "astg_state_min": None,
        "astg_stg_scr": None,
        "astg_syn": None,
        "astg_to_f": None,
        "astg_to_stg": None,
        "atpg": None,
        "bdsyn": None,
        "buffer_opt": None,
        "c_check": None,
        "c_opt": None,
        "chng_clock": None,
        "chng_name": None,
        "collapse": None,
        "constraints": None,
        "decomp": {
            "-g": None,
            "-q": None,
            "-d": None
        },
        "echo": None,
        "eliminate": {
            "-l": None
        },
        "env_seq_dc": None,
        "env_verify_fsm": None,
        "equiv_nets": None,
        "espresso": None,
        "exit": None,
        "extract_seq_dc": None,
        "factor": None,
        "fanout_alg": None,
        "fanout_param": None,
        "force_init_0": None,
        "free_dc": None,
        "full_simplify": None,
        "fx": None,
        "gcx": None,
        "gkx": None,
        "help": get_commands(),
        "history": None,
        "invert": None,
        "invert_io": None,
        "ite_map": None,
        "latch_output": None,
        "map": None,
        "one_hot": None,
        "phase": None,
        "power_estimate": None,
        "power_free_info": None,
        "power_print": None,
        "print": None,
        "print_altname": None,
        "print_clock": None,
        "print_delay": None,
        "print_factor": None,
        "print_gate": None,
        "print_io": None,
        "print_kernel": None,
        "print_latch": None,
        "print_level": None,
        "print_library": None,
        "print_map_stats": None,
        "print_state": None,
        "print_stats": None,
        "print_value": None,
        "quit": None,
        "read_astg": None,
        "read_blif": get_read_blif_params(),
        "read_eqn": get_read_eqn_params(),
        "read_kiss": None,
        "read_library": None,
        "read_pla": None,
        "read_slif": None,
        "red_removal": None,
        "reduce_depth": None,
        "remove_dep": None,
        "remove_latches": None,
        "replace": None,
        "reset_name": None,
        "resub": None,
        "retime": None,
        "save": None,
        "set": None,
        "set_delay": None,
        "set_state": None,
        "short_tests": None,
        "sim_verify": None,
        "simplify": None,
        "simulate": None,
        "source": get_source_params(),
        "speed_up": None,
        "speedup_alg": None,
        "state_assign": {
            "jedi": {
                "-e": None,
                "-h": None
            },
            "nova": {
                "-e": None,
                "-h": None
            }
        },
        "state_minimize": {
            "stamina": {
                "-h": None
            }
        },
        "stg_cover": None,
        "stg_extract": None,
        "stg_to_astg": None,
        "stg_to_network": None,
        "sweep": None,
        "tech_decomp": None,
        "time": None,
        "timeout": None,
        "unalias": None,
        "undo": None,
        "unset": None,
        "usage": None,
        "verify": None,
        "verify_fsm": None,
        "wd": None,
        "write_astg": None,
        "write_bdnet": None,
        "write_blif": {
            "-s": None,
            "-n": None
        },
        "write_eqn": {
            "-s": None
        },
        "write_kiss": None,
        "write_pds": None,
        "write_pla": None,
        "write_slif": None,
        "xl_absorb": None,
        "xl_ao": None,
        "xl_coll_ck": None,
        "xl_cover": None,
        "xl_decomp_two": None,
        "xl_imp": None,
        "xl_k_decomp": None,
        "xl_merge": None,
        "xl_part_coll": None,
        "xl_partition": None,
        "xl_rl": None,
        "xl_split": None,
        "cd": get_folders(),
        "ls": get_folders(),
        "edit": get_files(),
        "bsis_script": {
            "fsm_autoencoding_area": None,
            "fsm_autoencoding_delay": None,
            "fsm_area": None,
            "fsm_delay": None,
            "lgate_area_mcnc": None,
            "lgate_delay_mcnc": None,
            "lgate_area_synch": None,
            "lgate_delay_synch": None,
            "fsmd_area": None,
            "fsmd_delay": None
        },
        "bsis_tutorials": None,
        "bsis_documentation": None,
        "bsis_releases": None,
        "bsis_checkblif": get_files()
    }

    if os.getenv("APPIMAGE") and os.getenv("APPDIR"):
        # running inside an AppImage
        commands["bsis_update"] = None

    siscompleter = NestedCompleter.from_nested_dict(commands)

    return siscompleter


if __name__ == "__main__":

    print("commands:\n")
    commands = get_commands()
    for command in commands.keys():
        print("* '{}'".format(command))
