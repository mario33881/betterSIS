# BETTERSIS

[![Unit Tests](https://github.com/mario33881/betterSIS/actions/workflows/unittests.yml/badge.svg)](https://github.com/mario33881/betterSIS/actions/workflows/unittests.yml)
![Linter](https://github.com/mario33881/betterSIS/workflows/Linter/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/bettersis/badge/?version=latest)](https://bettersis.readthedocs.io/en/latest/?badge=latest)
[![bettersis](https://snapcraft.io/bettersis/badge.svg)](https://snapcraft.io/bettersis)

Bettersis, or bsis for short, is an **interactive shell** 
that allows you to **control SIS** (the tool for synthesis and optimization of sequential circuits)
more easily than its default shell thanks to modern features such as:

* command **autocompletion**
* command **history**
* command **suggestions**

> Read this README in: 
>
> | [English](README.md) | [Italiano](readmes/README.it.md) |
> | :--- | ---: |
> |      |      |


<br>
<p align="center">
    <img style="max-width: 100%; height: 350px;" height="350px" alt="logo" src="_static/images/logo.svg">
</p>


<br>

<p align="center">
    <img style="max-width: 100%;" height="350px" alt="example" src="_static/images/example.gif">
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
    * [Development requirements](#development-requirements)
* [Installation](#installation)
* [Usage](#usage)
    * [Persistent history across sessions](#persistent-history-across-sessions)
* [Found an issue?](#found-an-issue)
* [Changelog](#changelog)
* [Author](#author)

## Description ![](https://i.imgur.com/wMdaLI0.png)
This software provides a new interactive shell that 
**controls SIS in the background** using the ```siswrapper``` library.
> I build the ```siswrapper``` library thanks to the **pexpect** library,
> a Python library that can easily be used
> to control interactive shells by spawning and connecting to their process.

The interactive shell is controlled by the ```Bettersis``` class
which uses the ```prompt_toolkit``` library to show the prompt and
the bottom toolbar and provides history and autocompletion of commands.

You can read more about betterSIS's code on readthedocs [by clicking here](https://bettersis.readthedocs.io/en/latest/readme.html).

[Go to the index](#index)

## Requirements ![](https://i.imgur.com/H3oBumq.png)
* Unix-like OS
    > pexpect doesn't have all its features on Windows and SIS works best on linux OSes
* SIS, set in the path environment variable (callable with the ```sis``` command): the tool for synthesis and optimization of sequential circuits
    > You can [download it here](https://jackhack96.github.io/logic-synthesis/sis.html)

    > Only if you deside to install a version that is not the Snap store version.
    > The Snap store version is bundled with SIS.

* (snap ONLY for the Snap store version)

### Development requirements
* the requirements specified above
* Python 3 (version >= 3.6)
    > prompt-toolkit doesn't support older python 3 versions
* the siswrapper library for Python: controls SIS via Python
* the prompt-toolkit library for Python: manages the modern shell and its features
* (PyInstaller - only if you need to build the executable)
    > The OS you build the executable on should be the oldest possibile to support more updated OSes
    > (builds are not backwards compatible)
* certifi: a library that manages SSL/TLS certificates. It is necessary to connect to Github Release to check if there are updates.
    > This is only needed for old OSes that don't have up to date certificates

[Go to the index](#index)

## Installation

> You can also see a summary of the [differences between installation methods here](https://github.com/mario33881/betterSIS/wiki/Differences-between-versions)
>
> After reading the summary you can follow the instructions to install betterSIS using your prefered method and read its advantages and disadvantages down below.

You can:

* (Easiest and best option) Install the software from the Snap store.
    
    From the command line, execute this command:
    ```
    sudo snap install bettersis
    ```
    > You need to have snap installed. You can install by [following the instructions here](https://snapcraft.io/docs/installing-snapd). 
    >
    > Note that you probably already have it installed. (especially if you are using a recent version of an Ubuntu based distro)

    <br />
    From the Graphical User Interface:

    1. Click this button:

        [![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/bettersis)

    2. Then click on the "Install" button on the top right side of the webpage
    3. Click on "View in Desktop Store" and "Choose an app"
    4. Choose "Ubuntu software" OR "Handler for snap:// URIs" OR "Snap Store"
        > These options are written in order of preference: if the first option is not available, pick the second one, etc... If none of the options are available you should probably install betterSIS using the command above.
    5. Click on the "Install" button
    6. (Optional) If you want to, you can change the permissions by clicking the "Permissions" button
        > I recommend to only enable/disable the "read/write permissions on removable media" one to access BLIF files inside USBs or ```/mnt/``` directories (if you have for example a Virtualbox shared folder).
        >
        > The other permissions are needed to access BLIF files inside the home directory and to check if updates are available (Changing these might stop the application from working correctly OR it could become un-usable until you re-enable the permissions again)
    
    Advantages over the other options:
    * Execute the shell from everywhere by executing the ```bettersis``` command
    * There's no need to install Python and the dependencies
    * SIS is bundled together with betterSIS: there is no need to install it manually
        > If you already have SIS installed don't worry: they don't conflict.
    * Automatic updates: when an update is available it will be installed automatically.
        > This allows you to always have the latest bug fixes and features.
    * Compatible with all the OS distributions that snap is compatible with
    
    Disadvantages:
    * Might use (slightly) more resources than the other options
    * SIS is bundled together with betterSIS: it occupies more disk space (3.08 MB more)
    * Automatic updates: there's no way of turning them on and off [in a convenient way](https://forum.snapcraft.io/t/snap-method-to-remove-auto-updates/21199)
    * snap is required to install it 
        > Most Ubuntu based distros and others already [have it installed by default](https://snapcraft.io/docs/installing-snapd)
    
    Advantage/Disadvantage: 
    * Snaps are very limited in permissions. This means that you can easily find Permission Errors if you try to open files in folders in which you don't have permissions to enter as a user.
        > I suggest you to open and use betterSIS from a folder that is somewhere inside the home directory (for example ```/home/myuser/Documents/myprojects/sis_projects```) and to NOT use sudo to open bettersis.
        >
        > You should also be able to give permissions to open and use betterSIS in removable media by
        > following the 6th step described above "Advantages over the other options"

    You can uninstall it by opening the betterSIS page on the Ubuntu Store/Snap store and clicking the remove/uninstall button.
    > You can follow the same steps to install it and then click on remove/uninstall instead of "install" at the 5th step.

    You can also uninstall it by executing this command:
    ```
    snap remove bettersis
    ```

* Use the AppImage executable:

    Download the .AppImage file from the [Github Release page here](https://github.com/mario33881/betterSIS/releases/latest).
    > Ignore the ```.AppImage.zsync``` file: it is used by the AppImage to find updates and you DON'T need to download it

    You can start the shell by executing the file:
    ```
    ./Bettersis-<version>-x86_64.AppImage
    ```
    > Replace ```<version>``` with the version number (like ```1.2.1```)

    > If the command says "Permission denied", you need to set the file type to executable using this command:
    > ```
    > chmod +x Bettersis-<version>-x86_64.AppImage
    > ```
    > Make sure that you are in the same directory as the file
    
    Advantages:
    * No installation required
    * There's no need to install Python and its dependencies
    * You can update the AppImage by using the ```bsis_update``` command from the betterSIS shell

    Disadvantages:
    * Hard to use because of the unknown path
        > You could add it to the path environment variable,
        > otherwise you have to call it using the full path or you
        > have to read blif files using their full path
    
    > On many distros you can put the executable inside the ```bin``` folder inside your home folder (```$HOME```): this allows you to execute the ```bsis``` command from every folder. The result is the same as installing betterSIS and executing that command.

    Delete the file to "uninstall" betterSIS.

* Install the software as a DEB package

    Download the .deb package file from the [Github Release page here](https://github.com/mario33881/betterSIS/releases/latest) and
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

    Disadvantages:
    * Might not be 100% compatible with all the OSes / OSes versions.
        > It is definitely NOT compatible with distros that are NOT based on debian.
    * No automatic updates: you need to manually download the DEB package and install it.

    You can uninstall the shell by executing this command:
    ```
    dpkg --remove bettersis
    ```

* Use the PyInstaller executable
    
    Download the PyInstaller executable from the [Github Release page here](https://github.com/mario33881/betterSIS/releases/latest) (its the one called "bsis" with no file extension)

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
    * No automatic updates: you need to manually download the new version and replace the old one
    
    > On many distros you can put the executable inside the ```bin``` folder inside your home folder (```$HOME```): this allows you to execute the ```bsis``` command from every folder. The result is the same as installing betterSIS and executing that command.

    Delete the file to "uninstall" betterSIS.

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

* (there's a [PyPI version](https://pypi.org/project/bettersis/) but you shouldn't use it. I've created it to register the name there and to avoid possible confusion)
    > It might also come in handy in the future if I need to create a new installation method

[Go to the index](#index)

## Usage

Execute the ```bettersis``` interactive shell

You can execute it using:
* Python (if you want to execute this software from source code) or
* ```bsis``` command (if ```bettersis``` has been installed using the .deb file) or
* ```./bsis``` command (if you want to execute Pyinstaller's executable file) or
    > If the executable is in a path which is inside the $PATH environment variable then you can simply call it using the ```bsis``` command 
* ```bettersis``` command (if you installed the snap version)

Now you can use the shell has if it was the normal SIS shell:
start reading files (using ```read_blif```), optimize circuits,
simulate them, ...

You can see a usage example in the gif at the start
of this README.

You can use the ```help``` command to list the old SIS command and the new betterSIS commands with a small description.
> If that description is not sufficient you can probably find more information about it in this document. If more details are needed please create an issue.

There are also some tutorials on readthedocs (in italian): [click here](https://bettersis.readthedocs.io/en/latest/tutorials/tutorials.html)

---

### Persistent history across sessions

This feature allows you to execute commands, close betterSIS, re-open it later and find the old commands using the up/down arrow keys.

This feature is disabled by default because betterSIS needs to write the ```~/.bsis_history``` file to save the old commands and the user might not want that.

To enable this feature you need to set the "```BSIS_HISTORY_ENABLED```" environment variable to "true".

> To set the environment variable modify the ```~/.bashrc``` file (or an equivalent file based on your default OS shell) and
> add this line ```export BSIS_HISTORY_ENABLED=true``` to the end of the file.

The default history file size limit is 100 KB but you can set it using the "```BSIS_HISTORY_SIZELIMIT```" environment variable (the minimum limit is 1000 bytes)
> To change the history file size limit add this line to the ```~/.bashrc``` file (or equivalent): ```export BSIS_HISTORY_SIZELIMIT=10000```.
>
> Replace "10000" with the number of bytes you wish to cap the file size.

Close and then open the terminal to use the new changes.

[Go to the index](#index)

## Found an issue?

Please create a new issue with all the details here: https://github.com/mario33881/betterSIS/issues

If you used:
* the snap version: execute the following command on the terminal to create a log file and then add its content to the issue

        cat /var/log/syslog | grep "bettersis" > pybettersis.log

* the PyInstaller version: execute the following command on the terminal to create a log file and then add its content to the issue

        cat /var/log/syslog | grep "bettersis" > pybettersis.log

* the DEB package version: add the content of the ```/var/log/pybettersis/pybettersis.log``` file to the issue

[Go to the index](#index)

## Changelog ![](https://i.imgur.com/SDKHpak.png)
**2021-09-07 1.2.1:** <br>
### Changes:
* Now the original output is kept completely intact (included warnings) and at the end of the command execution warnings are shown a second time.
    > Warnings were hidden during the command execution because they were considered redondant (to the developer) but having the full "history" of the output
    > and then a brief summary of Warnings and/or errors makes more sense.

### Features:
* Added persistent command history across different sessions (they are saved inside the ```~/.bsis_history``` file). 

  It is disabled by default and you can enable it by setting the "```BSIS_HISTORY_ENABLED```" environment variable to "true". [Check the documentation on how to enable it](#persistent-history-across-sessions) and how to set the history size limit.

* Added the ```bsis_tutorials``` command: it opens the browser on the [SIS tutorials webpage](https://bettersis.readthedocs.io/en/latest/tutorials/tutorials.html)
* Added the ```bsis_documentation``` command: it opens the browser on the [betterSIS documentation webpage](https://bettersis.readthedocs.io/en/latest/readme.html)
* Added the ```bsis_releases``` command: it opens the browser on the [download page for the latest betterSIS](https://github.com/mario33881/betterSIS/releases/latest)
* Added the ```bsis_checkblif``` command: uses the blifparser library as a basic parser/validation tool for BLIF files
* Now the ```help``` command also shows betterSIS commands
* New release on the Snap store. You can now install this software using the ```snap install bettersis``` command or using the Snap Store GUI.
* New release as an AppImage. You can think of it as having an updatable PyInstaller version.
    > Use the ```bsis_update``` to update your AppImage when an update is available
* Added two arguments to betterSIS: the ```--debug``` flag used to write more details in the log file and the ```--verbosedebug``` flag to also show debug information inside the shell
    > ```--verbosedebug``` only works when you also use the ```--debug``` flag
* The simple text editor now shows the text "Saved to file" when the user saves the file using Ctrl+S

### Fixes:
* Now the program can correctly check if an update is available.
* Fixed the ```UnicodeEncodeError: 'ascii' codec can't encode character in position 0: ordinal not in range(128)``` error
    > This happened because of the ASCII art that is shown when bettersis is executed: 
    > the terminal must be set to use an UTF-8 language using the ```$LANG``` environment variable to be able to show those ASCII characters.
    >
    > Now the ASCII art is simply not shown if the user's terminal doesn't support it.
* (siswrapper) Fixed timeout error on commands that gave paginated outputs such as the ```help read_blif``` command.

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
    > to obtain better results you should try to execute these commands manually in a different order (try also to execute them more than once)
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

### Known bugs:
* The executable version of betterSIS (both the deb package and the PyInstaller executable) can't correctly connect to Github Release to check for updates (SSL verification error)
    > This will be fixed in the next version (for now you need to manually check if an update is available)
    
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