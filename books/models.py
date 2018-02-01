from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    '''
    Books categories
    '''
    name = models.CharField(max_length = 10)
    
    
class Tag(models.Model):
    '''
    Books tags
    '''
    name = models.CharField(max_length = 20)
    

class Book(models.Model):
    # Book information
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    publication_date = models.DateTimeField()
    press = models.CharField(max_length = 50)
    
    # Creating information
    creater =  models.ForeignKey(User)
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    
class Note(models.Model):
    # Books note
    title = models.CharField(max_length=70)
    body = models.TextField()
    creater =  models.ForeignKey(User)
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    book = models.ForeignKey(Book)
    
    
    

