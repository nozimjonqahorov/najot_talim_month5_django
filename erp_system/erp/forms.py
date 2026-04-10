from django.forms import ModelForm
from .models import Student, Teacher, Group, GroupStudents


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"


class GroupStudentsFrom(ModelForm):
    class Meta:
        model = GroupStudents
        fields = "__all__"