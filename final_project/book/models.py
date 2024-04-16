from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from final_project.author.models import Author
from final_project.core.validators import validate_title_letter_number_space, max_size_of_the_photo

UserModel = get_user_model()


class Book(models.Model):
    MIN_LENGTH_NAME = 30
    MAX_LENGTH_TITLE = 40
    MIN_LENGTH_TITLE = 2
    MAX_LENGTH_GENRE = 30

    CHOICES = (
        ('Fantasy', 'Fantasy'),
        ('Science Fiction', 'Science Fiction'),
        ('Romance', 'Romance'),
        ('Mystery/Thriller', 'Mystery/Thriller'),
        ('Young adult', 'Young adult'),
        ('Non-fiction', 'Non-fiction'),
        ('Fiction', 'Fiction'),
    )

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        validators=(validate_title_letter_number_space, MinLengthValidator(MIN_LENGTH_TITLE),),
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )

    genre = models.CharField(
        choices=CHOICES,
        max_length=MAX_LENGTH_GENRE,
    )

    review = models.TextField(
    )

    image = models.ImageField(
        upload_to='book/',
        validators=(max_size_of_the_photo,),
    )

    date_of_publication = models.DateField(auto_now=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return self.title





