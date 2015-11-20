from django.db import models  
from django.contrib import admin

  
class Author(models.Model):  
    AuthorID = models.CharField(max_length=30)  
    Name = models.CharField(max_length=40)
    Age = models.CharField(max_length=40)
    Country = models.CharField(max_length=40)
  
class Book(models.Model): 
    ISBN = models.CharField(max_length=100) 
    Title = models.CharField(max_length=100)  
    AuthorID = models.CharField(max_length=30)  
    Publisher = models.CharField(max_length=40)  
    PublishDate = models.DateField() 
    Price = models.CharField(max_length=10)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('AuthorID','Name')
class BookAdmin(admin.ModelAdmin):
    list_display = ('ISBN','Title')

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)