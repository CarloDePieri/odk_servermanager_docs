***********************
ODK Server Manager tool
***********************

.. image:: https://github.com/CarloDePieri/odk_servermanager/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/CarloDePieri/odk_servermanager/actions/workflows/ci.yml
    :alt: Travis build
.. image:: https://coveralls.io/repos/github/CarloDePieri/odk_servermanager/badge.svg?branch=master
    :target: https://coveralls.io/github/CarloDePieri/odk_servermanager?branch=master
    :alt: Coverage status
.. image:: https://img.shields.io/github/license/CarloDePieri/odk_servermanager
    :target: https://github.com/CarloDePieri/odk_servermanager/blob/master/LICENSE
    :alt: License
.. image:: https://img.shields.io/badge/os-Windows-blue
    :target: https://github.com/CarloDePieri/odk_servermanager
    :alt: Supported os: Windows
.. image:: https://img.shields.io/maintenance/yes/2024
    :target: https://github.com/CarloDePieri/odk_servermanager
    :alt: Maintained!
.. image:: https://img.shields.io/github/v/release/CarloDePieri/odk_servermanager
    :target: https://github.com/CarloDePieri/odk_servermanager/releases/latest
    :alt: Latest Release

Welcome!

.. image:: https://www.odkclan.it/img/ODK-logo.jpg
    :height: 100 px
    :alt: ODK Clan website
    :target: https://www.odkclan.it/

This is the documentation for ODKSM, hosted on ReadTheDocs both in `english`_ and in `italian`_.

ODKSM_ is an open source python tool to quickly and easily create more than one Arma 3 server instance and manage their
settings, mods and keys. It does so by intelligently using symlinks, which keeps server instances' folders small, easy
to update and archive.

It mainly caters to dedicated server maintainers, but could surely come in handy for mission makers.

Main features:

* Having separated server instances and mixing symlink with real configuration file result in a clean and organized Arma 3 main folder
* **ONE** easy to understand and thoroughly documented configuration file to manage the whole instance
* Flexible .bat scripts to call the tool that can easily adapt to different folders structures
* Simply running the tool is enough to keep mods, keys and Arma configuration files updated
* Quickstart tool to automate initial creation of multiple instances
* Modular architecture that allows to quickly implement mod specific behaviour
* Configuration file templates support

.. _ODKSM: https://github.com/CarloDePieri/odk_servermanager
.. _english: https://odksm.readthedocs.io/en/latest/
.. _italian: https://odksm.readthedocs.io/it/latest/
