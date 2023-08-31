# EsoDev
 An esoteric language IDE that supports syntax highlighting and execution, and installation of extensions (to support new languages)

EsoDev is an IDE of esoteric languages (esolangs). It's written in Python. It supports syntax highlighting, execution, and extensions. It only supports Windows 7+. (support for Windows 7 and 8 are untested)

Initially, it has extensions pre-installed for [brainfuck](https://esolangs.org/wiki/Brainfuck), [Random Brainfuck](https://esolangs.org/wiki/Random_Brainfuck), [Deadfish](https://esolangs.org/wiki/Deadfish) and [Weeeeeeeeeeeeeeeeeeeeeeeeeeeeee](https://esolangs.org/wiki/Weeeeeeeeeeeeeeeeeeeeeeeeeeeeee), these extensions cannot be uninstalled by the user unless deleted manually.

However, client-side users can develop there extensions for other esolangs. To build an extension, you need Python plus an interpreter of the esolang as a Windows executable. The Windows executable is usually build using C/C++, but it is also obviously possible to build it via Python, C&#35;, Rust, and other languages. Finally you pack all the files together into a zip file, which is the extensio file. Extension files are to be smaller than 2 GiB.
