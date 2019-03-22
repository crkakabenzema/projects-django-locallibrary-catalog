from django.urls import path
from . import views

#app_name = "catalog"
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(),name='books'),
    path('book/<int:book_id>', views.BookDetail,name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:author_id>',views.AuthorDetail, name='author-detail'),
]

#urlpatterns += [
#    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
#]
