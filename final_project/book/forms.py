from django import forms

from final_project.book.models import Book


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('user', )

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title of the book',
            }),
            'review': forms.Textarea(attrs={
                'placeholder': 'Write review of the book',
            }),

            'image': forms.FileInput(),
        }


class BookDeleteForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('image', 'user')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (key, value) in self.fields.items():
            value.widget.attrs['disabled'] = True
            value.widget.attrs['readonly']= True




