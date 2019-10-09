#!/usr/bin/env python3

import subprocess
import json
import sys


def captureShell(command):
    return subprocess.run(
        command, shell=True, text=True, capture_output=True).stdout.split('\n')[0:-1]


def ghqList():
    fullPath = captureShell('/usr/local/bin/ghq list -p')
    keys = captureShell('/usr/local/bin/ghq list --unique')
    return zip(keys, fullPath)


def alfred(items):
    print(json.dumps({"items": items}))


def getIcon(mode):
    if mode == 'vscode':
        return {"type": "fileicon", "path": "/Applications/Visual Studio Code.app"}
    elif mode == 'iterm':
        return {"type": "fileicon", "path": "/Applications/iTerm.app"}


if __name__ == '__main__':
    argv = sys.argv[1:]
    mode = argv[0]

    icon = getIcon(mode)

    items = [{
        "type": "file",
        "title": key,
        "subtitle": value,
        "arg": value,
        "icon": icon
    } for key, value in ghqList()]

    alfred(items)
