.. _ContributingGuide:

Contributing Guide 
====================

.. contents:: Table of Contents

Introduction
--------------
   Welcome to the Glitch Guru community! 
   
   We greatly appreciate your interest in contributing to our bug management and tracking tool built with Django. 
   Your contributions play a vital role in improving the tool and making it more efficient. 
   
   This guide will help you get started on your journey as a contributor.

Setting Up the Development Environment
----------------------------------------
   To contribute effectively, you need to set up your local development environment. Follow these steps to get started:

   - Install Python and Django.
   - Clone the project repository from `Github`_.
   - Install necessary dependencies using `pip`.

   For detailed instructions, refer to our :ref:`Tech Stack` Guide, :ref:`ConfigurationEnv`, and :ref:`LocalSetup` Guide.

Contributing Workflow
----------------------
   Our contribution process is straightforward and follows these steps:

   - Identify an issue or feature you want to work on.
      - Issues are available at `GitHub Issues`_.
      - Features planned to be enhanced are available at the :ref:`Future Enhancements` Page.
   - Fork the repository and create a new branch.
   - Make your changes, ensuring they follow our coding standards.
   - Write tests to validate your changes.
   - Create a pull request (PR) and reference the related issue.

Coding Standards
----------------
   Maintaining code quality is a top priority. We use Pylint to ensure code consistency. Make sure to:

   - Follow the PEP8 style guide.
   - Use code formatting tools like Black.
   - Include docstrings for functions and classes.
   - Provide unit tests, integration tests, and end-to-end tests.
   - If immediate updates to documentation are not feasible, add a TODO in the relevant sections and create issues connected to your PR. This helps other contributors easily identify and address these tasks.

Testing Guidelines
-------------------
   Proper testing is crucial to maintain the tool's reliability. Follow these guidelines:

   - Run tests using `coverage` by executing `coverage run manage.py test`.
   - Write comprehensive test cases for your code
   - Cross-check your testing coverage with the reports generated using `coverage report` or `coverage html`.
   - Cover unit, integration, and end-to-end testing.

Pull Request (PR) Process
--------------------------
   When you're ready to submit your contribution, follow these steps:

   - Create a PR with a clear title and description.
   - Reference the related issue.
   - Make sure your code passes all tests.

Code Review Process
--------------------
   Our community values code reviews. Reviewers will provide feedback to ensure the code meets our quality standards. Please address review comments promptly.

Issue Tracking
----------------
   To find and claim issues, visit our `GitHub Issues`_ page. We use an issue template and labeling system to make issue tracking efficient. Clear and informative issue descriptions are appreciated.

License
--------
   Glitch Guru is released under the GNU General Public License (GPL3). By contributing, you agree to license your contributions under GPL3.

Thank you for considering contributing to Glitch Guru. Your efforts are highly valued, and we look forward to working together to enhance our project!

Feel free to reach out if you have any questions or need assistance. Remember that contributions should not only include code changes but also relevant documentation updates and tests.

**Happy contributing!**

:ref:`Back to Top <Contributing Guide>`

.. _Github: https://github.com/Niloth-p/glitch-guru
.. _Github Issues: https://github.com/Niloth-p/glitch-guru/issues
.. _Contribution: #
