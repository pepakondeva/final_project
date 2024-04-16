from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from final_project.account.forms import SignUpForm
from final_project.account.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ['email', 'date_joined']
    list_filter = ()
    readonly_fields = ["date_joined"]
    add_form = SignUpForm

    fieldsets = (
        ('Info', {"fields": ["email", "password"]}),
        # ("Personal info", {"fields": ["first_name", "last_name", "age"]}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "age"),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ('first_name', 'last_name')
    list_display = ("first_name", "last_name", "age")



from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

superuser_group, _ = Group.objects.get_or_create(name='Superusers')
superuser_group.permissions.set(Permission.objects.all())
staff_group, _ = Group.objects.get_or_create(name='Staff')

content_type = ContentType.objects.get_for_model(UserModel)
permissions = Permission.objects.filter(content_type=content_type)
staff_group.permissions.set(permissions)
