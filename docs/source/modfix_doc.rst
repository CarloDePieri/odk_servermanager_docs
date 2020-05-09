Available Modfix
================
Here you can find a description of the ModFixes shipped with the current build.

cba_a3
^^^^^^

:name: cba_a3
:supported mod: `CBA: Community Based Addons for Arma 3`_

This ModFix takes care of making available a custom *cba_settings* to the server instance. The CBA mod is normally symlinked
and after that the custom *cba_settings* is symlinked (or copied) to the ``userconfig`` folder inside the Arma 3 installation
folder.

.. program:: mod_fix_settings

.. option:: cba_settings

    The absolute path of the custom ``cba_settings.sqf`` file.

    :required: yes
    :type: string

.. option:: instance_specific_cba

    If True the cba gets copied instead of symlinked, and won't be changed by instance updates.

    :required: no
    :type: string (**bool**)
    :default: ``"False"``

.. _`CBA: Community Based Addons for Arma 3`: https://steamcommunity.com/workshop/filedetails/?id=450814997

gos
^^^

:name: gos
:supported mods: `G.O.S Al Rayak`_, `G.O.S Dariyah`_, `G.O.S Gunkizli`_, `G.O.S Kalu Khan`_, `G.O.S Leskovets`_,
    `G.O.S N'ziwasogo`_, `G.O.S Song Bin Tahn`_, `G.O.S Song Bin Tanh 2.0 (APEX)`_

The gos ModFix is used as a compatibility layer between ODKSM and the unusual keys position of these mods. For each of them,
a folder is created inside the copied mod folder, then every file and folder of the mod get symlinked. All keys gets linked
inside a regular ``Keys`` folder, so that the tool can find them when linking them.

.. _`G.O.S Al Rayak`: https://steamcommunity.com/sharedfiles/filedetails/?id=648172507
.. _`G.O.S Dariyah`: https://steamcommunity.com/sharedfiles/filedetails/?id=701535490
.. _`G.O.S Gunkizli`: https://steamcommunity.com/sharedfiles/filedetails/?id=693153082
.. _`G.O.S Kalu Khan`: https://steamcommunity.com/sharedfiles/filedetails/?id=643744158
.. _`G.O.S Leskovets`: https://steamcommunity.com/sharedfiles/filedetails/?id=855464203
.. _`G.O.S N'ziwasogo`: https://steamcommunity.com/sharedfiles/filedetails/?id=694603075
.. _`G.O.S Song Bin Tahn`: https://steamcommunity.com/sharedfiles/filedetails/?id=693170122
.. _`G.O.S Song Bin Tanh 2.0 (APEX)`: https://steamcommunity.com/sharedfiles/filedetails/?id=878119643

odkai_local
^^^^^^^^^^^

:name: odkai_local
:supported mod: ODKAI_

This is used to replace the workshop mod with a local copy, which is useful during development.

.. option:: odkai_local_path

    The full path of the folder containing the local copy of the mod.

    :required: yes
    :type: string

.. _ODKAI: https://steamcommunity.com/sharedfiles/filedetails/?id=1929364814