#Why Django should be used for web-development? Explain how you can create a project in Django?


'''
-Django is a robust web framework that offers several advantages for web development. 
-It follows the Model-View-Controller (MVC) architectural pattern, promoting a clean and organized code structure.

why Django is commonly used for web development:
High-level Abstractions: 
    Django provides high-level abstractions for common web development tasks, such as handling forms, database queries, and URL routing. 
    This allows developers to focus on the application's logic rather than dealing with low-level details.

ORM (Object-Relational Mapping): 
    Django's ORM system allows you to interact with databases using Python objects, 
    abstracting away the need for raw SQL queries.
    This simplifies database operations and enhances code readability.

Built-in Admin Panel: 
    Django comes with a built-in admin panel that can be easily customized. 
    It provides an out-of-the-box solution for managing database records and 
    is a significant time-saver during the development process.

Security Features:
    Django incorporates security best practices by default.
    It helps prevent common security mistakes such as SQL injection, cross-site scripting,
    and cross-site request forgery.

Scalability:
    Django is scalable and can handle projects of various sizes. 
    Its modularity allows developers to build components that 
    can be reused in different parts of the application, contributing to scalability.
    
(Django follows the Model-View-Controller (MVC) architectural pattern, but the terms used are slightly different. 
In Django, the pattern is referred to as Model-View-Template (MVT))

Install Django:
     pip install django

Create a Django Project:
    django-admin startproject project_name
    
Create a Django App:
    python manage.py startapp app_name

Run development server:
    python manage.py runserver 
    #if we want to run on specific port we can append port i.e. runserver 8008
    
    

'''