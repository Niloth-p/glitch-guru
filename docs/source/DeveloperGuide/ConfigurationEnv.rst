.. _ConfigurationEnv:

Configuration of the environment
-----------------------------------

.. contents:: Table of Contents

Environment Variables Configuration
===================================

This section outlines the crucial environment variables used in the project's configuration. These variables are typically stored in a `.env` file for easy management. Properly configuring these variables is essential for the proper functioning of the Django project.

**1. SECRET_KEY**
   - **Purpose**: The `SECRET_KEY` is a cryptographic key used for securing various aspects of your Django application, such as session data and password resets.
   - **Example**:
     ```
     SECRET_KEY=mysecretkey
     ```

**2. DEBUG**
   - **Purpose**: The `DEBUG` variable controls whether the application runs in debug mode. In production, it should be set to `False` for security reasons.
   - **Example**:
     ```
     DEBUG=True
     ```

**3. ALLOWED_HOSTS**
   - **Purpose**: `ALLOWED_HOSTS` specifies which hosts or domains are allowed to access your Django application. It helps prevent unauthorized access.
   - **Example**:
     ```
     ALLOWED_HOSTS=localhost,example.com
     ```

**4. PROJECT_DIR**
   - **Purpose**: `PROJECT_DIR` is the path to the project's root directory. It helps in specifying absolute file paths in your application.
   - **Example**:
     ```
     PROJECT_DIR=/path/to/your/project
     ```

**5. VENV_DIR**
   - **Purpose**: `VENV_DIR` is the path to the virtual environment directory. It's essential for correctly setting up the Python environment.
   - **Example**:
     ```
     VENV_DIR=/path/to/venv
     ```

Ensure that you set these environment variables in your `.env` file with appropriate values. 
The `.env` file should be kept secure, and sensitive information like `SECRET_KEY` should never be exposed.

Refer to the `Django documentation on settings`_ for more information about these and other settings.
In Glitch Guru, we're using `python-decouple`_  for managing these environment variables.

.. _Django documentation on settings: https://docs.djangoproject.com/en/stable/topics/settings/
.. _python-decouple: https://github.com/henriquebastos/python-decouple

Constants
=========

In this section, we define the constants used in the project's configuration. 

Constants are values that do not change during the application's runtime and are typically used for settings that should remain consistent. 

**1. PAGINATE_BY**
   - **Purpose**: `PAGINATE_BY` determines the number of items displayed per page in paginated views, such as lists or search results.
   - **Default Value**: `10`

**2. MAX_CHAR_LENGTH_BUG_TITLE**
   - **Purpose**: `MAX_CHAR_LENGTH_BUG_TITLE` represents the maximum character length allowed for bug titles.
   - **Default Value**: `250`

**3. MIN_CHAR_LENGTH_BUG_TITLE**
   - **Purpose**: `MIN_CHAR_LENGTH_BUG_TITLE` specifies the minimum character length required for bug titles.
   - **Default Value**: `10`

**4. PRODUCT_NAME**
   - **Purpose**: `PRODUCT_NAME` is the constant representing the name of your product or application.
   - **Default Value**: `"Glitch Guru"`

Any variable that is intended to be constant in the project should be added to this document for easy reference. 
Ensure that these values remain consistent throughout the application's lifecycle. 

To add a new constant, follow these steps:

1. Define the constant with a clear and descriptive name.
2. Specify its purpose and usage within the project.
3. Set the default value, if applicable.

:ref:`Back to Top <Configuration of the environment>`
