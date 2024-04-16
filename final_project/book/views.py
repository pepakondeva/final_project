from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic as view
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from final_project.book.forms import BookCreateForm, BookDeleteForm
from final_project.book.models import Book

# Create your views here.

UserModel = get_user_model()


class CreateBook(view.CreateView, LoginRequiredMixin):
    form_class = BookCreateForm
    template_name = 'book/create-book.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form(*args, **kwargs)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('profile-details', pk=request.user.pk)


class EditBook(view.UpdateView, LoginRequiredMixin):
    model = Book
    fields = ('title', 'author', 'genre', 'review', 'image')
    template_name = 'book/edit-book.html'

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('book details',
                            kwargs={'pk': created_object.pk})

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return redirect('not authorized')
        return super().dispatch(request, *args, **kwargs)


class DetailsBooks(view.DetailView, LoginRequiredMixin):
    model = Book
    template_name = 'book/details-book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user.pk == self.object.user_id

        return context


@login_required
def delete_book_view(request, pk):
    book = Book.objects.filter(pk=pk).get()
    form = BookDeleteForm(instance=book)

    if request.method == 'POST':
        book.delete()
        return redirect('profile-details', pk=request.user.pk)

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'book/delete-book.html', context)
