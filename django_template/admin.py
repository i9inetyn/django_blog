from django.contrib import admin
from .models import bookStore

class bookStoreDB(admin.ModelAdmin):
    list_display = [
        "book_title", "book_author", "year_published"
    ]


admin.site.register(bookStore, bookStoreDB)