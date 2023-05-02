import json
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from .book_service import *


@csrf_exempt
def save_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book_data = save(data)
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
        data = json.loads(request.body)
        update_fields = {}
        id = data['id']

        for clave, valor in data.items():
            update_fields[clave] = valor
            book = Book.objects.get(id=id)

            for clave, valor in update_fields.items():
                setattr(book, clave, valor)

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


@csrf_exempt
def delete_book(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        id = data['id']
        book = delete(id)
    return JsonResponse({'mensaje': f'El libro {book.title} ha sido borrado'})
