from zipfile import ZipFile
import json, ctypes, os


def install(extpath, esodev_version):
    """Safely install an extension"""
    try:
        zip = ZipFile(extpath)
    except:
        return "Unsupported zip file format, maybe the file is corrupted"
    files = zip.namelist()
    if "entry.json" not in files:
        return 'Cannot find entry file "entry.json"'
    try:
        with zip.open("entry.json", "r") as f:
            entry = json.load(f)
        version = entry["esodev-version"] if ("esodev-version" in entry) else "1.0.0"
        bitwidth = entry["bitwidth"] if ("esodev-version" in entry) else "32bit"
        if "module" not in entry:
            return 'entry file does not contain the key "module"'
        module = entry["module"]
        binaries = entry["binaries"] if ("binaries" in entry) else []
        directories = entry['directorys'] if ('directories' in entry) else []
        if list(map(int, version.split("."))) > list(
            map(int, esodev_version.split("."))
        ):
            return f"The extension requires EsoDev>={version}, but you have EsoDev {esodev_version}"  # Version compatibility
        try:
            ctypes.windll.kernel32.GetSystemWow64DirectoryW
        except:
            if bitwidth == "64bit":
                return "The extension requires a 64-bit system"  # Bitwidth
        if module + ".py" not in files:
            return f"Could not find {module}.py"
        if os.path.exists(f"extensions\\{module}.py"):
            return f"The extension is already installed, or there is an extension with the same module name"
        if module == "list":
            return 'It is not allowed to install a module with the name "list"'
        zip.extract(module + ".py", f"extensions")
        for i in directories:
            try:
                os.mkdir(i)
            except:
                return f"Could not create directory {i}"
        for i in binaries:
            try:
                zip.extract(i, f"bin")
            except:
                return f"Could not find {i}"
        with open("extensions\\list.json", "r", encoding="utf-8") as f:
            extensions = json.load(f)
        extensions.append(module)
        with open("extensions\\list.json", "w", encoding="utf-8") as f:
            json.dump(extensions, f)
        with open(f"extensions\\{module}.json", "w", encoding="utf-8") as f:
            json.dump(binaries+directories, f)
    except BaseException as e:
        return "Internal error: " + str(e)
    return ("Installation was successful", module)


def uninstall(extname):
    """Safely uninstall an extension"""
    try:
        with open("extensions\\list.json", "r", encoding="utf-8") as f:
            extensions = json.load(f)
        if extname not in extensions or not os.path.exists(
            f"extensions\\{extname}.json"
        ):
            return f"Extension does not exist, or is a built-in extension"
        extensions.remove(extname)
        with open("extensions\\list.json", "w", encoding="utf-8") as f:
            json.dump(extensions, f)
        os.remove(f"extensions\\{extname}.py")
        with open(f"extensions\\{extname}.json", "r", encoding="utf-8") as f:
            binaries = json.load(f)
        files=[]
        dirs=[]
        for i in binaries:
            if os.path.isfile(os.path.join("bin", i)):
                files.append(os.path.join("bin", i))
            else:
                dirs.append(os.path.join("bin",i))
        for i in files:
            os.remove(i)
        dirs.reverse()
        for i in dirs:
            os.rmdir(i)
        os.remove(f"extensions\\{extname}.json")
        return "Uninstallation was successful"
    except BaseException as e:
        return "Internal error: " + str(e)
