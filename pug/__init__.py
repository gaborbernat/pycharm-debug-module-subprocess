import sys
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))

HELPER = os.path.join(HERE, "helper.py")


def run():
    print(subprocess.check_output([sys.executable, HELPER]))
