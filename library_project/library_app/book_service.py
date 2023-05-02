from .models import Book


def save(data) -> dict:
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

    return book_data


def delete(id) -> Book:
    book = Book.objects.get(id=id)

    book.delete()

    return book
