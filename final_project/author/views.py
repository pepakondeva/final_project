from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as view

from final_project.author.forms import AuthorCreateForm, AuthorDeleteForm
from final_project.author.models import Author
from final_project.book.models import Book
from final_project.core.utils import is_user_staff


# Create your views here.


class CreateAuthor(view.CreateView, LoginRequiredMixin):
    form_class = AuthorCreateForm
    template_name = 'author/create-author.html'

    def get_success_url(self):
        return reverse_lazy('book add')


class EditAuthor(view.UpdateView, LoginRequiredMixin):
    model = Author
    fields = '__all__'
    template_name = 'author/edit-author.html'

    def get_success_url(self):
        created_object = self.object

        return reverse_lazy('author details', kwargs={
            'pk': created_object.pk
        })

class DetailsAuthor(view.DetailView, LoginRequiredMixin):
    model = Author
    template_name = 'author/details-author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.filter(pk=self.kwargs['pk']).get()
        context['book'] = Book.objects.all().filter(author_id=author.pk).distinct('title')
        return context




@login_required
def delete_author_view(request, pk):
    author = Author.objects.filter(pk=pk).get()
    form = AuthorDeleteForm(instance=author)

    if request.method == 'POST':
        Book.objects.filter(author=author).delete()
        author.delete()
        return redirect('index')

    context = {
        'form': form,
        'author': author,
        'is_user_staff': is_user_staff(request.user)
        }

    return render(request, 'author/delete-author.html', context)