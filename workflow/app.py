#!/usr/bin/python3

import subprocess
import json
import sys
import os.path


def captureShell(command):
    return subprocess.run(command, shell=True, text=True,
                          capture_output=True).stdout.split('\n')[0:-1]


def ghqList():
    ghqRoot = captureShell('/usr/local/bin/ghq root')[0]
    fullPath = captureShell(
        '/usr/bin/find {} -type d -maxdepth 3 -depth 3'.format(ghqRoot))
    keys = list(map(lambda path: os.path.basename(path), fullPath))
    return zip(keys, fullPath)


def alfred(items):
    print(json.dumps({"items": items}))


def getIcon(mode):
    if mode == 'vscode':
        return {
            "type": "fileicon",
            "path": "/Applications/Visual Studio Code.app"
        }
    elif mode == 'iterm':
        return {"type": "fileicon", "path": "/Applications/iTerm.app"}
    elif mode == 'fork':
        return {"type": "fileicon", "path": "/Applications/Fork.app"}
    elif mode == 'finder':
        return {
            "type": "fileicon",
            "path": "/System/Library/CoreServices/Finder.app"
        }


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
