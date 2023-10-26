.. _PythonAnywhere:

PythonAnywhere Setup Instructions
===================================

.. contents:: Table of Contents

Overview
--------
Follow these instructions to set up your PythonAnywhere environment for hosting a web app using Python. This guide covers various aspects of the setup process, from naming conventions to automating deployment and updates.

Preparatory Steps
-------------------

Directory and Project Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Keep the project directory name the same as your web app name. This practice ensures consistency and simplifies management.
- To set your own directory name when cloning from a git repository, use the following command:
  ::
  
    git clone git-repo-URL desired-directory-name

Library Compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Before you start, check the compatibility of the libraries you plan to use with PythonAnywhere.
- PythonAnywhere provides a list of supported libraries; ensure you use only these.
- If a library is not supported, explore compatible alternatives or find workarounds.

Environment Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Create a .env file and load it using a library like python-decouple or Python's os module or python-dotenv.
- In cases where the library is not supported, use os.environ directly.

CDN Links and Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Verify that the CDN links you use are supported by PythonAnywhere.
- Host static files locally or on a different CDN if necessary.

Database Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- If you're using a database, configure it according to PythonAnywhere's guidelines.

Deployment Automation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Develop deployment scripts or configuration files specific to your hosting environment to automate deployment tasks.
- Our script deploy.sh updates the hosted version of Glitch Guru on PythonAnywhere.

backup.sh
----------

Here's how our backup script *backup.sh* works:

- **Backing Up Your Data:** Instead of backing up the entire project directory, which can consume excessive space and might not be supported under a Free Tier hosting plan, the "backup.sh" script takes a more efficient approach.

- **Git Branch Commit:** It creates a new Git branch named 'backup' within your project's repository and commits all the changes. If the branch already exists, it uses the same branch.

- **Pushing to Remote:** The script pushes the 'backup' branch to your remote Git repository. This action effectively saves your project's state at that moment, ensuring a reliable backup.

However, it's important to note that this method does have some limitations:

- **On-Git Assets:** Assets that are ignored by .gitignore will not be included in the backup, so be careful about any changes to those files (eg: your .env file). But, since git pull won't replace those ignored files either, so it's safe enough in normal operation.

First Time Setup Steps
-----------------------
1. Create a virtual environment:
   ::
   
     mkvirtualenv --python=/usr/bin/python3.10 venv_name

2. Clone your GitHub repository:
   ::
   
     git clone <GitHub repository URL>

3. Activate the virtual environment:
   ::
   
     workon venv_name

4. Set your virtual environment to point to the corresponding project directory
   ::
   
     setvirtualenvproject /home/username/venv_name /home/username/your_project_directory

5. Install required packages from "requirements.txt": 
   ::
   
     pip install -r requirements.txt

6. Update your Django project's settings for production by configuring the .env file.

7. Set up your web app and configure its settings on PythonAnywhere interface.

8. Update the WSGI configuration at var/www/<username>_pythonanywhere_com_wsgi.py

9. Reload your web app.

Instructions for Updating Hosted Version on PythonAnywhere
------------------------------------------------------------

Choose between manual and automated update steps:

Manual Steps (Option 1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Activate your virtual environment:
   ::
   
     workon venv_name

2. Stash any local changes:
   ::
   
     git stash

3. Pull the latest changes from the remote repository:
   ::
   
     git pull origin

4. Install updated packages:
   ::
   
     pip install -r requirements.txt

5. Touch the WSGI configuration file:
   ::
   
     touch /var/www/niloth-pythonanywhere.wsgi

6. Load fixtures into the database.

Automated Steps (Option 2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Make the backup script executable:
   ::
   
     chmod +x ./backup.sh

2. Execute the backup script:
   ::
   
     ./backup.sh

3. Execute the deployment script:
   ::
   
     ./deploy.sh

Common Update Steps
~~~~~~~~~~~~~~~~~~~~~

- Update the .env file with any new configurations.
- Refresh the WSGI configuration.
- Update web app settings.

- Delete all cached directories.
- Reload your web app.
- For a hard refresh, use Shift + Reload in your browser.

These instructions provide a comprehensive guide to setting up and maintaining your web app on PythonAnywhere. Ensure compatibility and follow best practices for a smooth hosting experience.

:ref:`Back to Top <PythonAnywhere>`
