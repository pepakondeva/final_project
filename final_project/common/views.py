from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic as view

from final_project.book.models import Book

UserModel = get_user_model()


class IndexView(view.ListView):
    template_name = 'common/home-page.html'
    model = Book

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('date_of_publication')
        pattern = self.__get_pattern()
        if pattern:
            queryset = queryset.filter(title__icontains=pattern.lower())
        return queryset

    def __get_pattern(self):
        return self.request.GET.get('pattern', None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def authorized(request):
    return render(request, 'not-authorized.html')
