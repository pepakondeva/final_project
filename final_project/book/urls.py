from django.urls import path

from final_project.book import views

urlpatterns = (
    path('add/', views.CreateBook.as_view(), name='book add'),
    path('edit/<int:pk>/', views.EditBook.as_view(), name='book edit'),
    path('delete/<int:pk>/', views.delete_book_view, name='book delete'),
    path('details/<int:pk>/', views.DetailsBooks.as_view(), name='book details'),
)