Development
===========

The ``pysec`` program is developed by Martin Thoma. The development began in
February 2015.

It is developed on GitHub: https://github.com/MartinThoma/pysec

You can file issues and feature requests there. Alternatively, you can send
me an email: info@martin-thoma.de

Contributions
-------------

Everybody is welcome to contribute to ``pysec``. You can do so by

* Adding ideas how to find a lost / stolen notebook again
* Improving the documentation
* Development (please look at the issue tracker on GitHub)


I suggest reading the issues page https://github.com/MartinThoma/pysec/issues
for more ideas how you can contribute.


Tools
-----

* ``nosetests`` for unit testing
* ``pylint`` to find code smug
* GitHub for hosting the source code
* https://pythonhosted.org/pysec for hosting the documentation



Documentation
-------------

The documentation is generated with `Sphinx <http://sphinx-doc.org/latest/index.html>`_.
On Debian derivates it can be installed with

.. code:: bash

    $ sudo apt-get install python-sphinx

Sphinx makes use of `reStructured Text <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_

The documentation can be built with ``make html``.



Current State
-------------

* lines of code without tests: LOC (make countc)
* lines of test code: LOT (make countt)
* test coverage: cov (make test)
* pylint score: lint

::

    date,        LOC,  LOT, cov, lint, cheesecake_index, users, changes
    2015-02-09,  176,    6, 61%, 9.28,          127/555,     1, initial commit
