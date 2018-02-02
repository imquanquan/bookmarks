from django.contrib import admin
from .models import Book, Category,  Note, Tag

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Note)
admin.site.register(Tag)