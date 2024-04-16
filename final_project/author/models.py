from django.core.validators import MinLengthValidator
from django.db import models

from final_project.core.validators import validate_only_letters, validate_start_with_capital_letter


# Create your models here.


class Author(models.Model):
    MIN_LENGTH_NAME = 2
    MAX_LENGTH_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=(MinLengthValidator(MIN_LENGTH_NAME),
                    validate_only_letters,
                    validate_start_with_capital_letter,),
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=[MinLengthValidator(MIN_LENGTH_NAME),
                    validate_only_letters,
                    validate_start_with_capital_letter],
    )

    image = models.URLField(
        null=True,
        blank=True,
    )

    about = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'