from django.conf.urls import url

from . import views

app_name = 'books'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^book/(?P<slug>[-_\w]+)/$',
        views.BookListView.as_view(),
        name='book_slug'),
    url(r'^book/(?P<book_slug>[-_\w]+)/(?P<slug>[-_\w]+)/',
        views.NoteView.as_view(),
        name='book_note_slug'),
]