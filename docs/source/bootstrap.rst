bootstrap.ini
=============

In here fields present in the ``bootstrap.ini`` configuration file are described.

bootstrap section
~~~~~~~~~~~~~~~~~
This section contains settings used by the quick start tool.

.. program:: bootstrap

.. option:: instances_root

    The absolute path to the folder in which the tool will create the new instance root folder.

    :Required: yes
    :Type: string
    :Default: ``""``

.. option:: odksm_folder_path

    The absolute path to the folder containing the odksm ``run.py``.

    :Required: yes
    :Type: string
    :Default: ``""``

config, bat, ODKSM, mod_fix_settings sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All values in these section will be the default one present in the ``config.ini`` of a new instance. They are described
in :doc:`the config.ini documentation<config>`.

.. warning:: Do not delete empty sections' titles from this file!
