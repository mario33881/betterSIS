#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PARSE_HELP_FILES:
This script tries to get as much information as possible about
the parameters of each command available on SIS
"""
import os

if __name__ == "__main__":

    all_usages = []
    for filepath in os.listdir():
        if not os.path.isfile(filepath):
            continue
        
        if filepath == "parse_help_files.py":
            continue

        with open(filepath, "r") as f:

            line = f.readline()
            n_paragraph = 0
            paragraphs = []

            paragraph = line.strip() + "\n"
            while line != "":
                paragraph += line.strip() + "\n"
                if line.strip() == "":
                    n_paragraph += 1
                    paragraphs.append(paragraph.strip())
                    paragraph = ""

                line = f.readline()

            #for p in paragraphs:
            #    print(p)
            #    print("------------------------------------------------------------")
            
            all_usages.append(paragraphs[2].replace("\n", " "))
            #print(paragraphs[2])
    
    command_dicts = {}
    commands = []
    for usage in all_usages:
        print(usage)
        
        components = [a.strip().replace("]", "") for a in usage.split("[")]
        print(components)
        command = components[0]
        commands.append(command)
        components = components[1:]

        command_dict = {}
        print("")
        print("command: ", command)
        for c in components:
            if " " in c and c.startswith("-"):
                flag = c.split(" ")[0]
                if "|" in flag:
                    for option in flag.split("|"):
                        command_dict["-" + option.strip().strip("-")] = None
                        print("-" + option.strip().strip("-"))
                else:
                    command_dict[flag] = None
                    print(flag)
            elif "|" in c:
                flag = c
                for option in flag.split("|"):
                    command_dict["-" + option.strip().strip("-")] = None
                    print("-" + option.strip().strip("-"))
            elif c.startswith("<") and c.endswith(">"):
                print(c, " (ignoring it because it is not an optional parameter)")
            elif c.startswith("-"):
                for l in c[1:]:
                    command_dict["-" + l] = None
                    print("-" + l)

        print("")
        
        if len(command_dict.keys()) == 0:
            print("None")
            command_dicts[command] = None
        else:
            print(command_dict)
            command_dicts[command] = command_dict

        print("-"*10)

    print("length:", len(all_usages))

    print("=="*10)
    import pprint
    pprint.pprint(command_dicts)

    print("")
    help_parameters = {}
    for c in commands:
        help_parameters[c] = None
    
    pprint.pprint(help_parameters)