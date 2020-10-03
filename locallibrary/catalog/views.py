from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    num_tec_book = Book.objects.filter(genre = 1).count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_tec_book': num_tec_book,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def message(request):
    string = ""
    return HttpResponse(string)

from django.views import generic
class BookListView(generic.ListView):
    model = Book    

class BookDetailView(generic.DetailView):
    model = Book