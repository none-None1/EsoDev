"""
Extension loader
"""
import os, json, runpy

with open(
    os.path.join(os.path.dirname(__file__), "list.json"), "r", encoding="utf-8"
) as f:
    xts = json.load(f)
extensions = {}
for i in xts:
    try:
        extensions[i] = runpy.run_path(
            os.path.join(os.path.dirname(__file__), i + ".py")
        )  # Load the extension and return its namespace
    except:
        extensions[i] = runpy.run_path(
            os.path.join(os.path.dirname(__file__), i + ".pyc")
        )  # Load the extension and return its namespace
