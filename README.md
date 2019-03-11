# pycharm-debug-module-subprocess

1. tox -rve py37 to generate interpreter with package
2. debug test.py -> 

```bash
/Users/bernat/git/github/pycharm-debug-module-subprocess/.tox/py37/bin/python "/Users/bernat/Library/Application Support/JetBrains/Toolbox/apps/PyCharm-P/ch-0/191.5849.23/PyCharm 2019.1 EAP.app/Contents/helpers/pydev/pydevd.py" --multiproc --qt-support=auto --client 127.0.0.1 --port 58714 --file /Users/bgabor8/git/github/pycharm-debug-module-subprocess/test.py
pydev debugger: process 15930 is connecting

Connected to pydev debugger (build 191.5849.23)
pydev debugger: process 15931 is connecting

pydev debugger: process 15932 is connecting

No module named /Users/bgabor8/git/github/pycharm-debug-module-subprocess/pug/helper.py
b''

Process finished with exit code 0
```

