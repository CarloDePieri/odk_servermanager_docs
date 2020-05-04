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

You can then keep it updated by running, in the ``odksm`` directory:

.. code:: console

    $ git fetch
    $ git pull

This will keep you on the stable ``master`` branch, while active development happens on ``testing``.


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

Verify the installation
^^^^^^^^^^^^^^^^^^^^^^^
You can verify that ODKSM is working as intended and all dependencies are met by running its test suite with:

.. code:: console

    $ pipenv run pytest tests/

All tests should pass! You are now ready to :doc:`create your first Instance <usage>`.