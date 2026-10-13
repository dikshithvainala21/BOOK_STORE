from django.shortcuts import get_object_or_404, render
from .models import Book
from django.http import Http404

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {
        'books': books
        })

def book_detail(request, book_id):
    # try:
    #     book = Book.objects.get(id=book_id)
    # except:
    #     raise Http404("Book does not exist")
    book = get_object_or_404(Book,id=book_id)
    return render(request, 'book_outlet/book_detail.html', {
        'book': book
        })