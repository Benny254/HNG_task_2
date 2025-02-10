from django.urls import path
from .views import BookDetailView

urlpatterns = [
    path('api/v1/books/<int:book_id>/', BookDetailView.as_view(), name='book-detail'),
]
