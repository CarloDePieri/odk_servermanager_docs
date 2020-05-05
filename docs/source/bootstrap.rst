bootstrap.ini
=============

In here fields present in the ``bootstrap.ini`` are described.

bootstrap
~~~~~~~~~

instances_root
    :required: yes
    :type: string
    :default: ``""``

    the absolute path to the folder in which the tool will create the new instance root folder

odksm_folder_path
    :required: yes
    :type: string
    :default: ``""``

    the absolute path to the folder containing the odksm run.py


config, bat, ODKSM, mod_fix_settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All values in these section will be the default one present in the ``config.ini`` of a new instance. They are described
in :doc:`the config.ini documentation<config>`

.. warning:: Do not delete empty sections' titles from this file!
