Template Files
==============

ODKSM compiles the Arma config file and the server startup script starting from templates that can be found in
``odk_servermanager\templates``.

These files nicely cover ODK Clan's use case, but at some point different parameters and generally more
control over the configs will probably be needed.

Custom templates
^^^^^^^^^^^^^^^^
To enable the use of custom templates make a copy of the template files in the instance's folder and fill in the related
fields in the instance's ``config.ini``.

ServerConfig.cfg
    Make a copy of ``server_cfg_template.txt``. Fill in the field :option:`config_template <config config_template>`.

run_server.bat
    Make a copy of ``run_server_template.txt``. Fill in the field :option:`bat_template <bat bat_template>`.

.. warning:: **DO NOT** edit template files directly in the tool folder! Make a copies and link those in the ``config.ini``.

The new template files are now going to be used by the tool. Every edit will be carried over to the generated
files when creating or updating server instances.

.. important:: These templates can be modified to heart's content but don't delete statements like ``{{ hostname }}``
    or ``{{ password }}``. These tokens are used by the template framework to fill in fields values set in the ``config.ini``
    and they are required. You can move them around though.

Custom templates fields
^^^^^^^^^^^^^^^^^^^^^^^
It's possible to fill in custom templates directly from the ``config.ini`` file.

Suppose a tweak to the ``maxPlayers`` Arma settings is needed often. Sure, it can be changed directly in the
template. But it's also possible to leverage the template framework and edit the template file with a line like this:

.. code-block::

    maxPlayers = {{ max_players }};

Now add a new field with the same name in the ``config.ini``, right in the ``[config]`` section. Like this:

.. code-block::

    [config]
    max_players = 40

When the tool is run, the value of the ``max_players`` field in the ``config.ini`` will replace the whole
``{{ max_players }}`` token in the template file, resulting in this:

.. code-block::

    maxPlayers = 40;
