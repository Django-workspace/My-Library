from msilib.schema import Class
from pyexpat import model
from re import template
from django.views.generic import ListView

from .models import Book

class BookListView(ListView):
    model= Book
    template = 'book_list.html'



# Create your views here.
