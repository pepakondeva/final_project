from django import forms

from final_project.author.models import Author


class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name')

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter Last Name'
            }),
        }


class AuthorDeleteForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (key, value) in self.fields.items():
            value.widget.attrs['disabled'] = True
