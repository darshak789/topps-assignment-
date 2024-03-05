#What is a QuerySet?Write program to create a new Post object in database:
'''
->In Django, a QuerySet is a collection of database queries 
    that can be executed to retrieve a set of objects from the database. 
    It allows you to interact with your database using a high-level abstraction. 
    When you perform a query, 
    Django returns a QuerySet that represents the result of that query.
    
# models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

# views.py or any other relevant file where you want to create a new Post

from .models import Post

def create_post():
    # Creating a new Post object
    new_post = Post(title="Example Post", content="This is the content of the post.")

    # Saving the Post object to the database
    new_post.save()

# Call the function to create and save a new Post
create_post()

    
'''