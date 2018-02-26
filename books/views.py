from django.http import HttpResponseNotFound  
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.utils.text import slugify

import markdown
from markdown.extensions.toc import TocExtension

from .models import Book, Note

class IndexView(ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = 'books_list'
    

class BookListView(ListView):
    def get(self, request, *args, **kwargs):
        self.book = get_object_or_404(Book, slug=self.kwargs.get('slug'))
        if not self.book.note_set.last():
            return HttpResponseNotFound('<h1>No Bookmark Here</h1>') 
        return redirect(self.book.note_set.last())


class NoteView(DetailView):
    model = Note
    template_name = 'books/note.html'
    context_object_name = 'note'
        
    def get_object(self, queryset=None):
        note = super().get_object(queryset=queryset)
        md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                TocExtension(slugify=slugify),
            ])
        note.body = md.convert(note.body)
        note.toc = md.toc
    
        return note    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        note = self.object
        
        notes_list = list(note.book.note_set.all().order_by('create_time'))
        context['notes_list'] = notes_list
        
        return context
    