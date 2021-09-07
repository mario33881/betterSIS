#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**BETTERSIS.TEXTEDITOR**: A simple text editor for betterSIS.

Features:

- edit (and save) files
- syntax highlighting

.. note:: This code was inspired by the prompt_toolkit example:
          https://github.com/prompt-toolkit/python-prompt-toolkit/blob/7fdd81597597a7a2f47655238b7f0cb3ea637091/examples/full-screen/text-editor.py  # noqa: E501

"""

__author__ = "Zenaro Stefano"

import os

from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import (
    HSplit,
    VSplit,
    Window,
    WindowAlign,
)
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import (
    TextArea,
)

try:
    from ._version import __version__  # noqa: F401
except ImportError:
    from _version import __version__  # noqa: F401

keywords = [
    ".model",
    ".inputs",
    ".outputs",
    ".names",
    ".exdc",
    ".start_kiss",
    ".end_kiss",
    ".i",
    ".o",
    ".s",
    ".p",
    ".r",
    ".code",
    ".subckt",
    ".search",
    ".latch",
    ".end"
]


class SisLexer(Lexer):
    """
    Defines a lexer for the text editor.
    """
    def lex_document(self, document):
        """
        Reads document to parse each line.

        :param document: document to parse
        :return function get_line: function that parses lines
        """

        def get_line(lineno):
            """
            Reads and parses the lines one by one.

            :param int lineno: row number of the line
            :return list colored_words: list of text (colored keywords)
            """
            colored_words = []
            commented = False

            # loop for each word in the line
            for word in document.lines[lineno].split(" "):
                color = "White"

                # set blue color for keywords
                if word in keywords:
                    color = "DeepSkyBlue"

                # set green color for comments
                if commented:
                    color = "Green"

                # add each char of the word with the correct color
                for char in word:
                    if char == "#":
                        # remember that the next chars are commented
                        color = "Green"
                        commented = True
                    colored_words.append((color, char))

                colored_words.append((color, " "))

            return colored_words

        return get_line


class SimpleTextEditor():
    """
    Opens the ``<t_file>`` file with the a simple CLI text editor.

    :param str t_file: file to open with the text editor
    """
    def __init__(self, t_file):
        self.saved_file = False  # used to set the toolbar text to "saved to file"

        if not os.path.isfile(t_file):
            raise Exception("ERROR: '{}' file doesn't exist".format(t_file))

        # define highlighter/completer
        sis_completer = WordCompleter(keywords, ignore_case=False)

        # create the text field with the content of the file
        self.text_field = None

        with open(t_file, "r") as f:
            self.text_field = TextArea(
                lexer=SisLexer(),
                text=f.read(),
                scrollbar=False,
                line_numbers=True,
                completer=sis_completer,
                style='bg:#131926'
            )

        # create a layout with the text field and the statusbar
        body = HSplit(
            [
                self.text_field,
                VSplit(
                    [
                        Window(
                            FormattedTextControl(self.get_statusbar_text), style="class:status"
                        ),
                        Window(
                            FormattedTextControl(self.get_statusbar_right_text),
                            style="class:status.right",
                            width=9,
                            align=WindowAlign.RIGHT,
                        ),
                    ],
                    height=1,
                )
            ]
        )

        # Global key bindings.
        bindings = KeyBindings()

        # define control hotkeys

        @bindings.add("c-c")
        def _(event):
            "Closes the app (hotkey Ctrl + C)"
            get_app().exit()

        @bindings.add("c-s")
        def _(event):
            """
            Saves the file (hotkey Ctrl + S)
            and sets self.saved_file to True to show in the toolbar the text "saved to file"
            """
            self.saved_file = True
            with open(t_file, "w") as f:
                f.write(self.text_field.text)

        @bindings.add("c-u")
        def _(event):
            """
            Undoes the last action (hotkey Ctrl + U)
            """
            self.text_field.buffer.undo()

        style = Style.from_dict(
            {
                "status": "reverse",
                "shadow": "bg:#440044",
            }
        )

        # create a layout object
        layout = Layout(body, focused_element=self.text_field)

        # create and start the app
        application = Application(
            layout=layout,
            enable_page_navigation_bindings=True,
            style=style,
            mouse_support=True,
            full_screen=True,
            key_bindings=bindings
        )

        application.run()

    def get_statusbar_text(self):
        """
        Shows control hotkeys.

        If the user saved the file with Ctrl-S show "Saved to file" instead.

        :return str: string with the control commands
        """
        if self.saved_file:
            self.saved_file = False
            return " | Saved to file |"

        return " | Ctrl-C: exit | Ctrl-S: save | Ctrl-U: undo |"

    def get_statusbar_right_text(self):
        """
        Shows the cursor position on the bottom right of the screen.

        :return str: string with cursor position
        """
        return " {}:{}  ".format(
            self.text_field.document.cursor_position_row + 1,
            self.text_field.document.cursor_position_col + 1,
        )


if __name__ == "__main__":

    try:
        SimpleTextEditor("file.txt")
    except Exception as e:
        print("expected error:", e)

    print("-" * 50)
