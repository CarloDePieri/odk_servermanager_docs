Installation
============
Prerequisites
^^^^^^^^^^^^^
The tool is currently compatible with Windows only (linux support is on its way).

The main requirement is Python 3.8 which can be installed via choco_ or the `official package`_.

Download
^^^^^^^^
The quickest way to get the tool is to download the `latest release`_ from github and extract the zipped file.

Alternatively, git_ can be used directly. This solution permits to more easily keep the tool updated.
Once git is installed, run:

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
If the tool has been installed from the zipped release, the latest one must be downloaded and the extracted files must
replace the old ones.

.. note:: Do not simply overwrite the tool installation folder. Delete the old one and replace it with the new one. This
    will make sure no old files are left lingering.

If git has been used instead, it can be used to keep the tool updated by running in its root directory:

.. code:: console

    $ git fetch
    $ git pull

This will keep the tool on the stable ``master`` branch, while active development happens on ``testing``.

.. note:: The installation directory must be *clean* to update it this way. If something has been changed there, backup
    any important changes, run ``git reset --hard HEAD`` to reset the tool to its original state, then update it!

.. important:: Independently from the update method, any ``ODKSM.bat`` or ``START.bat`` that has been copied
    around will need to be manually updated to the current version, if they have changed with the newest release.

Verify the installation
^^^^^^^^^^^^^^^^^^^^^^^
To verify that ODKSM is working as intended and all dependencies are met run its test suite with:

.. code:: console

    $ pipenv run pytest tests/

All tests should pass! You are now ready to :doc:`create your first Instance <usage>`.