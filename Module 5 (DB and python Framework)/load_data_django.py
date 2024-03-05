#Mention what command line can be used to load data into Django?
'''
->In Django, you can use the
    loaddata management command to load data from fixture files into your database.
    Fixture files are serialized representations of Django models,
    typically in JSON or YAML format.
    
#python manage.py loaddata <fixture_file>
This command will read the fixture file and
insert the data into the corresponding database tables, 
populating your database with the specified data.

'''