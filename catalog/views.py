from django.shortcuts import render,get_object_or_404
from .models import Book, Author, BookInstance, Genre
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genre = Genre.objects.all().count()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1
	
	
    # Render the HTML template index.html with the data in the context variable
    return render(
         request,
         'index.html',    # find the index.html in the directory: /projectname/appname/templates/
         context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,'num_genre':num_genre,'num_visits':num_visits}
    )

from django.views import generic
from django.http import Http404

#获取指定模型（Book）的所有记录，呈现位于catalog/templates/catalog/book_list.html 的模板 
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2   # separate pages by 2 records
#context_object_name = 'my_book_list' # your own name for the list as a template variable
#template_name = 'books/my_arbitrary_template_name_list.html' # sepcify your own template name/location

#    def get_queryset(self): #cover the method of get_queryset()
#        return Book.objects.filter(title__icontains='i')[:5] # Get 5 books containing the title i

    def get_context_data(self,**kwargs):  #cover the method of get_context_data()
#        # call the base implementation first to get the context
        context = super(BookListView,self).get_context_data(**kwargs)
        # create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

def BookDetail(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book':book}
    return render(request,'catalog/book_detail.html',context)

def AuthorDetail(request,author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {'author':author}
    return render(request,'catalog/author_detail.html',context)

class AuthorListView(generic.ListView):
    model = Author




    
