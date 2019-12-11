Running a conversion example
****************************

Repository `DRPOWER GRG CONVERSION`_ contains:

  - the Python script *psse2grg.py* that takes one source file, either a PSSE model (.raw file) or a GRG model (.json file), as input and converts it into a given target file, either a GRG model or PSSE model.

  - a set of PSSE (.raw) files that could be used for testing in folder *PSSE-test-files*.

**NAME**

.. code::

  psse2grg.py

**SYNOPSIS**

.. code::

  python psse2grg.py [-h] [-s file -t file]

**DESCRIPTION**

The following arguments need to be given:

.. code::

  -h [--help]
    To get help on how to call the script.

  -s [--source=]<path to source/input file>
    To provide the source model to be converted.

  -t [--target=]<path to target/output file>
    To provide a target file to save the new converted model to.

*psse2grg* script documentation
===============================

.. automodule:: psse2grg

.. _`DRPOWER GRG CONVERSION`: https://stash.pnnl.gov/users/mari009/repos/drpower-grg-conversion/browse