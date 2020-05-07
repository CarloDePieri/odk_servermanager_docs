Files Templates
===============

ODKSM compiles the Arma config file and the server startup script starting from templates that can be found in
``odk_servermanager\templates``.

These files nicely cover OUR use case but at some point you will probably need different parameters and generally more
control over the configs.

Custom templates
^^^^^^^^^^^^^^^^
To enable the use of a custom template you need to make a copy of the template file and fill in a field in your server
instance ``config.ini``.

ServerConfig.cfg
    Make a copy of ``server_cfg_template.txt``. Fill in the field :option:`config_template <config config_template>`.

run_server.bat
    Make a copy of ``run_server_template.txt``. Fill in the fields :option:`bat_template <bat bat_template>`.

.. warning:: Do not edit templates file directly in the tool folder! Make a copy and link that in your ``config.ini``.

Your new templates files are now going to be used by the tool. Every edit you do there will be carried over the generated
files when creating or updating your server instance.

.. important:: You can modify these templates to your heart's content but do not delete statement like ``{{ hostname }}``
    or ``{{ password }}``. These token are used by the template framework to fill in fields values set in the ``config.ini``
    and they are required. You can move them around though.

Custom template fields
^^^^^^^^^^^^^^^^^^^^^^
It's possible to fill in custom templates directly from the ``config.ini`` file.

Suppose you needed to change the ``maxPlayers`` Arma config file field. Sure, you can change it directly in the template.
But you can leverage the template framework and edit the template file with a line like this:

.. code-block::

    maxPlayers = {{ max_players }};

Now you need to add a new field with the same name in your ``config.ini``, right in the ``[config]`` section. Like this:

.. code-block::

    [config]
    max_players = 40

When the tool is run, the value of the ``max_players`` field in the ``config.ini`` will replace the whole
``{{ max_players }}`` in your template file like this:

.. code-block::

    maxPlayers = 40;
