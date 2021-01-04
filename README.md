# BETTERSIS

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
* Python 3
* the siswrapper library for Python: control SIS via Python

[Go to the index](#index)

## Installation
You can:

* (Easiest and best) Install the software:

    Download the .deb package file from [Github Release page here](https://github.com/mario33881/betterSIS/releases/latest) and
    install it using the following command:
    ```
    dpkg -i <file>
    ```
    > Replace ```<file>``` with the path of the .deb file

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

**2020-11-14 1.0.0:** <br>
First commit

[Go to the index](#index)

## Author ![](https://i.imgur.com/ej4EVF6.png)
[Stefano Zenaro (mario33881)](https://github.com/mario33881)