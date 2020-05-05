Quick Start Tool
================
If you are constantly creating new server instances, this tool may definitely make you life easier.
Its aim is to automate all actions taken at the very beginning of a new server instance creation.

First of all, make sure that ODKSM is installed and that you know how to configure a new instance.

Setup
^^^^^
Begin with choosing a folder that will be the root of all your server instances. Copy there both ``START.bat``
and ``bootstrap.ini``, that you can find in the ODKSM root folder.

You now need to edit ``bootstrap.ini`` and set the two fields in the ``[bootstrap]`` section:

- ``instances_root``: the directory in which the instances will be saved
- ``odksm_folder_path``: the root of ODKSM

.. note:: You can optionally set additional fields in ``bootstrap.ini``: these will be set as default values in newly
    created instances' ``config.ini``, so it makes sense to set them here only if they are global value for your
    server, like maybe ``arma_folder`` or ``password_admin``.

Finally, you need to edit ``START.bat`` and set the variable ``ODKSM_FOLDER_PATH`` to your ODKSM root.

.. note:: If you intend to keep the ``bootstrap.ini`` somewhere else than in the folder of ``START.bat`` you need to edit the
    latter and set the variable ``DEFAULT_CONFIG`` to the path of your ``bootstrap.ini``.

Usage
^^^^^
Simply launch the ``START.bat`` script. A console ui will ask for the instance name and whether to include
:doc:`templates <templates>`.

You are **not** done! The tool just created a new folder, where it put everything needed to start configuring the
server instance as explained in :ref:`usage:Create a server instance`.
