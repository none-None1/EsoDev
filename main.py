import os, PySide2, json
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, "plugins", "platforms")
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path
os.environ["QT_SCALE_FACTOR"] = "2"
from ui_ui import *
import sys, platform
os.chdir(os.path.dirname(sys.argv[0])) # To safely read and write
app = QApplication(sys.argv)
if platform.system() != "Windows":
    QMessageBox.critical(None, "Error", "Invalid platform, please run in Windows")
    sys.exit(1)
win = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(win)
win.show()
app.exec_()
with open("conf.json", "w") as f:  # Store JSON file after program terminates
    json.dump(
        {"DefaultLang": ui.defaultlang, "SyntaxHighlighting": ui.syntaxhighlight,'recent': ui.recent}, f
    )
