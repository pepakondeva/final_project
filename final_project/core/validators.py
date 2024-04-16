from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Name should contain only letters!")


def validate_title_letter_number_space(value):
    for ch in value:
        if not ch.isalnum() and ch != ' ':
            raise ValidationError(f"Ensure this value contains only letters and numbers.")


def max_size_of_the_photo(size_photo):
    filesize = size_photo.size
    if filesize > 5242880:
        raise ValidationError("The maximum file size that can be uploaded is 5MB.")


def validate_start_with_capital_letter(value):
    first_letter = value[0]
    if not first_letter.isupper():
        raise ValidationError('Your name must start with a capital letter!')


