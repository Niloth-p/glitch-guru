.. _LocalSetup:

Local Setup
------------

.. contents:: Table of Contents

Setup Instructions for Contribution
====================================

Prerequisites
====================================

Before you begin, ensure you have the following prerequisites installed on your system:

- Git (Version Control System)
- Python (3.12)
- Virtualenv (for creating a virtual environment)
- Pip (Python package manager)

If using Windows, remember to set
git config --global core.autocrlf true

Cloning the Repository
====================================

1. Open your terminal and navigate to the directory where you want to clone the project.

2. Clone the GitHub repository using the following command:

   .. code-block:: bash

      git clone https://github.com/Niloth-p/glitch-guru

Using Pip and venv (Option 1)
====================================

Creating a Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Navigate to the project's root directory by using the `cd` command.

2. Create a virtual environment by running the following command:

   .. code-block:: bash

      python -m venv venv

3. Activate the virtual environment:

   On Windows:

   .. code-block:: bash

      venv\Scripts\activate

   On macOS and Linux:

   .. code-block:: bash

      source venv/bin/activate

Installing Project Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the virtual environment activated, install project dependencies using Pip. The dependencies are listed in a `requirements.txt` file. Run:

   .. code-block:: bash

      pip install -r requirements.txt

Using Pipenv (Option 2)
====================================

If you prefer to use Pipenv, you can create a new virtual environment and install the project dependencies using the following commands:

   .. code-block:: bash

      pip install pipenv  # Install Pipenv if you haven't already

      pipenv --python 3.x  # Replace 3.x with your Python version
      pipenv install

Ensure you run these commands in the project's root directory.

Environment Configuration
====================================

Refer to :ref:`ConfigurationEnv` page.

Running the Development Server
====================================

1. Start the Django development server:

   .. code-block:: bash

      python manage.py runserver --settings=GlitchGuru.settings

2. Open your web browser and visit `http://localhost:8000/` to access the locally running Glitch Guru project.

Prefer localhost over `127.0.0.1:8000` as the third-party tool Font Awesome does not support the latter. 
And, you won't be able to view any icons without loading FontAwesome libraries.

Loading data into the Database (optional)
==============================================

You can populate your database with some initial template data using the json fixtures.

.. code-block:: bash

    python manage.py loaddata bug_hub/bugs.json --settings=GlitchGuru.settings

Frequently Used Commands
====================================

For some other optional but frequently used commands, see :ref:`commands`

Making Contributions
====================================

1. Make the necessary changes and contributions to the project.

2. Remember to make the relevant changes to the docstrings, documentation and tests as well.

3. Use Git to commit your changes and push them to your forked repository on GitHub.

4. Create a pull request on the original project's repository to submit your changes for review and inclusion.

You are now set up to contribute to the Glitch Guru project.

For more detailed information on contributing and advanced configurations, refer to the project's README and contribution guidelines.

:ref:`Back to Top <LocalSetup>`
