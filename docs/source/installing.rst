Installing
==========
Prerequisites
^^^^^^^^^^^^^
The tool is currently compatible with Windows only (linux support is on its way).

You will need Python 3.8 installed on your machine. You can install it via
[choco](https://chocolatey.org/packages/python/3.8.2) or via the [official package](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe).

## Download
The quickest way to get this tool is to download the [latest release](https://github.com/CarloDePieri/odk_servermanager/releases/latest) from github.
Simply download the zip and extract it.

Alternatively, if you prefer to more easily keep the tool updated, you may use [git](https://git-scm.com/download/win) directly.
Once installed, run:
```
$ git clone https://github.com/CarloDePieri/odk_servermanager.git odksm
```
You can then keep it updated by running, in the `odksm` directory:
```
$ git fetch
$ git pull
```
This will keep you on the stable `master` branch (while development happens on `testing`).

Install
^^^^^^^
Usage of a python virtual environment is strongly encouraged: install pipenv and prepare the venv by issuing these
commands inside the ODKSM root directory:
```
$ pip install pipenv
$ python -m venv .venv
```
When the venv is ready, install ODKSM and its dependencies inside the venv with:
```
$ pipenv install --dev
```

Verify the installation
^^^^^^^^^^^^^^^^^^^^^^^
You can verify that ODKSM is working as intended and all dependencies are met by running its test suite with:
```
$ pipenv run pytest tests/
```
All tests should pass! You are now ready to [create your first Instance](https://github.com/CarloDePieri/odk_servermanager/wiki/Usage).
