from django.contrib import admin

from final_project.book.models import Book


# Register your models here.


@admin.register(Book)
class AdminAuthor(admin.ModelAdmin):
    list_filter = ('title', 'genre')
    search_fields = ('title',)

