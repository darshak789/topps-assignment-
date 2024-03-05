#Explain what does django-admin.py make messages command is used for?
'''
->this command scans your Django project's source code and
templates for translatable strings and compiles them into message files. 
These files are then sent to translators who provide translations for the strings. 
Once the translations are available, Django can use them to display 
the application's content in different languages based on user preferences.

for example:
Suppose we have a Django project with the following code in a template file (index.html)

{% block content %}
    <h1>{% trans "Welcome to My Website" %}</h1>
    <p>{% trans "This is a sample Django application." %}</p>
{% endblock %}

-In this example, the {% trans %} template tag is used to mark the strings 
that need to be translated. The make messages command
will identify these translatable strings and create a message file.

-python manage.py makemessages -l es
This command instructs Django to create message files for the Spanish language (-l es). 


'''