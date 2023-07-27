# JobBuddy Web App

This is a web application built using Python, Django, JavaScript, Bootstrap, Sass, HTML, CSS, and the SortableJs Library.

## Reason For Project

I am currently in a job search phase; hence, I need an application that tracks and manages my job applications easily while offering a pleasing UI that's easy to navigate.

## Distinctiveness and Complexity

This web application stands out in several aspects. It serves as a comprehensive job search management and tracking tool, empowering users to effortlessly add and manage new job opportunities. Within the application, users can specify crucial details about each job, including the job title, company name, current application stage (whether not applied, applied, first interview, follow-up interviews, or offer received), location, URL, job description, and the level of the position (internship, entry-level, mid-level, or senior-level). Additionally, users can indicate the mode of employment, whether it's full-time, part-time, or contract-based, among other features.

The application showcases the added jobs in an aesthetically pleasing kanban-like layout, which has been achieved using the SortableJs Library. This library enables drag and drop functionality, allowing users to effortlessly update the job stage by moving cards representing each job to different categories (e.g., not applied, applied, first interview, follow-up interviews, or offer received).

Moreover, the application boasts several other useful functionalities, including:

1. Toggling Between Active and Archived Jobs: Users can easily switch between viewing active jobs and archived jobs, enabling them to focus on their current priorities or review past opportunities.

2. Archiving Active Jobs: When appropriate, users have the option to archive active jobs, decluttering their workspace without losing any valuable information.

3. Viewing Job Details: By clicking on a specific job card, users can access and review all the pertinent details of that particular job.

4. Deleting Archived Jobs: If needed, users can remove archived jobs from the application, ensuring a clean and organized workspace.

5. Persisting Archive Toggle State: The application intelligently saves the state of the archive toggle in local storage, ensuring that the preference remains even after refreshing the page. This feature enhances user convenience and efficiency.

6. Overall, the web application provides a user-friendly and feature-rich experience, streamlining the job search management process and facilitating seamless tracking and organization of job opportunities.


In addition to its job management and tracking features, the application also incorporates authentication functionality using Django's authentication system. This means that the application allows both new and existing users to access their accounts securely.

Here's how the authentication process works:

1. User Registration: New users can register for an account by providing their desired username, email address, and a secure password. The application then stores this information securely in the database, creating a new user account.

2. User Login: Existing users can access their accounts by providing their registered username or email address along with the corresponding password. Upon successful authentication, users gain access to their personalized accounts and can manage their job search data.

3. Secure Password Storage: To ensure user data security, the application uses Django's built-in authentication system, which securely stores user passwords using cryptographic hashing techniques. This way, the actual passwords are never stored in plain text, enhancing the protection of user credentials.

By incorporating Django's authentication functionality, the application provides a robust and secure way for users to access their accounts and manage their job search activities. This ensures that each user's data is protected and accessible only by the authorized user.

## File Contents

- jobbuddy/static/jobbuddy/add.js: Javascript code for adding a new job
- jobbuddy/static/jobbuddy/index.js: Javascript code for fetching and displaying all Jobs, saving active/archive state to local storage, toggling archive/active, updating job stage by dragging and dropping, archiving a job, deleting a job, and viewing a particular jobs details
- jobbuddy/static/jobbuddy/styles.scss: scss styles for entire project
- jobbuddy/static/jobbuddy/styles.css: css styles for entire project
- jobbuddy/templates/jobbuddy/add.html: html form for adding new job
- jobbuddy/templates/jobbuddy/details.html: html form for viewing details for a job
- jobbuddy/templates/jobbuddy/index.html: html page showing all jobs where you can update by dragging and dropping and also delete/archive jobs
- jobbuddy/templates/jobbuddy/layout.html: html layout including the navbar
- jobbuddy/templates/jobbuddy/login.html: login form
- jobbuddy/templates/jobbuddy/register.html: register form
- jobbuddy/admin.py: Job model registration
- jobbuddy/models.py: Job model
- jobbuddy/urls.py: all urls and api routes
- jobbuddy/views.py: view functions for login, register, logout, adding job, getting all jobs, updating a job, getting a single job

## How to run the application

1. Install project dependencies by running pip install -r requirements.txt
2. Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.
3. Run python manage.py runserver