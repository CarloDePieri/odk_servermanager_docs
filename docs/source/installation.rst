Installation
============
Prerequisites
^^^^^^^^^^^^^
The tool is currently compatible with Windows only (linux support is on its way).

You will need Python 3.8 installed on your machine. You can install it via
choco_ or via the `official package`_.

Download
^^^^^^^^
The quickest way to get this tool is to download the `latest release`_ from github.
Simply download the zip and extract it.

Alternatively, if you prefer to more easily keep the tool updated, you may use git_ directly.
Once installed, run:

.. code:: console

    $ git clone https://github.com/CarloDePieri/odk_servermanager.git odksm

.. _choco: https://chocolatey.org/packages/python/3.8.2
.. _official package: https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe
.. _latest release: https://github.com/CarloDePieri/odk_servermanager/releases/latest
.. _git: https://git-scm.com/download/win

Install
^^^^^^^
Usage of a `python virtual environment`_ is strongly encouraged: install pipenv and prepare the venv by issuing these
commands inside the ODKSM root directory:

.. code:: console

    $ pip install pipenv
    $ python -m venv .venv

When the venv is ready, install ODKSM and its dependencies inside the venv with:

.. code:: console

    $ pipenv install --dev

.. _python virtual environment: https://docs.python.org/3/tutorial/venv.html

Update
^^^^^^
If you used the zipped release, you will need to download the latest release and replace the content of the whole tool
installation with the new one.

.. note:: Do not simply overwrite the folder. Delete the old one and replace it with the new one. This will make sure no
    old files are left lingering.

If you used git instead, you can keep the tool updated by running in its root directory:

.. code:: console

    $ git fetch
    $ git pull

This will keep you on the stable ``master`` branch, while active development happens on ``testing``.

.. note:: You will need to have a pristine tool installation to update it this way. If you changed something there, backup
    any important changes, run ``git reset --hard HEAD`` to reset the tool to its original state, then update it!

.. important:: Remember that, independently from the update method, any ``ODKSM.bat`` or ``START.bat`` you copied around will need to be manually updated to
    the current version, if they have changed.

Verify the installation
^^^^^^^^^^^^^^^^^^^^^^^
You can verify that ODKSM is working as intended and all dependencies are met by running its test suite with:

.. code:: console

    $ pipenv run pytest tests/

All tests should pass! You are now ready to :doc:`create your first Instance <usage>`.