.. _specs:

Specifications
===============

.. contents:: Table of Contents

Assumptions
-----------
In developing our bug and issue tracking tool, we operate under certain assumptions:

Security and Access Assumptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **User Authentication**: We assume users are authenticated before accessing the system. This app does not provide built-in authentication.
- **User Permissions**: Users have appropriate permissions for accessing and modifying project data. This app does not include an authorization system, as of now.
- **Browser Security**: Browser security measures are in effect for data safety.
- **Data Privacy**: Data privacy and security measures comply with relevant regulations (e.g., GDPR), but the app does not verify or enforce this compliance.

Accessibility and Connectivity Assumptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Accessibility**: This app is designed to meet specific accessibility standards to ensure inclusivity for all users. 
- **Internet Connectivity**: Users are expected to have internet connectivity to access the tool as it's a web-based application. Offline functionality is not supported by this app.

Infrastructure and Performance Assumptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Moderate Server Resources**: We assume the availability of servers with adequate resources for optimal performance. 
- **Server Redundancy**: The assumption is that redundant servers are implemented to ensure high availability and fault tolerance. 
- **Scalable Infrastructure**: We anticipate that the infrastructure can be scaled as user and data volume increase, but this app does not include built-in infrastructure scaling.
- **Performance Monitoring**: Continuous monitoring is expected to maintain optimal system performance. 

Data Management Assumptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Data Backup**: Regular backups of project data are maintained to prevent data loss.
- **Data Retention**: Established policies are in place for data retention and archiving.

Limitations
-----------
While we strive to provide a comprehensive bug tracking solution, our project has some limitations:

- **Offline Usage**: Our tool requires an internet connection; it doesn't support offline usage.
- **Browser Compatibility**: It's optimized for modern browsers, and some features may not work on older browser versions.
- **Scalability**: While designed for small to medium-sized teams, it may face limitations in handling very large-scale projects. Scalability challenges include handling high traffic, caching, optimizing database performance, and load balancing.
- **Performance**: The app's performance may vary based on the server's resources and internet connectivity.
- **Privacy Regulations**: Compliance with data privacy regulations (e.g., GDPR) depends on user configurations and usage.
- **External Services**: The app's functionality depends on third-party services and may be affected by their availability.
- **Integration Limitations**: While integration is possible, the app may not fully support all external services or APIs.

URL Parameters
~~~~~~~~~~~~~~~~

When accessing the bug list, you have the option to search the bug list, filter it, or navigate to a specific page. However, it's important to note that these operations cannot be combined in a single URL. Only one of the following parameters can be accessed from the bug list URL at a time:

- Bug type
- Bug status
- Search query
- Page number

Compatibility
~~~~~~~~~~~~~~~~

Our bug tracking tool is designed with compatibility in mind, although some aspects are still under development and testing. Here are the current compatibility considerations:

- **Web Browsers and Operating Systems**: Compatibility with various web browsers and operating systems is an ongoing process. At present, extensive testing has not been completed, and we are actively working to enhance compatibility in this regard.

- **Device Responsiveness**: The tool is designed to be responsive to different screen sizes and has been tested and supported to ensure a consistent user experience across various devices.

Please stay updated with our documentation for the latest information on compatibility and ongoing development efforts.

Tech Stack Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~

- **Hosting on PythonAnywhere - Free Tier**: Note that hosting on the PythonAnywhere Free Tier may come with certain limitations, and it's essential to be aware of these constraints.
- **Monitoring with UptimeRobot - Free Tier**: UptimeRobot, our monitoring tool, has limitations in terms of monitoring frequency and alerting options. It only monitors in intervals of 5 mins, hence that affects the effectiveness of real-time monitoring.
- **Font Awesome**: The reliance on external resources may introduce latency if network connectivity is slow. 
- **Dependabot**: Dependabot automates dependency updates, but it may introduce compatibility issues or break existing functionality when updating dependencies in the codebase.
- **Python** may have performance limitations in high-throughput or resource-intensive scenarios. Additionally, Python's Global Interpreter Lock (GIL) can impact multi-threaded performance.
- The UI may not be fully supported in older web browsers, potentially limiting the user experience for users on outdated browser versions.
- **JavaScript**: Its execution may be limited in environments with disabled or restricted JavaScript capabilities.
- **Shell Script**: The use of shell scripts for certain operations may introduce platform-specific limitations, affecting cross-platform compatibility.
- **Other Third Party Tool and Library Limitations**: Various components of our tech stack - tools and libraries may have their own constraints and restrictions that can impact the functionality of our bug tracking tool. 

:ref:`Back to Top <specs>`
