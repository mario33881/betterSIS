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

try:
    from ._version import __version__  # noqa: F401
except ImportError:
    from _version import __version__  # noqa: F401

boold = False
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

# ==============================================================================================
#
#                                 HELP COMMAND PARAMETERS
#
# ==============================================================================================

help_params = {
    'xilinx': None,
    'act_map': None,
    'add_inverter': None,
    'alias': None,
    'astg_add_state': None,
    'astg_contract': None,
    'astg_current': None,
    'astg_cycle': None,
    'astg_encode': None,
    'astg_flow': None,
    'astg_hfrpdft': None,
    'astg_irred': None,
    'astg_lockgraph': None,
    'astg_marking': None,
    'astg_mgc': None,
    'astg_persist': None,
    'astg_print_sg': None,
    'astg_print_stat': None,
    'astg_slow': None,
    'astg_smc': None,
    'astg_state_min': None,
    'astg_stg_scr': None,
    'astg_syn': None,
    'astg_to_f': None,
    'astg_to_stg': None,
    'atpg': None,
    'bdsyn': None,
    'buffer_opt': None,
    'c_check': None,
    'c_opt': None,
    'chng_clock': None,
    'chng_name': None,
    'collapse': None,
    'constraints': None,
    'decomp': None,
    'echo': None,
    'eliminate': None,
    'env_seq_dc': None,
    'env_verify_fsm': None,
    'equiv_nets': None,
    'espresso': None,
    'extract_seq_dc': None,
    'factor': None,
    'fanout_alg': None,
    'fanout_param': None,
    'force_init_0': None,
    'free_dc': None,
    'full_simplify': None,
    'fx': None,
    'gcx': None,
    'gkx': None,
    'help': None,
    'history': None,
    'invert': None,
    'invert_io': None,
    'ite_map': None,
    'latch_output': None,
    'map': None,
    'one_hot': None,
    'phase': None,
    'plot_blif': None,
    'power_estimate': None,
    'power_free_info': None,
    'power_print': None,
    'print': None,
    'print_altname': None,
    'print_clock': None,
    'print_delay': None,
    'print_factor': None,
    'print_gate': None,
    'print_io': None,
    'print_kernel': None,
    'print_latch': None,
    'print_level': None,
    'print_library': None,
    'print_map_stats': None,
    'print_state': None,
    'print_stats': None,
    'print_value': None,
    'quit': None,
    'read_astg': None,
    'read_blif': None,
    'read_eqn': None,
    'read_kiss': None,
    'read_library': None,
    'read_oct': None,
    'read_pla': None,
    'read_slif': None,
    'red_removal': None,
    'reduce_depth': None,
    'remove_dep': None,
    'remove_latches': None,
    'replace': None,
    'reset_name': None,
    'resub': None,
    'retime': None,
    'save': None,
    'set': None,
    'set_delay': None,
    'set_state': None,
    'short_tests': None,
    'sim_verify': None,
    'simplify': None,
    'simulate': None,
    'source': None,
    'speed_up': None,
    'speedup_alg': None,
    'state_assign': None,
    'state_minimize': None,
    'stg_cover': None,
    'stg_extract': None,
    'stg_to_astg': None,
    'stg_to_network': None,
    'sweep': None,
    'tech_decomp': None,
    'time': None,
    'timeout': None,
    'undo': None,
    'usage': None,
    'verify': None,
    'verify_fsm': None,
    'wd': None,
    'write_astg': None,
    'write_bdnet': None,
    'write_blif': None,
    'write_eqn': None,
    'write_kiss': None,
    'write_oct': None,
    'write_pds': None,
    'write_pla': None,
    'write_slif': None,
    'xl_absorb': None,
    'xl_ao': None,
    'xl_coll_ck': None,
    'xl_cover': None,
    'xl_decomp_two': None,
    'xl_imp': None,
    'xl_k_decomp': None,
    'xl_merge': None,
    'xl_part_coll': None,
    'xl_partition': None,
    'xl_rl': None,
    'xl_split': None,
    "-a": None
}

# ==============================================================================================
#
#                                 SIS COMMAND PARAMETERS
#
# ==============================================================================================

