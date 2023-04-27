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
        finish_date = data['finish_date']

    book = Book(title=title, author=author, genre=genre,
                year=year, finish_date=finish_date)
    book.save()

    book_data = {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'genre': book.genre,
        'year': book.year,
        'finish_date': book.finish_date,
    }

    return JsonResponse(book_data)


def get_books_by_name(request):
    if request.method == 'GET':
        search_bar = request.GET.get('search_bar', '')
        books = Book.objects.filter(title__icontains=search_bar)

        book_data = []
        for book in books:
            book_data.append([{
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'genre': book.genre,
                'year': book.year,
                'finish_date': book.finish_date,
            }])

        return JsonResponse({'books': book_data})


@csrf_exempt
def update(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        id = data['id']
        book = Book.objects.get(id=id)

        if book:
            if data['title']:
                title = data['title']
            elif data['author']:
                author = data['author']
            elif data['genre']:
                genre = data['genre']
            elif data['year']:
                year = data['year']
            elif data['finish_date']:
                finish_date = ['finish_date']
            else:
                return JsonResponse({'Mensaje': "No se han introducido datos"})

        book = Book(id=id, title=title, author=author, genre=genre,
                    year=year, finish_date=finish_date)
        book.save()
        
        book_data = {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'genre': book.genre,
        'year': book.year,
        'finish_date': book.finish_date,
        }

        return JsonResponse(book_data)
        else:
            return JsonResponse({f'Mensaje': "El libro con id {id} no existe"})

    


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        id = data['id']
        book = Book.objects.get(id=id)

        book.delete()
    return JsonResponse({'mensaje': f'El libro {book.title} ha sido borrado'})
