Mod Specific Behavior
=====================

ODKSM modular architecture makes it easy to implement mod specific behaviour, like pasting a custom configuration file
in the right folder after a mod has been installed or fetch an unusually placed mod's key. This is done through
ModFixes, plug&play python modules.

Usage
^^^^^
Enabling a ModFix is easy enough: just put its name in the list value of
:option:`enabled_fixes <mod_fix_settings enabled_fixes>`.

.. note:: The *name* of a ModFix is the name of its module file (without the ``.py`` extension), which can be found
    inside the ``odk_servermanager\modfix`` folder (here it is, on github_).

At this point, depending on the modfix, additional fields and their relative values may be needed inside the
``mod_fix_settings`` section. In :doc:`this page <modfix_doc>` currently implemented modfix are thoroughly documented.

.. _github: https://github.com/CarloDePieri/odk_servermanager/tree/master/odk_servermanager/modfix

Linked vs copied
^^^^^^^^^^^^^^^^
Take a moment to notice the difference between linked and copied mods.

Usually, mods without a modfix get simply linked inside the :option:`linked_mod_folder_name <ODKSM linked_mod_folder_name>`
folder. Mod folders inside this linked mod one are *symlinks* pointing to the relevant mod folder, which means that
files inside those mod folders are the original ones: these files are managed directly by Steam and should never be touched
by an user or a modfix. This is the same behavior of the ``!Workshop`` folder, inside the main Arma 3 installation one.

When a change is needed inside a mod folder, the modfix should **copy** the mod folder with all its files to the
:option:`copied_mod_folder_name <ODKSM copied_mod_folder_name>` folder. Files inside this folder are safe to edit and
server instance specific.

.. note:: This behavior can be forced by putting a mod's name inside the
    :option:`mods_to_be_copied <ODKSM mods_to_be_copied>`.

.. warning:: When handling copied mods, the modfix should also take care of updating said mod copy inside a server instance
    when needed. Depending on the specific mod structure and/or on the ModFix, the tool behavior when updating a copied
    mod could change. Be sure to backup any important file changed inside the copied mod folder before updating its
    instance the first time, just in case.

Implement a ModFix
^^^^^^^^^^^^^^^^^^
It's relatively easy to implement a ModFix. Some example can be found inside the modfix folder.

#. First of all create a new python file inside the ``odk_servermanager\modfix`` folder. The file name will be the name
   of the ModFix you need to add to the :option:`enabled_fixes <mod_fix_settings enabled_fixes>`. For example, the file
   ``my_modfix.py`` will result in a ModFix called ``my_modfix``.

   |br|

#. Inside that file, extend the ``odk_servermanager.modfix.ModFix`` class. For example:

   |br|

   .. code-block:: python

    # file: odk_servermanager/modfix/my_modfix.py
    from odk_servermanager.modfix import ModFix


    class MyModFix(ModFix):
        """This is my wonderfull modfix"""

        name = "my_mod"  # this ModFix will be applied to the mod named 'my_mod'

   The ``name`` class field is required: by default the modfix will use that field to check if a modfix is to be applied
   to a specific mod. In this case, if the mod called ``my_mod`` is to be loaded (and the ``my_modfix`` is enabled!) this
   ModFix will be triggered.

   If a different pair mechanism between ModFix and mod is desired, the ``ModFix.does_apply_to_mod()``
   method can be overridden. It may also be necessary to override ``ModFix.update_mods_to_be_copied_list()``,
   which takes care of automatically adding mods name to the :option:`mods_to_be_copied <ODKSM mods_to_be_copied>` list
   when needed.

   |br|

#. In the MyModFix module namespace (after and outside the newly created class) save a MyModFix object in a variable
   called ``to_be_registered``, like this:

   |br|

   .. code-block:: python

    to_be_registered = MyModFix()

   This is required by the ModFix loading mechanism.

   |br|

#. MyModFix will now be loaded by the tool, but is currently doing nothing. Enter **ModFix hooks**. These are ModFix
   methods that the MyModFix class inherited and that by default are set to ``None``. Override the hook (or hooks!)
   that best cover this modfix needs and implement there the mod specific behavior. More information on hooks can be
   found in the next section.

   |br|

   .. important:: Remember to implement behaviors both for the instance *init* and *update* *stages*. More on
    this later!

#. It's a good idea to implement a proper test suite for MyModFix. Tests goes into the ``tests\modfixes`` folder,
   where you can also find several test examples.

.. |br| raw:: html

    <br />

ModFixes&#39; Hooks
^^^^^^^^^^^^^^^^^^^
This is an example of a modfix hook:

.. code-block:: python

    def hook_init_copy_replace(self, server_instance: ServerInstance, call_data: List[str]) -> None:
        """This is a hook that REPLACE the default COPY mod behavior during this instance INIT stage."""
        # do very complicated stuff here

Let's start by going over its arguments:

server_instance: ServerInstance
    This is the object representing the current server instance. It's an instance of the
    ``odk_servermanager.instance.ServerInstance`` class. It can be used to modify or to obtain information about the
    current server instance. Of particular interest is the ``server_instance.S`` object, which is a
    ``odk_servermanager.settings.ServerInstanceSettings`` instance, containing all settings currently valid for this
    server instance.

call_data: List[str]
    This is seldomly needed. It's a list containing, in order, the current *stage*, the current *operation*, and the Mod name.

There are currently 12 hooks that can be overridden. Their name is a combination of three elements:

hook^_[stage]_[operation]_[time]
    :stage: init, update
    :operation: copy, link
    :time: pre, post, replace

.. object:: stage: init

    All hooks in this *stage* get triggered when first creating the server instance.

.. object:: stage: update

    All hooks in this *stage* get triggered when the server instance folder is already present and the tool is activated.

.. object:: operation: copy

    These hooks activate if the mod is copied.

.. object:: operation: link

    These hooks activate if the mod is symlinked.

.. object:: time: pre

    These hooks activate before its designed *operation*. The default *operation* still takes place.

.. object:: time: post

    These hooks activate after its designed *operation*. The default *operation* still takes place.

.. object:: time: replace

    These hooks replace the default *operation*. Pre and Post hooks can still be called around replace hooks.

.. hint:: If a replace hook that activates and does exactly nothing is needed (for example to prevent a regular copy
    update), override the hook ``hook_update_copy_replace`` and have it do nothing with a ``pass`` instruction like this:

    .. code-block:: python

        def hook_update_copy_replace(server_instance, call_data):
            pass
