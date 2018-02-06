from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Category(models.Model):
    '''
    Books categories
    '''
    name = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    '''
    Books tags
    '''
    name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    # Book information
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    publication_date = models.DateField()
    press = models.CharField(max_length = 50)
    cover = models.ImageField(upload_to='covers', blank=True)
    cover_thumbnail = ImageSpecField(source='cover',
                                     format='JPEG',
                                     options={'quality': 90})
    
    # Creating information
    creater =  models.ForeignKey(User)
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Note(models.Model):
    # Books note
    title = models.CharField(max_length=70)
    body = models.TextField()
    creater =  models.ForeignKey(User)
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    book = models.ForeignKey(Book)
    
    def __str__(self):
        return self.name
    
    

