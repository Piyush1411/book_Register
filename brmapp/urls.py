from django.contrib import admin
from django.urls import path,include, re_path
from .views import helloView, addBookView, addBook, editBook,editBookView,deleteBookView
# from .api_views import BookListAPIView, BookDetailAPIView, BookCreateAPIView, BookUpdateAPIView, BookDeleteAPIView

urlpatterns = [
    path('',helloView),
    path("add-book/",addBookView),
    path("add-book/add",addBook),
    path("edit-book/",editBookView),
    path("edit-book/edit",editBook),
    path("delete-book",deleteBookView),
    # path('api/books/', BookListAPIView.as_view(), name='book-list'),
    # path('api/books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    # path('api/books/create/', BookCreateAPIView.as_view(), name='book-create'),
    # path('api/books/<int:pk>/update/', BookUpdateAPIView.as_view(), name='book-update'),
    # path('api/books/<int:pk>/delete/', BookDeleteAPIView.as_view(), name='book-delete'),
]