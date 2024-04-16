from django.contrib import admin

from final_project.author.models import Author


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_filter = ('first_name', 'last_name')
    # list_display = ('first_name', 'last_name')
    search_fields = ('first_name',)
