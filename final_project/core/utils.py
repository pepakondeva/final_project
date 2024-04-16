from django.contrib.auth import get_user_model

UserModel = get_user_model()


def is_user_staff(user):
    return user.groups.filter(name='Staff').exists()





