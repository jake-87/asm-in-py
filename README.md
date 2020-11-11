# asm-in-py
An implementation of intel x86 32 bit  assembly in python 3.

## Install
Linux:
Simply extract the files into a directory, and run ```python main.py```. Still working on an install script :p

MacOS:
Same as Linux, make sure that you have python installed.

Windows:
I don't own a windows machine, so idk

## Contributing: 
Just make a pull request. I will test everything, and merge/reject as suitable.

Naming releases: 

 (1,2,etc).## : Major releases. Only used for major changes to the codebase.
 
 #.(1,2,etc)# : Minor releases. Used for most changes over 2 lines of code.
 
 #.#(1,2,etc) : Patches. Only for bugfixes.

## URGENT PRs

Makefile

`int`, but only `int 0x80` right now.

## Basics:
So far the project is basically the same as x86, with a few differences:

1. Variables are assigned via `mov (varname),(content)`. This is due to the fact that seperate .data and .text sections would  be complicated for a small project. 

2. Varables cannot contain spaces __for now__, as they require some clever thinking that i'm  still working on.

3. The end of the file is declared via just typing in EOF on its own line

So for an example, here is "Hello!"

mov eax,4 ;set-syscall-to-print

mov ecx,Hello! ;set-what-to-print

mov edx,6 ;length-of-ecx

int 0x80 ;call-the-syscall

mov eax,1 ;set-syscall-to-exit

int 0x80 ;call-syscall
