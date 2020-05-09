Troubleshooting
===============
In case something goes wrong, you will be warned by the console ui. The message there plus this documentation should be
enough to correct eventual mistakes in your config.

.. hint:: The tool *should* be able to tell you if your server instance is compromised by the error but, if the an error
    that shouldn't be there keep reappearing, you may try to delete the instance folder and regenerate with the tool just in case!

In case you need more detailed information, you have the option to activate the debug mode of the tool, uncommenting
this line in your instance's ``ODKSM.bat`` script:

.. code-block:: batch

    SET "DEBUG=true"

The tool will now produce log files containing the stack trace, which you can use to further debug the malfunction. If
you can't fix your problem this way, be sure to open `an issue`_ on our tracker!

.. note:: Be specific in the issue report about what you were doing and maybe paste along the error stack trace.

.. _an issue: https://github.com/CarloDePieri/odk_servermanager/issues
