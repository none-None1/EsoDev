# -*- coding: utf-8 -*-
import os.path

################################################################################
## Form generated from reading UI file 'uigvaIRF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from extensions import extensions
from ui_about import Ui_MainWindow as mw
from ui_keyboard_shortcuts import Ui_MainWindow as sc
from subprocess import run, PIPE
import html, json
from extinstaller import install, uninstall


class Ui_MainWindow(object):
    fn = "Untitled"
    saved = True
    newfile = True
    opened = False  # Stop textChange event for a while when you open a file
    syntaxhighlight = True
    highlighted = False
    text = ""
    filext = []
    version = "1.0.0"

    @Slot()
    def save(self):
        if self.newfile:
            fn, _ = QFileDialog.getSaveFileName(
                self.MainWindow, "Choose a file name", filter=self.filext
            )
            if not fn:
                return False
            self.lang = self.recongnize_language(fn)
            while fn in self.recent:
                self.recent.remove(fn)
            self.fn = fn
            with open(fn, "w", encoding="utf-8") as f:
                f.write(self.code.toPlainText())
            while fn in self.recent:
                self.recent.remove(fn)
            self.recent.insert(0, fn)  # Insert at the front
        with open(self.fn, "w", encoding="utf-8") as f:
            f.write(self.code.toPlainText())
        self.saved = True
        self.newfile = False
        self.MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", self.fn + " - EsoDev", None)
        )
        return True

    @Slot()
    def saveas(self):
        fn, _ = QFileDialog.getSaveFileName(
            self.MainWindow, "Choose a file name", filter=self.filext
        )
        if not fn:
            return
        self.fn = fn
        self.lang = self.recongnize_language(fn)
        while fn in self.recent:
            self.recent.remove(fn)
        self.recent.insert(0, fn)
        with open(fn, "w", encoding="utf-8") as f:
            f.write(self.code.toPlainText())
        self.fn = fn
        self.MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", self.fn + " - EsoDev", None)
        )

    @Slot()
    def quit(self):
        if not self.saved:
            result = QMessageBox.question(
                self.MainWindow, "Confirm", "Your file is not saved, save your file?"
            )
            if result == QMessageBox.Yes:
                self.save()
        self.MainWindow.close()

    def quit_proxy(self, event):
        self.quit()
        event.accept()

    @Slot()
    def new(self):
        if (
            not self.saved
            and QMessageBox.question(
                self.MainWindow, "Confirm", "Your file is not saved, save your file?"
            )
            == QMessageBox.Yes
        ):
            self.save()
        self.fn = "Untitled.b"
        self.newfile = True
        self.code.clear()

    def recongnize_language(
        self, fn
    ):  # Automatically recognize the language through file extension
        ext = os.path.splitext(fn)[-1]
        for i, j in extensions.items():
            if ext in [k.replace("*", "") for k in j["filext"].split()]:
                return i
        return self.defaultlang

    @Slot()
    def open(self):
        fn, _ = QFileDialog.getOpenFileName(
            self.MainWindow, "Open a file", filter=self.filext
        )
        self.lang = self.recongnize_language(fn)
        if fn:
            if (
                not self.saved
                and QMessageBox.question(
                    self.MainWindow,
                    "Confirm",
                    "Your file is not saved, save your file?",
                )
                == QMessageBox.Yes
            ):
                self.save()
            self.opened = True
            self.newfile = False
            self.saved = True
            while fn in self.recent:
                self.recent.remove(fn)
            self.recent.insert(0, fn)
            with open(fn, "r", encoding="utf-8", errors="ignore") as f:
                self.text = f.read()
                self.code.setText(self.text)
            self.fn = fn
            self.MainWindow.setWindowTitle(
                QCoreApplication.translate("MainWindow", self.fn + " - EsoDev", None)
            )

    @Slot()
    def about(self):
        self.win = QMainWindow(self.MainWindow)
        ui = mw()
        ui.setupUi(self.win, self.version)
        self.win.show()

    @Slot()
    def shortcuts(self):
        self.win = QMainWindow(self.MainWindow)
        ui = sc()
        ui.setupUi(self.win)
        self.win.show()

    @Slot()
    def change(self):
        if not self.opened and not self.highlighted:
            self.MainWindow.setWindowTitle(
                QCoreApplication.translate("MainWindow", self.fn + "* - EsoDev", None)
            )
            self.saved = False
        self.opened = False
        if (
            not self.highlighted
            and self.syntaxhighlight
            and "syntaxhighlighter" in extensions[self.lang]
        ):
            self.text = self.code.toPlainText()
            self.highlighted = True
            highlighted = extensions[self.lang]["syntaxhighlighter"](self.text)
            hypertext = ""
            for i, j in highlighted:
                hypertext += (
                    f'<font color="{i}">'
                    + html.escape(j)
                    .replace("\n", "<br>")
                    .replace("\r", "<br>")
                    .replace("\t", "    ")
                    .replace(" ", "&nbsp;")
                    + "</font>"
                )
            cursor = QTextCursor(self.code.document())
            cursorpos = self.cursorpos
            self.code.setHtml(hypertext)
            cursor.setPosition(cursorpos)
            self.code.setTextCursor(cursor)
        self.highlighted = False
        return True

    @Slot()
    def cchange(self):
        cursor = self.code.textCursor()
        self.cursorpos = cursor.position()

    @Slot()
    def run(self):
        if not self.saved:
            result = QMessageBox.question(
                self.MainWindow, "Confirm", "Your file is not saved, save your file?"
            )
            if result == QMessageBox.Yes:
                self.save()
        if self.newfile:
            if not self.save():
                return
        run(
            'start "'
            + extensions[self.lang]["name"]
            + '" pauser.exe bin\\'
            + extensions[self.lang]["cmd"].replace("%1", self.fn),
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
        )

    @Slot()
    def language(self):
        self.dlg = QDialog(self.MainWindow)
        self.dlg.setWindowFlags(
            self.dlg.windowFlags() & ~Qt.WindowContextHelpButtonHint
        )
        self.dlg.setModal(True)
        self.dlg.setWindowTitle("Choose a language")
        self.dlg.resize(572, 356)
        self.choice = QComboBox(self.dlg)
        self.choice.setGeometry(QRect(120, 60, 271, 41))
        self.choice.addItems([i["name"] for i in extensions.values()])
        self.choice.setCurrentText(extensions[self.lang]["name"])
        self.okbtn = QPushButton(self.dlg)
        self.okbtn.setGeometry(QRect(130, 190, 100, 40))
        self.cancelbtn = QPushButton(self.dlg)
        self.cancelbtn.setGeometry(QRect(280, 190, 100, 40))
        self.cancelbtn.setText("Cancel")
        self.okbtn.setText("Ok")
        self.okbtn.clicked.connect(lambda: self.dlg.accept())
        self.cancelbtn.clicked.connect(lambda: self.dlg.reject())

        def func():
            self.lang = list(extensions.keys())[
                [i["name"] for i in extensions.values()].index(
                    self.choice.currentText()
                )
            ]

        self.dlg.accepted.connect(func)
        self.dlg.show()

    @Slot()
    def default_language(self):
        self.dlg = QDialog(self.MainWindow)
        self.dlg.setWindowFlags(
            self.dlg.windowFlags() & ~Qt.WindowContextHelpButtonHint
        )
        self.dlg.setModal(True)
        self.dlg.setWindowTitle("Configure default language")
        self.dlg.resize(572, 356)
        self.choice = QComboBox(self.dlg)
        self.choice.setGeometry(QRect(120, 60, 271, 41))
        self.choice.addItems([i["name"] for i in extensions.values()])
        self.choice.setCurrentText(extensions[self.lang]["name"])
        self.okbtn = QPushButton(self.dlg)
        self.okbtn.setGeometry(QRect(130, 190, 100, 40))
        self.cancelbtn = QPushButton(self.dlg)
        self.cancelbtn.setGeometry(QRect(280, 190, 100, 40))
        self.cancelbtn.setText("Cancel")
        self.okbtn.setText("Ok")
        self.okbtn.clicked.connect(lambda: self.dlg.accept())
        self.cancelbtn.clicked.connect(lambda: self.dlg.reject())

        def func():
            self.defaultlang = list(extensions.keys())[
                [i["name"] for i in extensions.values()].index(
                    self.choice.currentText()
                )
            ]

        self.dlg.accepted.connect(func)
        self.dlg.show()

    @Slot()
    def syntax_highlight(self):
        self.dlg = QDialog(self.MainWindow)
        self.dlg.setWindowFlags(
            self.dlg.windowFlags() & ~Qt.WindowContextHelpButtonHint
        )
        self.dlg.setModal(True)
        self.dlg.setWindowTitle("Configure syntax highlighting")
        self.dlg.resize(572, 356)
        self.choice = QCheckBox(self.dlg)
        self.choice.setText("Enable syntax\nhighlighting")
        self.choice.setCheckState(
            Qt.CheckState.Checked if self.syntaxhighlight else Qt.CheckState.Unchecked
        )
        self.choice.setGeometry(QRect(120, 60, 271, 90))
        self.okbtn = QPushButton(self.dlg)
        self.okbtn.setGeometry(QRect(130, 190, 100, 40))
        self.cancelbtn = QPushButton(self.dlg)
        self.cancelbtn.setGeometry(QRect(280, 190, 100, 40))
        self.cancelbtn.setText("Cancel")
        self.okbtn.setText("Ok")
        self.okbtn.clicked.connect(lambda: self.dlg.accept())
        self.cancelbtn.clicked.connect(lambda: self.dlg.reject())

        def func():
            self.syntaxhighlight = self.choice.isChecked()

        self.dlg.accepted.connect(func)
        self.dlg.show()

    @Slot()
    def uninstall(self):
        self.dlg = QDialog(self.MainWindow)
        self.dlg.setWindowFlags(
            self.dlg.windowFlags() & ~Qt.WindowContextHelpButtonHint
        )
        self.dlg.setModal(True)
        self.dlg.setWindowTitle("Uninstall an extension")
        self.dlg.resize(572, 356)
        self.choice = QComboBox(self.dlg)
        self.choice.setGeometry(QRect(120, 60, 271, 41))
        self.choice.addItems([i["name"] for i in extensions.values()])
        self.choice.setCurrentText(extensions[self.lang]["name"])
        self.okbtn = QPushButton(self.dlg)
        self.okbtn.setGeometry(QRect(130, 190, 100, 40))
        self.cancelbtn = QPushButton(self.dlg)
        self.cancelbtn.setGeometry(QRect(280, 190, 100, 40))
        self.cancelbtn.setText("Cancel")
        self.okbtn.setText("Ok")
        self.okbtn.clicked.connect(lambda: self.dlg.accept())
        self.cancelbtn.clicked.connect(lambda: self.dlg.reject())

        def func():
            to_be_uninstalled = list(extensions.keys())[
                [i["name"] for i in extensions.values()].index(
                    self.choice.currentText()
                )
            ]
            if (
                QMessageBox.question(
                    self.MainWindow,
                    "Confirm",
                    "Uninstallation of an extension has NO UNDO!\nAre you sure you still want to uninstall it?",
                )
                == QMessageBox.No
            ):
                return
            response = uninstall(to_be_uninstalled)
            if response == "Uninstallation was successful":
                QMessageBox.information(
                    self.MainWindow,
                    "Success",
                    f'Successfully uninstalled the extension "{self.choice.currentText()}", now please restart EsoDev to apply your changes',
                )
            else:
                QMessageBox.critical(self.MainWindow, "Error", response)

        self.dlg.accepted.connect(func)
        self.dlg.show()

    @Slot()
    def install(self):
        fn, _ = QFileDialog.getOpenFileName(
            self.MainWindow,
            "Choose an extension zip file to install",
            "",
            "Zip files (*.zip);;All files (*.*)",
        )
        response = install(fn, self.version)
        if isinstance(response, tuple):
            QMessageBox.information(
                self.MainWindow,
                "Success",
                f'Successfully installed the extension "{response[-1]}", now please restart EsoDev to apply your changes',
            )
        else:
            QMessageBox.critical(self.MainWindow, "Error", response)

    def create_opener(self, fn):
        def wrapper():
            self.lang = self.recongnize_language(fn)
            if fn:
                if (
                    not self.saved
                    and QMessageBox.question(
                        self.MainWindow,
                        "Confirm",
                        "Your file is not saved, save your file?",
                    )
                    == QMessageBox.Yes
                ):
                    self.save()
                self.opened = True
                self.newfile = False
                self.saved = True
                while fn in self.recent:
                    self.recent.remove(fn)
                self.recent.insert(0, fn)
                with open(fn, "r", encoding="utf-8", errors="ignore") as f:
                    self.text = f.read()
                    self.code.setText(self.text)
                self.fn = fn
                self.MainWindow.setWindowTitle(
                    QCoreApplication.translate(
                        "MainWindow", self.fn + " - EsoDev", None
                    )
                )

        return wrapper

    def update_recent(self):
        for i in self.recent:
            if os.path.exists(i):
                a = QAction(self.MainWindow)
                a.triggered.connect(self.create_opener(i))
                a.setText(i)
                self.menuRecent.addAction(a)

    @Slot()
    def clear(self):
        self.recent = []
        QMessageBox.information(
            self.MainWindow,
            "Clear success",
            "Successfully cleared the history, now please restart EsoDev to save your changes",
        )

    @Slot()
    def reset(self):
        if (
            QMessageBox.question(
                self.MainWindow,
                "Confirm",
                "Resetting EsoDev will remove all your extensions, your history and reset all options!\nAre you sure you still want to reset?",
            )
            == QMessageBox.No
        ):
            return
        for i in extensions.keys():
            uninstall(i)  # Delete extensions
        self.syntaxhighlight = True
        self.defaultlang = "brainfuck"
        self.recent = []
        QMessageBox.information(
            self.MainWindow, "Reset success", "Reset was successful, press OK to quit."
        )
        self.MainWindow.close()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon("EsoDev.png"))
        MainWindow.resize(934, 790)
        MainWindow.setWindowFlags(
            MainWindow.windowFlags() & ~Qt.WindowMaximizeButtonHint
        )
        self.MainWindow = MainWindow
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionSelect_All = QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionRun = QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionLanguage = QAction(MainWindow)
        self.actionLanguage.setObjectName("actionLanguage")
        self.actionDefault_Language = QAction(MainWindow)
        self.actionDefault_Language.setObjectName("actionDefault_Language")
        self.actionSyntax_Highlighting = QAction(MainWindow)
        self.actionSyntax_Highlighting.setObjectName("actionSyntax_Highlighting")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionKeyboard_Shortcuts = QAction(MainWindow)
        self.actionKeyboard_Shortcuts.setObjectName("actionKeyboard_Shortcuts")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionInstall = QAction(MainWindow)
        self.actionInstall.setObjectName("actionInstall")
        self.actionUninstall = QAction(MainWindow)
        self.actionUninstall.setObjectName("actionUninstall")
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionReset = QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.code = QTextEdit(self.centralwidget)
        self.code.setObjectName("code")
        self.code.setGeometry(QRect(0, 0, 931, 741))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 934, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuExecution = QMenu(self.menubar)
        self.menuExecution.setObjectName("menuExecution")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuExtensions = QMenu(self.menubar)
        self.menuExtensions.setObjectName("menuExtensions")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuRecent = QMenu(self.menuFile)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuExecution.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuExtensions.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.menuRecent.menuAction())
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuExecution.addAction(self.actionRun)
        self.menuOptions.addAction(self.actionLanguage)
        self.menuOptions.addAction(self.actionDefault_Language)
        self.menuOptions.addAction(self.actionSyntax_Highlighting)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionReset)
        self.menuExtensions.addAction(self.actionInstall)
        self.menuExtensions.addAction(self.actionUninstall)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionKeyboard_Shortcuts)
        # Load config
        with open("conf.json", "r") as f:
            conf = json.load(f)
        self.syntaxhighlight = conf["SyntaxHighlighting"]
        self.lang = conf["DefaultLang"]
        self.defaultlang = self.lang
        for i, j in extensions.items():
            if i == self.defaultlang:
                self.filext.insert(
                    0, f"{j['name']} ({j['filext']})"
                )  # If the language is chosen to be the default by the user, then put it in the top of the list
            else:
                self.filext.append(f"{j['name']} ({j['filext']})")
        self.recent = conf["recent"]
        self.filext.append("All files (*.*)")
        self.filext = ";;".join(self.filext)
        # File
        self.retranslateUi(MainWindow)
        self.actionSave.triggered.connect(self.save)
        self.actionSave_As.triggered.connect(self.saveas)
        self.actionExit.triggered.connect(self.quit)
        self.actionNew.triggered.connect(self.new)
        self.actionOpen.triggered.connect(self.open)
        self.actionClear.triggered.connect(self.clear)
        self.MainWindow.closeEvent = self.quit_proxy
        save = QShortcut(QKeySequence("Ctrl+S"), MainWindow)
        save.activated.connect(self.save)
        saveas = QShortcut(QKeySequence("Ctrl+Shift+S"), MainWindow)
        saveas.activated.connect(self.saveas)
        new = QShortcut(QKeySequence("Ctrl+N"), MainWindow)
        new.activated.connect(self.new)
        op = QShortcut(QKeySequence("Ctrl+O"), MainWindow)
        op.activated.connect(self.open)
        quit = QShortcut(QKeySequence("Ctrl+Q"), MainWindow)
        quit.activated.connect(self.quit)
        quit = QShortcut(QKeySequence("Ctrl+R"), MainWindow)
        quit.activated.connect(self.run)
        self.code.textChanged.connect(self.change)
        self.code.cursorPositionChanged.connect(self.cchange)
        # Edit
        self.actionCopy.triggered.connect(self.code.copy)
        self.actionPaste.triggered.connect(self.code.paste)
        self.actionUndo.triggered.connect(self.code.undo)
        self.actionRedo.triggered.connect(self.code.redo)
        self.actionCut.triggered.connect(self.code.cut)
        self.actionSelect_All.triggered.connect(self.code.selectAll)
        # Execution
        self.actionRun.triggered.connect(self.run)
        # Options
        self.actionLanguage.triggered.connect(self.language)
        self.actionDefault_Language.triggered.connect(self.default_language)
        self.actionSyntax_Highlighting.triggered.connect(self.syntax_highlight)
        self.actionReset.triggered.connect(self.reset)
        # Extensions
        self.actionInstall.triggered.connect(self.install)
        self.actionUninstall.triggered.connect(self.uninstall)
        # Help
        self.actionAbout.triggered.connect(self.about)
        self.actionKeyboard_Shortcuts.triggered.connect(self.shortcuts)
        cursor = self.code.textCursor()
        self.cursorpos = cursor.position()
        QMetaObject.connectSlotsByName(MainWindow)
        self.update_recent()

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", self.fn + " - EsoDev", None)
        )
        # if QT_CONFIG(statustip)
        MainWindow.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.actionNew.setText(QCoreApplication.translate("MainWindow", "New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", "Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", "Save", None))
        self.actionSave_As.setText(
            QCoreApplication.translate("MainWindow", "Save As", None)
        )
        self.menuRecent.setTitle("Recent files")
        self.actionClear.setText("Clear history")
        self.actionExit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", "Copy", None))
        self.actionPaste.setText(
            QCoreApplication.translate("MainWindow", "Paste", None)
        )
        self.actionCut.setText(QCoreApplication.translate("MainWindow", "Cut", None))
        self.actionSelect_All.setText(
            QCoreApplication.translate("MainWindow", "Select All", None)
        )
        self.actionRun.setText(QCoreApplication.translate("MainWindow", "Run", None))
        self.actionLanguage.setText(
            QCoreApplication.translate("MainWindow", "Language", None)
        )
        self.actionDefault_Language.setText(
            QCoreApplication.translate("MainWindow", "Default Language", None)
        )
        self.actionSyntax_Highlighting.setText(
            QCoreApplication.translate("MainWindow", "Syntax Highlighting", None)
        )
        self.actionAbout.setText(
            QCoreApplication.translate("MainWindow", "About", None)
        )
        self.actionKeyboard_Shortcuts.setText(
            QCoreApplication.translate("MainWindow", "Keyboard Shortcuts", None)
        )
        self.actionReset.setText(
            QCoreApplication.translate("MainWindow", "Reset and quit", None)
        )
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", "Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", "Redo", None))
        self.actionInstall.setText(
            QCoreApplication.translate("MainWindow", "Install", None)
        )
        self.actionUninstall.setText(
            QCoreApplication.translate("MainWindow", "Uninstall", None)
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", "Edit", None))
        self.menuExecution.setTitle(
            QCoreApplication.translate("MainWindow", "Execution", None)
        )
        self.menuOptions.setTitle(
            QCoreApplication.translate("MainWindow", "Options", None)
        )
        self.menuExtensions.setTitle(
            QCoreApplication.translate("MainWindow", "Extensions", None)
        )
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))

    # retranslateUi
