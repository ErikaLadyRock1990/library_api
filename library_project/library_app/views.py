import json
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def save_book(request):
    if request.method == 'POST':
        data = json.load(request.body)
        title = data['title']
        author = data['author']
        genre = data['genre']
        year = data['year']

    book = Book(title=title, author=author, genre=genre, year=year)
    book.save()

    return JsonResponse({'message': 'El libro se ha guardado correctamente'})
