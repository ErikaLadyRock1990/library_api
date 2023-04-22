import json
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def save_book(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        title = data['title']
        author = data['author']
        genre = data['genre']
        year = data['year']

    book = Book(title=title, author=author, genre=genre, year=year)
    book.save()

    book_data = {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'genre': book.genre,
        'year': book.year,
    }

    return JsonResponse(book_data)


def get_books_by_name(request):
    if request.method == 'GET':
        search_bar = request.GET.get('search_bar', '')
        books = Book.objects.filter(title__icontains=search_bar)
        '''
        book_data = [{
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'genre': book.genre,
            'year': book.year,
        } for book in books]
        '''
        book_data = []
        for book in books:
            book_data.append([{
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'genre': book.genre,
                'year': book.year,
            }])

        return JsonResponse({'books': book_data})


@csrf_exempt
def update(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        id = data['id']
        title = data['title']
        author = data['author']
        genre = data['genre']
        year = data['year']

    book = Book(id=id, title=title, author=author, genre=genre, year=year)
    book.save()

    book_data = {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'genre': book.genre,
        'year': book.year,
    }

    return JsonResponse(book_data)
