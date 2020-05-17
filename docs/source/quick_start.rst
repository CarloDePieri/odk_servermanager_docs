Quick Start Tool
================
This tool aims to automate all actions taken at the very beginning of a new server instance creation.

First of all, make sure that ODKSM is installed and that you know how to configure a new instance.

Setup
^^^^^
Begin with choosing a folder that will be the root of all server instances. Copy there both ``START.bat``
and ``bootstrap.ini``, that can be found in the ODKSM root folder.

Now edit ``bootstrap.ini`` and set the two fields in the ``[bootstrap]`` section:

- :option:`instances_root <bootstrap instances_root>`: the directory in which the instances will be saved
- :option:`odksm_folder_path <bootstrap odksm_folder_path>`: the root of ODKSM

.. note:: Additional fields can be set in ``bootstrap.ini``: these will be default values in newly
    created instances' ``config.ini``, so it makes sense to set them here only if they are global values for the whole
    server, like maybe :option:`arma_folder <ODKSM arma_folder>` or :option:`password_admin <config password_admin>`.

Finally, edit ``START.bat`` and set the variable ``ODKSM_FOLDER_PATH`` to your ODKSM root.

.. note:: When keeping ``bootstrap.ini`` and ``START.bat`` in different folders, edit the
    latter and set the variable ``DEFAULT_CONFIG`` to the path of ``bootstrap.ini``.

Usage
^^^^^
Simply launch the ``START.bat`` script. A console ui will ask for the instance name and whether to include
:doc:`templates <templates>`.

You are **not** done! The tool just created a new folder, where it put everything needed to start configuring the
server instance as explained in :ref:`usage:Create a server instance`.
