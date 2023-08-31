# EsoDev
 An esoteric language IDE that supports syntax highlighting and execution, and installation of extensions (to support new languages)

EsoDev is an IDE of esoteric languages (esolangs). It's written in Python. It supports syntax highlighting, execution, and extensions. It only supports Windows 7+. (support for Windows 7 and 8 are untested)

Initially, it has extensions pre-installed for [brainfuck](https://esolangs.org/wiki/Brainfuck), [Random Brainfuck](https://esolangs.org/wiki/Random_Brainfuck), [Deadfish](https://esolangs.org/wiki/Deadfish) and [Weeeeeeeeeeeeeeeeeeeeeeeeeeeeee](https://esolangs.org/wiki/Weeeeeeeeeeeeeeeeeeeeeeeeeeeeee), these extensions cannot be uninstalled by the user unless deleted manually.

However, client-side users can develop there own extensions for other esolangs. To build an extension, you need Python plus an interpreter of the esolang as a Windows executable. The Windows executable is usually build using C/C++, but it is also obviously possible to build it via Python, C&#35;, Rust, and other languages. Finally you pack all the files together into a zip file, which is the extension file. Extension files are to be smaller than 2 GiB.

*Note: The author admits that his code was a mess*
## Changelog
* 1.0.0
  * First version
* 1.0.1
  * Minor bugfixes
  * Added support for enabling/disabling language guessing
  * Added footer showing current language
  * Added support for directories in extensions
## Menus
File
* New
* Open
* Save
* Save as
* Recent files
* Clear history
* Exit

Edit
* Copy
* Paste
* Cut
* Select all
* Undo
* Redo

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

## Note for anyone who would like to build the project
To build the project, you need: PySide2, PyInstaller, and a C++ compiler.
1. Copy `EsoDev.ico`, `ui_about.py`, `ui_keyboard_shortcuts.py`, `ui_ui.py`, `main.py`, `img_rc.py` and `extinstaller.py` to a separate folder (do **not** copy other files yet), say you copied it to `D:\test`.
2. Run `pyinstaller -D -w main.py -n "EsoDev --hidden-import runpy -i EsoDev.ico` in `D:\test`.
3. A folder `D:\test\dist\EsoDev\` will be created. Copy the folders `extensions` and `examples`, and the files `EsoDev.png` and `conf.json` to that folder.
4. Use your favorite C++ compiler to compile Pauser.cpp and copy the resulting `Pauser.exe` to `D:\test\dist\EsoDev\`. Then compile all the C++ files in the `bin` directory and copy the resulting executables to `D:\test\dist\EsoDev\bin` (you have to manually create that directory)
After the steps 1~4, the directory tree of the folder `D:\test\dist\EsoDev` should be like this:
```text
EsoDev                                   
├─ bin                                   
│  ├─ brainfuck.exe                      
│  ├─ Deadfish.exe                       
│  ├─ RandomBrainfuck.exe                
│  └─ wee.exe                            
├─ examples                              
│  ├─ cat.b                              
│  ├─ dbfi.b                             
│  ├─ dice.rbf                           
│  ├─ e.b                                
│  ├─ golden.b                           
│  ├─ hello.b                            
│  ├─ hello.wee                          
│  ├─ hi.wee                             
│  ├─ infinite_loop.wee                  
│  ├─ random_decimal.rbf                 
│  ├─ random_letter.rbf                  
│  ├─ testcase1.df                       
│  ├─ testcase2.df                       
│  └─ testcase3.df                       
├─ extensions                            
│  ├─ __pycache__                        
│  │  └─ __init__.cpython-37.pyc         
│  ├─ brainfuck.py                       
│  ├─ deadfish.py                        
│  ├─ list.json                          
│  ├─ rbf.py                             
│  ├─ wee.py                             
│  └─ __init__.py                        
├─ PySide2                               
│  ├─ plugins                            
│  │  ├─ bearer                          
│  │  │  └─ qgenericbearer.dll           
│  │  ├─ generic                         
│  │  │  └─ qtuiotouchplugin.dll         
│  │  ├─ iconengines                     
│  │  │  └─ qsvgicon.dll                 
│  │  ├─ imageformats                    
│  │  │  ├─ qgif.dll                     
│  │  │  ├─ qicns.dll                    
│  │  │  ├─ qico.dll                     
│  │  │  ├─ qjpeg.dll                    
│  │  │  ├─ qpdf.dll                     
│  │  │  ├─ qsvg.dll                     
│  │  │  ├─ qtga.dll                     
│  │  │  ├─ qtiff.dll                    
│  │  │  ├─ qwbmp.dll                    
│  │  │  └─ qwebp.dll                    
│  │  ├─ platforminputcontexts           
│  │  │  └─ qtvirtualkeyboardplugin.dll  
│  │  ├─ platforms                       
│  │  │  ├─ qdirect2d.dll                
│  │  │  ├─ qminimal.dll                 
│  │  │  ├─ qoffscreen.dll               
│  │  │  ├─ qwebgl.dll                   
│  │  │  └─ qwindows.dll                 
│  │  ├─ platformthemes                  
│  │  │  └─ qxdgdesktopportal.dll        
│  │  └─ styles                          
│  │     └─ qwindowsvistastyle.dll       
│  ├─ translations                       
│  │  ├─ qtbase_ar.qm                    
│  │  ├─ qtbase_bg.qm                    
│  │  ├─ qtbase_ca.qm                    
│  │  ├─ qtbase_cs.qm                    
│  │  ├─ qtbase_da.qm                    
│  │  ├─ qtbase_de.qm                    
│  │  ├─ qtbase_en.qm                    
│  │  ├─ qtbase_es.qm                    
│  │  ├─ qtbase_fi.qm                    
│  │  ├─ qtbase_fr.qm                    
│  │  ├─ qtbase_gd.qm                    
│  │  ├─ qtbase_he.qm                    
│  │  ├─ qtbase_hu.qm                    
│  │  ├─ qtbase_it.qm                    
│  │  ├─ qtbase_ja.qm                    
│  │  ├─ qtbase_ko.qm                    
│  │  ├─ qtbase_lv.qm                    
│  │  ├─ qtbase_pl.qm                    
│  │  ├─ qtbase_ru.qm                    
│  │  ├─ qtbase_sk.qm                    
│  │  ├─ qtbase_tr.qm                    
│  │  ├─ qtbase_uk.qm                    
│  │  ├─ qtbase_zh_TW.qm                 
│  │  ├─ qt_ar.qm                        
│  │  ├─ qt_bg.qm                        
│  │  ├─ qt_ca.qm                        
│  │  ├─ qt_cs.qm                        
│  │  ├─ qt_da.qm                        
│  │  ├─ qt_de.qm                        
│  │  ├─ qt_en.qm                        
│  │  ├─ qt_es.qm                        
│  │  ├─ qt_fa.qm                        
│  │  ├─ qt_fi.qm                        
│  │  ├─ qt_fr.qm                        
│  │  ├─ qt_gd.qm                        
│  │  ├─ qt_gl.qm                        
│  │  ├─ qt_he.qm                        
│  │  ├─ qt_help_ar.qm                   
│  │  ├─ qt_help_bg.qm                   
│  │  ├─ qt_help_ca.qm                   
│  │  ├─ qt_help_cs.qm                   
│  │  ├─ qt_help_da.qm                   
│  │  ├─ qt_help_de.qm                   
│  │  ├─ qt_help_en.qm                   
│  │  ├─ qt_help_es.qm                   
│  │  ├─ qt_help_fr.qm                   
│  │  ├─ qt_help_gl.qm                   
│  │  ├─ qt_help_hu.qm                   
│  │  ├─ qt_help_it.qm                   
│  │  ├─ qt_help_ja.qm                   
│  │  ├─ qt_help_ko.qm                   
│  │  ├─ qt_help_pl.qm                   
│  │  ├─ qt_help_ru.qm                   
│  │  ├─ qt_help_sk.qm                   
│  │  ├─ qt_help_sl.qm                   
│  │  ├─ qt_help_tr.qm                   
│  │  ├─ qt_help_uk.qm                   
│  │  ├─ qt_help_zh_CN.qm                
│  │  ├─ qt_help_zh_TW.qm                
│  │  ├─ qt_hu.qm                        
│  │  ├─ qt_it.qm                        
│  │  ├─ qt_ja.qm                        
│  │  ├─ qt_ko.qm                        
│  │  ├─ qt_lt.qm                        
│  │  ├─ qt_lv.qm                        
│  │  ├─ qt_pl.qm                        
│  │  ├─ qt_pt.qm                        
│  │  ├─ qt_ru.qm                        
│  │  ├─ qt_sk.qm                        
│  │  ├─ qt_sl.qm                        
│  │  ├─ qt_sv.qm                        
│  │  ├─ qt_tr.qm                        
│  │  ├─ qt_uk.qm                        
│  │  ├─ qt_zh_CN.qm                     
│  │  └─ qt_zh_TW.qm                     
│  ├─ d3dcompiler_47.dll                 
│  ├─ libegl.dll                         
│  ├─ libglesv2.dll                      
│  ├─ MSVCP140.dll                       
│  ├─ MSVCP140_1.dll                     
│  ├─ opengl32sw.dll                     
│  ├─ pyside2.abi3.dll                   
│  ├─ Qt5Core.dll                        
│  ├─ Qt5DBus.dll                        
│  ├─ Qt5Gui.dll                         
│  ├─ Qt5Network.dll                     
│  ├─ Qt5Pdf.dll                         
│  ├─ Qt5Qml.dll                         
│  ├─ Qt5QmlModels.dll                   
│  ├─ Qt5Quick.dll                       
│  ├─ Qt5Svg.dll                         
│  ├─ Qt5VirtualKeyboard.dll             
│  ├─ Qt5WebSockets.dll                  
│  ├─ Qt5Widgets.dll                     
│  ├─ QtCore.pyd                         
│  ├─ QtGui.pyd                          
│  ├─ QtNetwork.pyd                      
│  ├─ QtWidgets.pyd                      
│  └─ VCRUNTIME140_1.dll                 
├─ shiboken2                             
│  ├─ shiboken2.abi3.dll                 
│  ├─ shiboken2.pyd                      
│  └─ VCRUNTIME140_1.dll                 
├─ base_library.zip                      
├─ conf.json                             
├─ EsoDev.exe                            
├─ EsoDev.png                            
├─ libcrypto-1_1-x64.dll                 
├─ libssl-1_1-x64.dll                    
├─ MSVCP140.dll                          
├─ Pauser.exe                            
├─ python3.dll                           
├─ python37.dll                          
├─ select.pyd                            
├─ ucrtbase.dll                          
├─ unicodedata.pyd                       
├─ VCRUNTIME140.dll                      
├─ _bz2.pyd                              
├─ _ctypes.pyd                           
├─ _hashlib.pyd                          
├─ _lzma.pyd                             
├─ _socket.pyd                           
└─ _ssl.pyd                                                                     
```
5. Run EsoDev.exe in the `D:\test\dist\EsoDev\` folder, if it works correctly, then you're done!

That is EsoDev, have fun :D (If you have any bugs, questions or suggestions, **please** post an issue.)
