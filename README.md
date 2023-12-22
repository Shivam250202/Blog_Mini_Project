This simple personal blog platform allows users to read blog posts and administrators to perform CRUD (Create, Read, Update, Delete) operations on blog posts.

Project Structure:
/blog-platform
    /static
        /css
            style.css
        /js
            script.js
    /templates
        index.html
        post_detail.html
        admin.html
    app.py

1. /static: Contains static assets like CSS and JavaScript files.
2. /templates: Contains HTML templates for the frontend.
3. app.py: The main Flask application file.

Setup Instructions
Initialize Git Repository:
git init

Create Virtual Environment:
python -m venv venv

Activate Virtual Environment:
venv\Scripts\activate

Install Dependencies:
1. pip install Flask-SQLAlchemy
2. pip install mysql-connector-python
3. pip install --upgrade watchdog

Configure MySQL Database:
1. Create a MySQL database named "blog_platform".
2. Update the MySQL connection details in "app.py".

Run the Application:
1. python app.py

Access the Application:
1. Open your browser and navigate to http://127.0.0.1:5000/ to view the blog platform.

Database Setup
1. The database schema includes a "Post" table with fields for 'id', 'title', 'content', and 'pub_date'.

Features

Homepage:
1. Lists all blog posts with titles and short descriptions.

Post Detail Page:
1. Displays a detailed view of a blog post when the title is clicked.

Admin Page:
1. Allows administrators to add new blog posts.
2. Provides a list of existing blog posts with the option to delete them.

   
Form Validation
1. JavaScript form validation is implemented on the admin page to ensure the title and content are not empty before submission.

   
Automatic Date and Time
1. The pub_date field in the database is automatically set to the current date and time when a post is published.


Version Control
1. The project is version-controlled using Git. Regular commits demonstrate an understanding of version control workflow.


Troubleshooting
1. If encountering issues, ensure that the MySQL server is running, and the database connection details in app.py are correct.


Additional Notes
1. This project serves as a foundational example and can be extended with additional features and improvements.
2. Feel free to explore and enhance the functionality based on your requirements!

