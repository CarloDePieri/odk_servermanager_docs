Mod Specific Behavior
=====================

ODKSM modular architecture makes it easy to implement mod specific behaviour, like paste your custom configuration file
in the right folder after a mod has been installed or fetch a unusually placed mod's key. This is done through ModFixes,
plug&play python modules.

Usage
^^^^^
Enabling a ModFix is easy enough: you just need to put its name in the list value of
:option:`enabled_fixes <mod_fix_settings enabled_fixes>`.

.. note:: The *name* of a ModFix is the name of its file (without the ``.py`` extension), which can be found inside
    the ``odk_servermanager\modfix`` folder (here it is, on github_).

At this point, depending on the modfix, you may need to add additional fields and relative values to the
``mod_fix_settings``.

.. _github: https://github.com/CarloDePieri/odk_servermanager/tree/master/odk_servermanager/modfix

Linked vs copied
^^^^^^^^^^^^^^^^
Take a moment to notice the difference between linked and copied mods.

Usually, mods without a modfix get simply linked inside the :option:`linked_mod_folder_name <ODKSM linked_mod_folder_name>`
folder. Folders inside this linked mod folder are *symlink*, which means that files inside those folders are the original
mods files: these files are managed directly by Steam and should never be touched by you or a modfix. This is the same behavior
of ``!Workshop``, inside the main Arma 3 installation folder.

When a change is needed inside a mod's folder, the modfix should **copy** the mod's files inside the
:option:`copied_mod_folder_name <ODKSM copied_mod_folder_name>` folder. Files inside this folders are safe to edit and
server instance specific.

.. note:: You can force this behavior putting a mod's name inside the :option:`mods_to_be_copied <ODKSM mods_to_be_copied>`.

.. warning:: When copying mods, the modfix should also take care of updating said mod's copy inside an instance when
    needed. Depending on the specific mod structure and/or on the ModFix the tool behavior when updating a copied mod could
    change. Be sure to backup any important file you changed inside the copied mod folder before updating its instance
    the first time, just in case.

Implement your own ModFix
^^^^^^^^^^^^^^^^^^^^^^^^^
It's relatively easy to implement your own ModFix. You can find some example inside the modfix folder.

#. First of all create a new python file inside the ``odk_servermanager\modfix`` folder. The file name will be the name
   of the ModFix you need to add to the :option:`enabled_fixes <mod_fix_settings enabled_fixes>`. For example:
   ``my_modfix.py``.

#. Inside that file, extend the ``odk_servermanager.modfix.modfix.ModFix`` class. For example:

   .. code-block:: python

    class MyModFix(ModFix):
        """This is my wonderfull modfix"""

        name = "my_mod"  # Apply this ModFix to the mod 'my_mod'

   The ``name`` class field is required: by default the modfix will use that field to check if a modfix is to be applied
   to a specific mod. In this case, if the mod called ``my_mod`` is to be loaded (and the ``my_modfix`` is enabled!) this
   ModFix will be triggered. If you want to modify the mechanism used to pair ModFix to mod, you may override the
   ``ModFix.does_apply_to_mod()`` method to do so. You may also need to override ``ModFix.update_mods_to_be_copied_list()``
   which takes care of automatically adding mods name to the :option:`mods_to_be_copied <ODKSM mods_to_be_copied>` list
   when needed.

#. In your ModFix module namespace (after and outside your newly created class) save an object of your ModFix in a variable
   called ``to_be_registered``:

   .. code-block:: python

    to_be_registered = MyModFix()

   This is required to the ModFix loading mechanism.

#. Your ModFix will load now but is currently doing nothing. Enter **ModFix hooks**. These are ModFix methods that your
   class inherited and that by default are set to ``None``. Override the hook (or hooks!) that best cover your needs and
   implement there your mod specific behavior. More information on hooks can be found in the next section.

   .. important:: Remember that you need to implement behaviors both for the instance *init* and *update* *stages*. More on
    this later!

#. It's a good idea to implement a proper test suite for your ModFix. Tests goes into the ``tests\modfixes`` folder,
   where you can also find several test examples.

ModFixes' Hooks
^^^^^^^^^^^^^^^
Here an example of a hook:

.. code-block:: python

    def hook_init_copy_replace(self, server_instance: ServerInstance, call_data: List[str]) -> None:
        """This is a hook that REPLACE the default COPY mod behavior during this instance INIT stage."""
        # do very complicated stuff here

Let's start by going over its arguments:

server_instance: ServerInstance
    This is the object representing the current server instance. It's an instance of the
    ``odk_servermanager.instance.ServerInstance`` class. You can use this to modify or to obtain information about the
    current server instance. Of particular interest is the ``server_instance.S`` object, which is a
    ``odk_servermanager.settings.ServerInstanceSettings`` instance, containing all settings currently valid for this server instance.

call_data: List[str]
    This is seldomly needed. It's a list containing, in order, the current *stage*, the current *operation*, and the Mod name.

There are currently 12 hooks you can override. Their name is a combination of three elements:

hook_[stage]_[operation]_[time]
    :stage: init, update
    :operation: copy, link
    :time: pre, post, replace

.. object:: stage: init

    All hooks in this *stage* get triggered when first creating the server instance.

.. object:: stage: update

    All hooks in this *stage* get triggered when the server instance folder is already present and the tool is activated.

.. object:: operation: copy

    These hooks activate when the mod is copied.

.. object:: operation: link

    These hooks activate when the mod is symlinked.

.. object:: time: pre

    These hooks activate before its designed *operation*. The default *operation* still takes place.

.. object:: time: post

    These hooks activate after its designed *operation*. The default *operation* still takes place.

.. object:: time: replace

    These hooks replace the default *operation*. Pre and Post hooks can still be called around these hooks.

.. hint:: If you need a replace hook to do nothing (for example to prevent a copy update) you still need to override
    the hook ``hook_update_copy_replace``. Just have it do nothing with a ``pass`` instruction like this:

    .. code-block:: python

        def hook_update_copy_replace(server_instance, call_data):
            pass
