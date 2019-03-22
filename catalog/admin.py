from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance

#ModelAdmin class is the representation of a model in the admin interface.

class BookInline(admin.TabularInline):
    model = Book

# Define the admin class
# fields属性用 （）,使分组在元组中水平显示
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

#inline, TabularInline(horizontal layout), StackedInline(vertical layout) 
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    inlines = [BooksInstanceInline]     # enable to add inline class BooksInstanceInline

# Register the Admin classes for BookInstance using the decorator
#@admin.register(BookInstance)
#class BookInstanceAdmin(admin.ModelAdmin):
#    list_filter = ('status','due_back')
#    list_display = ('book','status','borrower','due_back','id')
#    fieldsets = (
#       (None, {
#          'fields':('book','imprint','id')
#        }),
#        ('Availability',{
#           'fields': ('status','due_back','borrower')    
#        }),
#    )

# Register the admin class with the associated model
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre)

