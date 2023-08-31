# EsoDev
 An esoteric language IDE that supports syntax highlighting and execution, and installation of extensions (to support new languages)

EsoDev is an IDE of esoteric languages (esolangs). It's written in Python. It supports syntax highlighting, execution, and extensions. It only supports Windows 7+. (support for Windows 7 and 8 are untested)

Initially, it has extensions pre-installed for [brainfuck](https://esolangs.org/wiki/Brainfuck), [Random Brainfuck](https://esolangs.org/wiki/Random_Brainfuck), [Deadfish](https://esolangs.org/wiki/Deadfish) and [Weeeeeeeeeeeeeeeeeeeeeeeeeeeeee](https://esolangs.org/wiki/Weeeeeeeeeeeeeeeeeeeeeeeeeeeeee), these extensions cannot be uninstalled by the user unless deleted manually.

However, client-side users can develop there own extensions for other esolangs. To build an extension, you need Python plus an interpreter of the esolang as a Windows executable. The Windows executable is usually build using C/C++, but it is also obviously possible to build it via Python, C&#35;, Rust, and other languages. Finally you pack all the files together into a zip file, which is the extensio file. Extension files are to be smaller than 2 GiB.

## Menus
File
* New
* Open
* Save
* Save as
* Recent files
* Clear history
* Exit
* 
Edit
* Copy
* Paste
* Cut
* Select all
* Undo
* Redo
* 
Execution
* Run
  
Options
* Language
* Default language
* Syntax highlighting
* Reset and quit

Help
* About
* Keyboard shortcuts
  
Extensions
* Install
* Uninstall

## Bugs
There is a bug: If you enable syntax highlighting, you can't use undo and redo. The author is probably not good enough at programming to fix it, so if you know how to fix it, you can post an issue.

## Things currently unsupported by EsoDev
1. Debugging
2. Undo and redo when syntax highlighting (an shown above in the Bugs section)

That is EsoDev, have fun :D
