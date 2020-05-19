Troubleshooting
===============
In case something goes wrong, the console ui will present warning messages. These messages plus this documentation
should be enough to correct eventual mistakes in the config.

.. hint:: The tool *should* be able to tell if the server instance is compromised by the error but, if an error
    that shouldn't be there keep reappearing, a possible workaround could be to delete the instance folder and
    have the tool generate it again!

If more detailed information are needed, there's the option to activate the tool debug mode, uncommenting
this line in the instance's ``ODKSM.bat`` script:

.. code-block:: batch

    SET "DEBUG=true"

The tool will now produce log files containing the python stack trace, which can be used to further debug the
malfunction. If the problem can't be fixed this way, be sure to open `an issue`_ on our tracker!

.. note:: Be specific in the issue report about what you were doing and maybe paste along the error stack trace.

.. _an issue: https://github.com/CarloDePieri/odk_servermanager/issues
