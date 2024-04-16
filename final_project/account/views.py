from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import  redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from rest_framework import permissions
from rest_framework.views import APIView

from final_project.account.forms import SignUpForm, LoginForm
from final_project.account.models import BookipediaUser, Profile
from final_project.book.models import Book

# Create your views here.



UserModel = get_user_model()

# LOGIN/REGISTER/LOGOUT/


class SignUpView(CreateView):
    model = BookipediaUser
    form_class = SignUpForm
    template_name = 'account/sign-up.html'
    success_url = reverse_lazy('index')


class SignInView(LoginView):
    form_class = LoginForm
    template_name = 'account/sign-in.html'
    next_page = reverse_lazy('index')


class LogoutViewAPI(APIView):
    """
    Djano 5 does not have GET logout route anymore, so Django Rest Framework UI can't log out.
    This is a workaround until Django Rest Framework implements POST logout.
    Details: https://github.com/encode/django-rest-framework/issues/9206
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        logout(request)
        return redirect('/')


# PROFILE #


class UserEditView(UpdateView, LoginRequiredMixin):
    model = Profile
    template_name = 'account/profile-edit.html'
    fields = ('first_name', 'last_name', 'age', 'profile_image')

    def get_success_url(self):
        created_object = self.object

        return reverse_lazy('profile-details', kwargs={
            'pk': created_object.pk
        })

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return redirect('not authorized')
        return super().dispatch(request, *args, **kwargs)


class UserDetailsView(DetailView, LoginRequiredMixin):
    template_name = 'account/profile-details.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user.pk == self.object.user_id
        context['count_books'] = Book.objects.all().filter(user=self.object.user_id).count()
        context['all_books'] = Book.objects.all().filter(user=self.object.user_id)
        context['account_details'] = UserModel.objects.filter(pk=self.object.user_id).get()
        return context
