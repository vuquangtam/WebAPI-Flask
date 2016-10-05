import os

def cmd(command):
    return os.popen(command).read()