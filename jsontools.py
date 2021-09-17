import json
import os

def dumpJSON(path, val, indent=2):
    dirpath = os.path.dirname(path)
    if(dirpath == "" or os.path.isdir(dirpath)):
        with open(path, 'w') as f:
            json.dump(val, f, indent=indent)
        return True
    else:
        return False

def loadJSON(path):
    if(os.path.isfile(path)):
        with open(path, "r") as f:
            val = json.load(f)
        return val
    else:
        return {}