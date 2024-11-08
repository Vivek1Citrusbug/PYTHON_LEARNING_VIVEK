from django.contrib import admin
from .models import students

class MemberAdmin(admin.ModelAdmin):
    list_display = ("student_name","student_id","join_date","result")

admin.site.register(students,MemberAdmin)
# Register your models here.
