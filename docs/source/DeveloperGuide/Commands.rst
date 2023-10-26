.. _Commands:

Frequently used Commands
------------------------

.. contents:: Table of Contents

Django 
=======================

Running tests:

.. code-block:: bash
    
    Run with coverage run manage.py module_name

Create a superuser:

.. code-block:: bash

    `python manage.py createsuperuser`.

Apply database migrations:

.. code-block:: bash

    python manage.py migrate --settings=GlitchGuru.settings

Collect static files:

.. code-block:: bash
        
    python manage.py collectstatic --noinput --settings=GlitchGuru.settings

Documentation
=======================

1. **Write Documentation**: Create `.rst` files in the `source` folder to write documentation content.

   .. code-block:: rst

      .. include:: path/to/your/file.rst

2. **Create Table of Contents**: In your `.rst` files, use directives like `.. toctree::` to create a table of contents.

   .. code-block:: rst

      .. toctree::
         :maxdepth: 2
         :caption: Contents:

3. **Cross-Reference**: To link to other parts of the documentation, use `:ref:` or `:doc:` directives.

   .. code-block:: rst

      See :doc:`path/to/another/file`.

4. **Build HTML Documentation**:

   .. code-block:: bash

      make html

Feel free to provide feedback or contribute to this documentation by following our contribution guidelines.

:ref:`Back to Top <Commands>`
