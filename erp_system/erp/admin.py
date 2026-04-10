from django.contrib import admin
from .models import Student, Teacher, Group, GroupStudents

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "last_name", "age", "phone"]
    list_filter = ["age"]
    ordering = ["-id"]
    list_editable = ["name"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "last_name", "subject", "experience"]
    list_filter = ["subject",]
    ordering = ["-id"]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["id", "group_name", "subject", "teacher", "start_date", "finish_date"]
    list_filter = ["subject"]
    ordering = ["-id"]


@admin.register(GroupStudents)
class GroupStudentsAdmin(admin.ModelAdmin):
    list_display = ["id", "group", "student"]
    ordering = ["-id"]
"id", 