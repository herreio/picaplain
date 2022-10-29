=========
picaplain
=========

``picaplain`` is a Python package that allows to parse
`plain serialized PICA data <https://format.gbv.de/pica/plain>`_ from K10plus.

Installation
============

... via SSH
~~~~~~~~~~~

.. code-block:: bash

    pip install -e git+ssh://git@github.com/herreio/picaplain.git#egg=picaplain

... or via HTTPS
~~~~~~~~~~~~~~~~

.. code-block:: bash

    pip install -e git+https://github.com/herreio/picaplain.git#egg=picaplain


Usage Example
=============

Date source: `K10plus UnAPI <https://wiki.k10plus.de/x/CYCWBw>`_

.. code-block:: python

    import picaplain
    import urllib.request
    unapi_url = "https://unapi.k10plus.de/?format=pp&id=opac-de-627:ppn:84738084X"
    connection = urllib.request.urlopen(unapi_url)
    plain = connection.read().decode("UTF-8")
    connection.close()
    title = picaplain.K10plus(plain)
    items = title.get_holdings_via_eln("DDSU")
