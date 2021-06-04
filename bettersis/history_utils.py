#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
**BETTERSIS.HISTORY_UTILS**:
Defines functions to keep control of the size of the history file.
"""

__author__ = "Zenaro Stefano"

import shutil
import os
import tempfile

try:
    from ._version import __version__  # noqa: F401
except ImportError:
    from _version import __version__  # noqa: F401


def remove_blank_lines(t_input, t_output):
    """
    Reads a file and rewrites its content
    skipping blank lines.

    :param str t_input: path to the input file
    :param str t_output: path to the output file
    """
    fout = open(t_output, "wb")

    with open(t_input, "r") as fin:
        line = fin.readline()
        while line != "":
            linestrip = line.strip()

            # skip empty lines
            if linestrip != "":
                fout.write(line.encode())

            line = fin.readline()

    fout.close()


def truncate_beginning(t_input, t_output, t_limit):
    """
    Removes the first chars/bytes from
    the ``<t_input>`` file and saves the last ``<t_limit>`` bytes
    inside the ``<t_output>`` file.

    :param str t_input: path to the input file
    :param str t_output: path to the output file
    :param int t_limit: number of chars/bytes to keep from the end of the file
    """
    with open(t_input, 'rb') as fin:
        fin.seek(-int(t_limit), 2)
        with open(t_output, 'wb') as fout:
            for chunk in iter(lambda: fin.read(16384), b''):
                fout.write(chunk)


def limit_history_size(t_file, t_size_limit, t_output=None):
    """
    Limits the size of ``<t_file>`` to ``<t_size_limit>`` bytes/chars.
    If ``<t_output>`` is set the output is the ``<t_output>`` file,
    else the ``<t_file>`` is overwritten.

    :param str t_file: path of the file of which to limit its size
    :param int t_size_limit: limit of ``<t_file>`` size
    :param str t_output: output file path (if equal to None ``<t_file>`` gets modified in place)
    """
    t_limit = t_size_limit

    if t_size_limit < 1000:
        t_limit = 1000

    filesize = os.path.getsize(t_file)

    # prepare a temporary folder with partial files
    tmp_dir = tempfile.TemporaryDirectory()
    filename = os.path.basename(t_file)
    tmp_filepath = os.path.join(tmp_dir.name, filename)

    # remove blank lines
    remove_blank_lines(t_file, tmp_filepath + ".nospaces.txt")

    # if the file size permits to read last t_limit bytes, remove the first bytes
    if filesize > t_size_limit:
        # truncate the file by keeping the last t_limit chars/bytes
        truncate_beginning(tmp_filepath + ".nospaces.txt", tmp_filepath + ".trunc.txt", t_limit)

        # be sure that the first command starts with the timestamps
        found_ts = False
        with open(tmp_filepath + ".trunc.txt", "r") as fin:
            with open(tmp_filepath + ".fixed.txt", "wb") as fout:
                line = fin.readline()
                while line != "":
                    linestrip = line.strip()

                    if linestrip.startswith("#"):
                        found_ts = True

                    if found_ts:
                        fout.write(line.encode())

                    line = fin.readline()

        # if specified, copy the file to the <t_output> path
        # else overwrite the input file (<t_file>)
        if t_output:
            shutil.copyfile(tmp_filepath + ".fixed.txt", t_output)
        else:
            shutil.copyfile(tmp_filepath + ".fixed.txt", t_file)
    else:
        # "return" the file with no blank lines

        # if specified, copy the file to the <t_output> path
        # else overwrite the input file (<t_file>)
        if t_output:
            shutil.copyfile(tmp_filepath + ".nospaces.txt", t_output)
        else:
            shutil.copyfile(tmp_filepath + ".nospaces.txt", t_file)

    tmp_dir.cleanup()
