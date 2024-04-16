from django.urls import path

from final_project.author.views import CreateAuthor, EditAuthor, delete_author_view, DetailsAuthor

urlpatterns = (
    path('add/', CreateAuthor.as_view(), name='author add'),
    path('edit/<int:pk>/', EditAuthor.as_view(), name='author edit'),
    path('delete/<int:pk>/', delete_author_view, name='author delete'),
    path('details/<int:pk>/', DetailsAuthor.as_view(), name='author details'),
)