commands = {
    'xilinx': None,
    'act_map': {'-D': None,
                '-M': None,
                '-d': None,
                '-f': None,
                '-g': None,
                '-h': None,
                '-l': None,
                '-n': None,
                '-o': None,
                '-q': None,
                '-r': None,
                '-s': None,
                '-v': None},
    'add_inverter': None,
    'alias': None,
    'astg_add_state': {'-m': None, '-v': None},
    'astg_contract': {'-f': None},
    'astg_current': None,
    'astg_cycle': None,
    'astg_encode': {'-h': None, '-s': None, '-u': None, '-v': None},
    'astg_flow': {'-l': None, '-o': None, '-x': None},
    'astg_hfrpdft': {'-v': None},
    'astg_irred': {'-p': None},
    'astg_lockgraph': {'-l': None},
    'astg_marking': {'-s': None},
    'astg_mgc': None,
    'astg_persist': {'-p': None},
    'astg_print_sg': None,
    'astg_print_stat': None,
    'astg_slow': {'-F': None,
                '-d': None,
                '-f': None,
                '-m': None,
                '-s': None,
                '-t': None,
                '-u': None,
                '-v': None},
    'astg_smc': None,
    'astg_state_min': {'-B': None,
                    '-G': None,
                    '-M': None,
                    '-b': None,
                    '-c': None,
                    '-f': None,
                    '-g': None,
                    '-m': None,
                    '-o': None,
                    '-p': None,
                    '-u': None,
                    '-v': None},
    'astg_stg_scr': {'-v': None},
    'astg_syn': {'-m': None, '-r': None, '-v': None, '-x': None},
    'astg_to_f': {'-d': None, '-r': None, '-s': None, '-v': None},
    'astg_to_stg': {'-m': None, '-v': None},
    'atpg': {'-F': None,
            '-R': None,
            '-d': None,
            '-f': None,
            '-h': None,
            '-n': None,
            '-p': None,
            '-r': None,
            '-t': None,
            '-v': None,
            '-y': None},
    'bdsyn': None,
    'buffer_opt': {'-D': None,
                '-L': None,
                '-T': None,
                '-c': None,
                '-d': None,
                '-f': None,
                '-l': None,
                '-v': None},
    'c_check': None,
    'c_opt': None,
    'chng_clock': None,
    'chng_name': None,
    'collapse': None,
    'constraints': None,
    'decomp': {'-d': None, '-g': None, '-q': None},
    'echo': None,
    'eliminate': {'-l': None},
    'env_seq_dc': {'-v': None},
    'env_verify_fsm': {'-V': None, '-v': None},
    'equiv_nets': {'-v': None},
    'espresso': None,
    'extract_seq_dc': {'-m': None, '-o': None, '-v': None},
    'factor': {'-gq': None},
    'fanout_alg': {'-v': None},
    'fanout_param': {'-v': None},
    'force_init_0': None,
    'free_dc': None,
    'full_simplify': {'-d': None, '-l': None, '-m': None, '-o': None, '-v': None},
    'fx': {'-b': None, '-l': None, '-o': None, '-z': None},
    'gcx': {'-b': None, '-c': None, '-d': None, '-f': None, '-t': None},
    'gkx': {'-1': None,
            '-a': None,
            '-b': None,
            '-c': None,
            '-d': None,
            '-f': None,
            '-o': None,
            '-t': None},
    'help': help_params,
    'history': {'-h': None},
    'invert': None,
    'invert_io': None,
    'ite_map': {'-C': None,
                '-D': None,
                '-M': None,
                '-c': None,
                '-d': None,
                '-f': None,
                '-l': None,
                '-m': None,
                '-n': None,
                '-o': None,
                '-r': None,
                '-s': None,
                '-v': None},
    'latch_output': {'-v': None},
    'map': {'-A': None,
            '-B': None,
            '-F': None,
            '-G': None,
            '-W': None,
            '-b': None,
            '-f': None,
            '-i': None,
            '-m': None,
            '-n': None,
            '-p': None,
            '-r': None,
            '-s': None,
            '-v': None},
    'one_hot': None,
    'phase': {'-g': None, '-q': None, '-r': None, '-s': None, '-t': None},
    'plot_blif': {'-g': None, '-i': None, '-k': None, '-n': None, '-r': None},
    'power_estimate': {'-M': None,
                    '-N': None,
                    '-R': None,
                    '-S': None,
                    '-a': None,
                    '-d': None,
                    '-e': None,
                    '-f': None,
                    '-h': None,
                    '-i': None,
                    '-l': None,
                    '-m': None,
                    '-n': None,
                    '-s': None,
                    '-t': None,
                    '-v': None},
    'power_free_info': None,
    'power_print': None,
    'print': {'-d': None, '-n': None},
    'print_altname': None,
    'print_clock': None,
    'print_delay': {'-a': None,
                    '-f': None,
                    '-l': None,
                    '-m': None,
                    '-p': None,
                    '-r': None,
                    '-s': None},
    'print_factor': None,
    'print_gate': {'-p': None, '-s': None},
    'print_io': {'-d': None},
    'print_kernel': {'-a': None, '-s': None},
    'print_latch': {'-s': None},
    'print_level': {'-c': None, '-l': None, '-m': None, '-t': None},
    'print_library': {'-a': None, '-f': None, '-h': None, '-l': None, '-r': None},
    'print_map_stats': None,
    'print_state': None,
    'print_stats': {'-d': None, '-f': None},
    'print_value': {'-a': None, '-d': None, '-p': None},
    'quit': {'-s': None},
    'read_astg': None,
    'read_blif': None,
    'read_eqn': None,   # read_eqn and read_blif parameters are the same
    'read_kiss': None,
    'read_library': {
        '-a': None, 
        '-i': None, 
        '-n': None, 
        '-r': None,
        "synch.genlib": None,
        "mcnc.genlib": None
    },
    'read_oct': None,
    'read_pla': {'-a': None, '-c': None, '-s': None},
    'read_slif': None,
    'red_removal': {'-R': None,
                    '-d': None,
                    '-h': None,
                    '-n': None,
                    '-p': None,
                    '-q': None,
                    '-r': None,
                    '-t': None,
                    '-v': None,
                    '-y': None},
    'reduce_depth': {'-R': None,
                    '-S': None,
                    '-b': None,
                    '-d': None,
                    '-f': None,
                    '-g': None,
                    '-r': None,
                    '-s': None,
                    '-v': None},
    'remove_dep': {'-o': None, '-v': None},
    'remove_latches': {'-b': None, '-f': None, '-r': None, '-v': None},
    'replace': {'-t': None, '-v': None},
    'reset_name': {'-l': None, '-s': None},
    'resub': {'-a': None, '-b': None, '-d': None},
    'retime': {'-a': None,
            '-c': None,
            '-d': None,
            '-f': None,
            '-i': None,
            '-m': None,
            '-n': None,
            '-t': None,
            '-v': None},
    'save': None,
    'set': None,
    'set_delay': {'-A': None,
                '-D': None,
                '-I': None,
                '-L': None,
                '-R': None,
                '-S': None,
                '-W': None,
                '-a': None,
                '-d': None,
                '-i': None,
                '-l': None,
                '-r': None},
    'set_state': {'-i': None, '-s': None},
    'short_tests': {'-F': None,
                    '-V': None,
                    '-f': None,
                    '-h': None,
                    '-i': None,
                    '-r': None,
                    '-t': None,
                    '-v': None},
    'sim_verify': {'-n': None},
    'simplify': {'-d': None, '-f': None, '-i': None, '-m': None},
    'simulate': None,
    'source': {'-p': None, '-s': None, '-x': None},
    'speed_up': {'-T': None,
                '-a': None,
                '-c': None,
                '-d': None,
                '-i': None,
                '-m': None,
                '-t': None,
                '-vD': None,
                '-w': None},
    'speedup_alg': {'-v': None},
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
    'stg_cover': None,
    'stg_extract': {'-a': None, '-c': None, '-e': None},
    'stg_to_astg': {'-v': None},
    'stg_to_network': {'-e': None},
    'sweep': None,
    'tech_decomp': {'-a': None, '-o': None},
    'time': None,
    'timeout': {'-k': None, '-t': None},
    'undo': None,
    'usage': None,
    'verify': {'-m': None, '-v': None},
    'verify_fsm': {'-m': None, '-o': None, '-v': None},
    'wd': {'-c': None},
    'write_astg': {'-p': None},
    'write_bdnet': None,
    'write_blif': {'-n': None, '-s': None},
    'write_eqn': {'-s': None},
    'write_kiss': None,
    'write_oct': {'-m': None},
    'write_pds': {'-c': None, '-d': None, '-s': None},
    'write_pla': None,
    'write_slif': {'-d': None, '-n': None, '-s': None},
    'xl_absorb': {'-f': None, '-n': None, '-v': None},
    'xl_ao': {'-n': None},
    'xl_coll_ck': {'-c': None, '-k': None, '-n': None, '-v': None},
    'xl_cover': {'-h': None, '-n': None},
    'xl_decomp_two': {'-L': None,
                    '-c': None,
                    '-f': None,
                    '-l': None,
                    '-n': None,
                    '-u': None,
                    '-v': None},
    'xl_imp': {'-A': None,
            '-M': None,
            '-a': None,
            '-b': None,
            '-c': None,
            '-g': None,
            '-l': None,
            '-m': None,
            '-n': None,
            '-v': None},
    'xl_k_decomp': {'-d': None,
                    '-e': None,
                    '-f': None,
                    '-n': None,
                    '-p': None,
                    '-v': None},
    'xl_merge': {'-F': None,
                '-c': None,
                '-f': None,
                '-l': None,
                '-n': None,
                '-o': None,
                '-u': None,
                '-v': None},
    'xl_part_coll': {'-A': None,
                    '-C': None,
                    '-M': None,
                    '-a': None,
                    '-b': None,
                    '-c': None,
                    '-g': None,
                    '-l': None,
                    '-m': None,
                    '-n': None,
                    '-v': None},
    'xl_partition': {'-M': None, '-m': None, '-n': None, '-t': None, '-v': None},
    'xl_rl': {'-M': None,
            '-c': None,
            '-m': None,
            '-n': None,
            '-t': None,
            '-v': None},
    'xl_split': {'-d': None, '-n': None},
    "cd": None,
    "ls": None,
    "edit": None,
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
    "bsis_checkblif": None,
    "blif2graph": {
        "--fsm": {
            "--input": None,
            "--output": None,
            "--format": {
                "svg": None,
                "pdf": None
            },
            "--view_graph": None,
            "--style": None,
            "--debug": None,
        }
    }
}

