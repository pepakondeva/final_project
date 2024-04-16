from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm

from final_project.account.models import Profile

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First Name',
                              widget=forms.TextInput(attrs={
                                  'placeholder': 'Enter your first name'
                              }))
    last_name = forms.CharField(label='Last Name',
                              widget=forms.TextInput(attrs={
                                  'placeholder': 'Enter your last name'
                              }))
    age = forms.IntegerField(label='Age',
                              widget=forms.NumberInput(attrs={
                                  'placeholder': 'Enter your age'
                              }))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name',)
        field_classes = {'username': UsernameField}

        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address',
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            age=self.cleaned_data['age'],
            user=user,
        )

        if commit:
            profile.save()
        return user


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.EmailInput(attrs={'autofocus': True, 'placeholder': 'Enter your email'}))
    password = forms.CharField(strip=False,
                               widget=forms.PasswordInput(attrs={
                                   "autocomplete": "current-password",
                                   "placeholder": "Enter your password",
                               }))


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.CharField()

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'first_name', 'last_name', 'age')
        field_classes = {'username': UsernameField}
