
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Book
from .forms import BookModelForm

def book_list(request):
    selected_title = request.GET.get('title', '')
    selected_author = request.GET.get('author', '')
    selected_genre = request.GET.get('genre', '')
  
    books =  Book.objects.all()

    # Apply filters
    if selected_title:
        books = books.filter(title__icontains=selected_title)
    if selected_author:
        books = books.filter(author__icontains=selected_author)
    if selected_genre:
        books = books.filter(genre__iexact=selected_genre)
      
      
    genres = list(books.values_list('genre', flat=True))

    page = request.GET.get('page', 1)  # Default to page 1 if not provided
    paginator = Paginator(books, 2)  # Show 2 books per page

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    # Fetch distinct titles, authors, and genres for dropdowns
    titles = Book.objects.values_list('title', flat=True).distinct().order_by('title')
    authors = Book.objects.values_list('author', flat=True).distinct().order_by('author')
    genres = Book.objects.values_list('genre', flat=True).distinct().order_by('genre')


    context = {
        'books': books,
        'titles': titles,
        'authors': authors,
        'genres': genres,
        'selected_title': selected_title,
        'selected_author': selected_author,
        'selected_genre': selected_genre,
    }
    return render(request, 'books.html', context)


def book_create(request):
    
    if request.method == "POST":
        form = BookModelForm(request.POST)

        isbn = request.POST.get('isbn')
        if isbn and Book.objects.filter(isbn__iexact=str(isbn)):
            return JsonResponse({'status': 'error', 'message': 'Book with this ISBN already exists.'}, status=400)
        
        if form.is_valid():
            book_obj = form.save(commit=False)
            book_obj.save()
                
            return JsonResponse({'status': 'success', 'book_id': book_obj.id, 'name': book_obj.title}, status=200)

        else:
            print('invalid', form)
    return JsonResponse({'status': 400, 'message': 'Invalid request method.'})


def export_books(request):
    books = Book.objects.all()
    data = serializers.serialize('json', books)
    response = HttpResponse(data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="books.json"'
    return response