# ==============================================================================================
#
#                                       FUNCTIONS
#
# ==============================================================================================


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


def get_siscompleter():
    """
    Returns the siscompleter object.

    These commands accept files or folders and need to be updated every time the working directory changes:
    - read_blif
    - read_eqn
    - source
    - act_map -r
    - cd
    - ls
    - edit
    - bsis_checkblif
    - blif2graph --fsm --input
    - blif2graph --fsm --style

    :return prompt_toolkit.completion.nested.NestedCompleter siscompleter: contains SIS commands with their parameters
    """

    folders = get_folders()
    files = get_files()
    
    siscompleter_commands = commands

    # update all the parameters that use files or folders
    read_blif_params = files
    read_blif_params["-a"] = None
    siscompleter_commands["read_blif"] = read_blif_params
    siscompleter_commands["read_eqn"] = read_blif_params

    source_params = {
        '-p': None, '-s': None, '-x': None,
        "script": None,
        "script.boolean": None,
        "script.algebraic": None,
        "script.rugged": None,
        "script.delay": None
    }
    source_params.update(files)
    siscompleter_commands["source"] = source_params

    siscompleter_commands["act_map"]["-r"] = files
    siscompleter_commands["cd"] = folders
    siscompleter_commands["ls"] = folders
    siscompleter_commands["edit"] = files
    siscompleter_commands["bsis_checkblif"] =  files
    siscompleter_commands["blif2graph"]["--fsm"]["--input"] = files
    siscompleter_commands["blif2graph"]["--fsm"]["--style"] = files

    if os.getenv("APPIMAGE") and os.getenv("APPDIR"):
        # running inside an AppImage
        siscompleter_commands["bsis_update"] = None

    siscompleter = NestedCompleter.from_nested_dict(siscompleter_commands)

    return siscompleter


if __name__ == "__main__":

    siscompleter = get_siscompleter()
    import pprint
    pprint.pprint(siscompleter.options)
