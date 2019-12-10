Building the GRG conversion platform
************************************

Grid Research for Good - GRG - conversion tools can be found at:

  - Python tools for working with PSSE v33 data files

    - Location: `GRG PSSE data structure location`_

    - Documentation: `GRG PSSE data structure docs`_

  - Python tools for working with GRG data files

    - Location: `GRG data structure location`_

    - Documentation: `GRG data structure docs`_

Requirements:

  - Python 3.x

  - Generic Python modules: numpy, scipy, pytest (not quite sure, but they don't hurt)

  - Specific to the tool: grg-pssedata, grg-grgdata, grg-psse2grg. These could be installed from PyPi, but to make sure we keep up with LANL current developments, it is better to be installed from the GitHub repositories, as exemplified in the Dockerfile below.

Docker File
================

.. code::

  ARG UBUNTU=ubuntu
  ARG UBUNTU_VERSION=:18.04

  FROM ${UBUNTU}${UBUNTU_VERSION} AS ubuntu-base

  ENV USER_NAME=grg-user
  ENV WORK_DIR=/home/${USER_NAME}

  # -------------------------------------------------------------------
  # By default, the docker image is built as ROOT.
  # Updating, upgrading the distribution, and installing everything
  # that needs to be installed with ROOT privileges
  # -------------------------------------------------------------------
  RUN apt-get update && \
      apt-get dist-upgrade -y && \
      apt-get install -y \
      sudo \
      git \
      nano \
      python3 \
      python3-dev \
      python3-pip && \
      rm -rf /var/lib/apt/lists/* && \
      rm -rf /var/cache/apt/archives/* && \
      ln -fs python3 /usr/bin/python && \
      echo "===== PYTHON VERSION =====" && \
      python --version && \
      echo "===== PIP VERSION =====" && \
      pip3 --version && \
      echo "===== UPGRADE PIP =====" && \
      pip3 install --upgrade pip && \
      ln -fs /usr/local/bin/pip /usr/bin/pip && \
      pip --version && \
      pip list --format=columns && \
      echo "===== installing NUMPY =====" && \
      pip install --upgrade --ignore-installed numpy && \
      echo "===== installing SCIPY =====" && \
      pip install --upgrade --ignore-installed scipy && \
      echo "===== installing PYTEST =====" && \
      pip install --upgrade --ignore-installed pytest && \
      echo "===== installing GRG PSSE data structure =====" && \
      cd /tmp/ && git clone https://github.com/lanl-ansi/grg-pssedata.git && \
      cd /tmp/grg-pssedata && python setup.py install && cd && rm -rf /tmp/grg-pssedata && \
      echo "===== installing GRG GRG data structure =====" && \
      cd /tmp/ && git clone https://github.com/lanl-ansi/grg-grgdata.git && \
      cd /tmp/grg-grgdata && python setup.py install && cd && rm -rf /tmp/grg-grgdata && \
      echo "===== installing GRG PSSE2GRG module =====" && \
      cd /tmp/ && git clone https://github.com/lanl-ansi/grg-psse2grg.git && \
      cd /tmp/grg-psse2grg && python setup.py install && cd && rm -rf /tmp/grg-psse2grg && \
      echo "===== current PYTHON modules =====" && \
      pip list --format=columns && \
      echo "root:grg" | chpasswd && \
      useradd -m -s /bin/bash ${USER_NAME}

  USER ${USER_NAME}
  WORKDIR ${WORK_DIR}

.. _`GRG PSSE data structure location`: https://github.com/lanl-ansi/grg-pssedata
.. _`GRG PSSE data structure docs`: https://grg-pssedata.readthedocs.io/en/stable/
.. _`GRG data structure location`: https://github.com/lanl-ansi/grg-grgdata
.. _`GRG data structure docs`: https://grg-grgdata.readthedocs.io/en/stable/