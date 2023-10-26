.. _Design And Architecture:

Design And Architecture
---------------------------

.. contents:: Table of Contents


.. image:: /_static/images/project_scope/decisions.jpg

Our design decisions are focused on delivering a user-friendly and efficient bug and issue tracking tool:
:ref:`project-objectives`

 
- **Embracing Minimalism**:
    Throughout the project, we have embraced minimalism as a guiding principle. 
    This approach involves keeping the user interface clean and uncluttered, avoiding unnecessary complexity, and presenting only essential features and information. 
    Minimalism enhances the tool's usability, making it more intuitive and user-friendly for bug tracking and management.

UI Design Decisions
~~~~~~~~~~~~~~~~~~~~

    - **Intuitive Navigation**: Keep the navigation straightforward and easy to understand, reducing clutter and distractions.
    - **Minimalistic Design**: Opt for a clean and minimalistic user interface to keep it simple and user-friendly.
    - **Responsive Design**: Ensure the UI adapts to different devices and screen sizes. Link to the screenshots
    - **Consistent UI Elements**: Maintain visual and functional consistency throughout the app. Maintaining consistency in the use of buttons, menus, and visual elements.
    - **Accessibility**: Implementing accessbility features to make the app accessible to more users. Link to the accessibility page.
    - **Clear Feedback**: Providing feedback mechanisms on user actions and system response, such as alerts and form errors.
        - **Error Handling**: Creating user-friendly error messages and recovery options.
    - **User-Centric Approach**: Prioritize essential user needs and features to avoid overcomplication.

Technology Stack Decisions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - **Frontend Framework**: At this juncture, we have opted not to implement a frontend framework, as we believe that using one would be an overkill. Our primary goal is to maintain a lightweight and straightforward frontend for our bug management tool. Introducing a frontend framework would add unnecessary complexity, which contradicts our preference for a minimalistic approach.

    - **Backend Framework**: We have selected the Django framework for its simplicity and rapid development capabilities.

    - **Database**: To suit the needs of small-scale projects, we have chosen a lightweight database, SQLite.

    - **Frontend Technologies**: For ease of development and responsive design, we have opted for Bootstrap CSS3. To keep the frontend lightweight, we rely on simple HTML, CSS, and minimal JavaScript.

    - **Dependency Management**: Our choice for package management tools includes pipenv and Pipfile, in favor of requirements.txt.

    - **Templating Language**: We will use Django's built-in templating language for rendering, as opposed to Jinja2.

    - **Basic Deployment**: Our deployment strategy involves hosting the application on a simple platform, such as PythonAnywhere.

    - **Linting and Documentation**: We plan to use Sphinx and ReadTheDocs for linting, documentation, and maintaining code quality.

    - **CI/CD Pipelines**: We will implement Continuous Integration/Continuous Deployment (CI/CD) pipelines using tools like GitHub Actions to automate testing and deployment processes.

    - **Basic Data Security**: We prioritize basic data security practices while avoiding unnecessary complexity. This includes using an `.env` file to store secrets, employing a randomly generated secret key, and enforcing HTTPS for browser security.

    - **CDNs for Static Files**: To optimize the efficiency and performance of our application, we have chosen to leverage Content Delivery Networks (CDNs) for serving static files. This approach reduces the server load and significantly improves page load times, resulting in an enhanced user experience.


Functional Design Decisions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    - **Simplified Workflow**: Our ticketing system will follow a simple, straightforward and intuitive workflow. Users can create, assign, resolve, and close tickets with minimal friction.
    - **Minimal Customization**: Limit customization options to essential features.
    - **Search and Filtering**: The tool will offer robust search and filtering capabilities, allowing users to quickly locate specific bug reports based on various criteria. This feature simplifies the task of finding and managing relevant issues.
    - **Scalability**: The architecture will be designed with scalability in mind, ensuring that the bug management tool can grow and adapt to the evolving needs of the organization.
    - **No Edit and Delete Views**: Allowing any visitor to edit or delete bug reports could potentially lead to unintended consequences, including the risk of clearing the entire database. Thus, the decision was made to postpone the implementation of edit and delete views to after the introduction of authentication (Wikimedia Auth).

.. - **Page-based Pagination**: over other types of pagination because of the intuitive and simple interface


Open-Source Design Decisions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have adopted a **comprehensive holistic approach**: We placed a strong focus not only on the end-user experience, but we were committed to ensuring a positive experience for the developer community as well, fostering a collaborative environment.

    - **Developer-Centric Approach**: Prioritizing contributing developers' needs and preferences in the development process.
    - **Clear Documentation**: Provide comprehensive and well-organized documentation to facilitate contribution.
    - **Contribution Guidelines**: Publish clear contribution guidelines and a code of conduct for a positive community.
    - **Regular Updates**: Maintain active development and release updates to keep the project engaging.
    - **Transparent Decision Making**: Share the rationale behind design and technical choices to engage the community.
    - **Choice Justifications**: Document why specific technologies, libraries, or solutions were chosen over alternatives.
    - **Quality Code**: Prioritize clean and well-documented code for ease of maintenance and understanding.
    - **Community Feedback Integration**: Embrace community feedback and contributions to enhance the app.

These design decisions emphasize the transparency of design and technology choices, creating an open and collaborative development environment.
They have been tailored for simplicity, efficiency, and essential functionality.

:ref:`Back to Top <Design And Architecture>`
