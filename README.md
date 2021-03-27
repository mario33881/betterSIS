# BETTERSIS

![BetterSIS](https://github.com/mario33881/betterSIS/workflows/BetterSIS/badge.svg)
![Update Checker](https://github.com/mario33881/betterSIS/workflows/Update%20Checker/badge.svg)
![Siscompleter](https://github.com/mario33881/betterSIS/workflows/Siscompleter/badge.svg)
![Linter](https://github.com/mario33881/betterSIS/workflows/Linter/badge.svg)

Bettersis, or bsis for short, is an **interactive shell** 
that allows you to **control SIS** (the tool for synthesis and optimization of sequential circuits)
more easily than its default shell thanks to modern features such as:

* command **autocompletion**
* command **history**
* command **suggestions**

> Read this README in: 
>
> |[English](README.md)|[Italiano](readmes/README.it.md)|
> |-|-|

<br>
<p align="center">
    <img height="350px" alt="logo" src="images/logo.svg">
</p>


<br>

<p align="center">
    <img height="350px" alt="example" src="images/example.gif">
</p>

<br>

> **Disclaimer:**
>
> I'm not affiliated with the SIS developers in any way.
>
> The aim of this software is to provide a better shell with modern features for SIS.
> 

## Index
* [Description](#description)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Changelog](#changelog)
* [Author](#author)

## Description ![](https://i.imgur.com/wMdaLI0.png)
This software provides a new interactive shell that 
**controls SIS in the background** using the ```siswrapper``` library.
> I build the ```siswrapper``` library thanks to the **pexpect** library,
> a Python library that can easily be used
> to control interactive shells by spawning and connecting to their process.

The interactive shell is controlled by the ```Bettersis``` class
which uses the ```prompt_toolkit``` library to show the promt and
the bottom toolbar and provides history and autocompletion of commands.

[Go to the index](#index)

## Requirements ![](https://i.imgur.com/H3oBumq.png)
* Unix-like OS
    > pexpect doesn't have all its features on Windows and SIS works best on linux OSes
* SIS, set in the path environment variable (callable with the ```sis``` command): the tool for synthesis and optimization of sequential circuits
    > You can [download it here](https://jackhack96.github.io/logic-synthesis/sis.html)

### Development requirements
* the requirements specified above
* Python 3 (version >= 3.6)
    > prompt-toolkit doesn't support older python 3 versions
* the siswrapper library for Python: control SIS via Python
* the prompt-toolkit library for Python: manages the modern shell and its features
* (PyInstaller to build the executable)
    > The OS you build the executable on should be the oldest possibile to support more updated OSes
    > (builds are not backwards compatible)

[Go to the index](#index)

## Installation
You can:

* (Easiest and best) Install the software:

    Download the .deb package file from [Github Release page here](https://github.com/mario33881/betterSIS/releases/latest) and
    install it using the following command:
    ```
    sudo dpkg -i <file>
    ```
    > Replace ```<file>``` with the path of the .deb file

    > You can repeat this command on a new version to update
    > the software.

    > It is necessary to use the super user to install the software,
    > (the OS will ask for the root password)

    > You can also install the .deb file by double clicking on it and then click "Install"

    Advantages:
    * Execute the shell from everywhere by executing the ```bsis``` command on the terminal.
    * There's no need to install Python and the dependencies to execute ```bettersis.py```

    You can uninstall the shell by executing this command:
    ```
    dpkg --remove bettersis
    ```

* Use the Pyinstaller executable:
    
    Download the Pyinstaller executable from [Github Release page here](https://github.com/mario33881/betterSIS/releases/latest)

    You can start the shell by executing the file:
    ```
    ./bsis
    ```
    > If the command says "Permission denied", you need to set the file type to executable using this command:
    > ```
    > chmod +x bsis
    > ```
    > Make sure that you are in the same directory as the file

    Advantages:
    * No installation required
    * There's no need to install Python and the dependencies to execute ```bettersis.py```

    Disadvantages:
    * Hard to use because of the unknown path
        > You could add it to the path environment variable,
        > otherwise you have to call it using the full path or you
        > have to read blif files using their full path

* Use the source code:

    1. Download this repository
    2. Install the dependencies (better if you use a virtual environment for Python) using the following command:
        ```
        pip3 install -r requirements.txt
        ```
        > Be sure that the current working directory is the repository root
    3. Execute ```bettersis.py```:
        ```
        python3 bettersis.py
        ```
    
    Advantages:
    * It's the only way to develop improvements for this software

    Disadvantages:
    * Hard to use because of the unknown path
        > You could add it to the path environment variable,
        > otherwise you have to call it using the full path or you
        > have to read blif files using their full path
    * You need to install Python and its dependencies

[Go to the index](#index)

## Usage

Executing the ```bettersis``` interactive shell
>
> You can execute it using:
> * Python (if you want to execute this software from source code) or
> * ```bsis``` command (if ```bettersis``` has been installed using the .deb file) or
> * ```./bsis``` command (if you want to execute Pyinstaller's executable file)

Now you can use the shell has if it was the normal SIS shell:
start reading files (using ```read_blif```), optimize circuits,
simulate them, ...

You can see a usage example in the gif at the start
of this README.

[Go to the index](#index)

## Changelog ![](https://i.imgur.com/SDKHpak.png)

**2021-03-17 1.2.0:** <br>
### Features:
* Added the ```ls``` command: it shows files and directories in the given/current path
* Added the ```cd``` command: you can use it to navigate directories from betterSIS
* Added the ```edit``` command: opens the specified file with a simple text editor
    > Editor's features: syntax highlighting, basic edit/save functionality, use the tab key to write/complete keywords
* (siswrapper feature) Added ```bsis_script``` command. Its accepted parameters are:
    * ```fsm_autoencoding_area```, useful for FSM circuits: minimizes states, automatically encodes states, optimizes area and maps the circuit by area (synch library)
        > Executed commands: ```state_minimize stamina```, ```state_assign jedi```, ```source script.rugged```, ```read_library synch.genlib```, ```map -m 0 -W -s```
    * ```fsm_autoencoding_delay```, useful for FSM circuits: minimizes states, automatically encodes states, optimizes delay and maps the circuit by delay (synch library)
        > Executed commands: ```state_minimize stamina```, ```state_assign jedi```, ```reduce_depth```, ```source script.rugged```, ```read_library synch.genlib```, ```map -n 1 -W -s```
    * ```fsm_area```, useful for FSM circuits: minimizes states, uses manual states encoding, optimizes area and maps the circuit by area (synch library)
        > Executed commands: ```state_minimize stamina```, ```stg_to_network```, ```source script.rugged```, ```read_library synch.genlib```, ```map -m 0 -W -s```
    * ```fsm_delay```, useful for FSM circuits: minimizes states, uses manual states encoding, optimizes delay and maps the circuit by delay (synch library)
        > Executed commands: ```state_minimize stamina```, ```stg_to_network```, ```reduce_depth```, ```source script.rugged```, ```read_library synch.genlib```, ```map -n 1 -W -s```
    * ```lgate_area_mcnc```, useful for combinational circuits: optimizes area and maps the circuit by area (mcnc library)
        > Executed commands: ```source script.rugged```, ```read_library mcnc.genlib```, ```map -m 0 -W -s```
    * ```lgate_delay_mcnc```, useful for combinational circuits: optimizes delay and maps the circuit by delay (mcnc library)
        > Executed commands: ```reduce_depth```, ```source script.rugged```, ```read_library mcnc.genlib```, ```map -n 1 -W -s```
    * ```lgate_area_synch```, useful for combinational circuits: optimizes area and maps the circuit by area (synch library)
        > Executed commands: ```source script.rugged```, ```read_library synch.genlib```, ```map -m 0 -W -s```
    * ```lgate_delay_synch```, useful for combinational circuits: optimizes delay and maps the circuit by delay (synch library)
        > Executed commands: ```reduce_depth```, ```source script.rugged```, ```read_library synch.genlib```, ```map -n 1 -W -s```
    * ```fsmd_area```, useful for FSMD circuits (circuits which include datapaths and an FSM): optimizes area and maps the circuit by area (synch library)
        > Executed commands: ```source script.rugged```, ```read_library synch.genlib```, ```map -m 0 -W -s```
    * ```fsmd_delay```, useful for FSMD circuits (circuits which include datapaths and an FSM): optimizes delay and maps the circuit by delay (synch library)
        > Executed commands: ```reduce_depth```, ```source script.rugged```, ```read_library synch.genlib```, ```map -n 1 -W -s```

    > This command also shows which command is executed and the statistics after some commands

    > Partial and full results are written to new BLIF files.

    > WARNING! These commands are executed in this order, thus does NOT guarantee the best result: multi-level minimization is not perfect!
    > to obtain better results you should try to execute these commands manually in a diffent order (try also to execute them more than once)
* (siswrapper feature) Now this library verifies if the stg_to_network command is successful

### Fixes:
* (siswrapper fix) Now the ```write_eqn``` command gives the expected result when used to output to a file.
     > Before this fix the ```write_blif``` method was executed instead of the correct method
* (siswrapper fix) When SIS is not installed the error message shows exactly what the problem is
* (siswrapper fix) If you call the ```write_eqn``` and ```write_blif``` method without parameters the output doesn't contain the command.
* (siswrapper fix) Can't execute the rugged script if no file as been read with a read command
* (siswrapper fix) When you execute a read command, this library calls the ```reset``` method to close the SIS session and 
  open a new session inside the folder of the input file
    > This "fixes" the ".search x file not found" error when you try to read a file that is in another folder and contains the .search keyword.
    >
    > This error was normal but not intuitive (because the imported file was present inside the same folder as the input file but not inside the current folder).
    > It was the original SIS behaviour.
* (siswrapper fix) The output of the ```print_stats``` command couldn't be intepreted as correct when the circuit had more than a 10000 literals/states
    > The output was correct but the program reported it as an error

**2021-01-09 1.1.0:** <br>
### Features:
* Added logs to syslog to help solving problems (and ```/var/log/pybettersis/pybettersis.log``` for .deb package installations)
* An "Update is available" message is shown when a new Github Release is online
* Files are shown as parameters (for faster workflow)

### Fixes:
* ```sim``` command is treated the same as the ```simulate``` command
* ```siswrapper 1.1.1``` can manage FSM outputs (fix: ```TypeError: 'NoneType' object is not subscriptable```)
* Builds are made on an older OS (Ubuntu 12.04) to improve OS versions support
> This should fix this problem: ```Error loading Python lib [...] GLIBC_2.29 not found```

**2020-11-14 1.0.0:** <br>
First commit

[Go to the index](#index)

## Author ![](https://i.imgur.com/ej4EVF6.png)
[Stefano Zenaro (mario33881)](https://github.com/mario33881)