from django.urls import path
from .views import save_book

urlpatterns = [
    path('books/save/', save_book),
]
