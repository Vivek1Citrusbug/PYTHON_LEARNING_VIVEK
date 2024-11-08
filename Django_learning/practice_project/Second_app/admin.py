from django.contrib import admin
from .models import Book,Course,Profile,Review,Student
# Register your models here.

class BookCustomeClass (admin.ModelAdmin):
    list_display = ("title","author")

class ReviewCustomeClass (admin.ModelAdmin):
    list_display = ("book","review_text","rating")

class ProfileCustomeClass (admin.ModelAdmin):
    list_display = ("user","birth_date","bio")

admin.site.register(Book,BookCustomeClass)
admin.site.register(Course)
admin.site.register(Profile,ProfileCustomeClass)
admin.site.register(Review,ReviewCustomeClass)
admin.site.register(Student)
