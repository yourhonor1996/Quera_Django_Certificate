from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.db.models.query import QuerySet

# Register your models here.
from .models import Author, Book

# Aciton: delete all selected authors' countries
def clear_author_country(modeladmin, request, queryset:QuerySet):
    queryset.update(country= '')
clear_author_country.short_description = 'Clear All Selected Country'

class BookInline(admin.StackedInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    actions = [clear_author_country]
    list_filter = ['country']
    list_display = ['first_name', 'last_name', 'birth_date', 'country']
    list_editable = ['country']
    # sortable_by = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    inlines = [BookInline]
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = [('title', 'publish_date'), 'pages_count', 'author']
    # list_editable = ['pages_count']