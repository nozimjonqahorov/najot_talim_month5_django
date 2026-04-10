from django.db import models

class SubjectChoice(models.TextChoices):
    BACKEND = "backend", "BACKEND"
    FRONTEND = "frontend", "FRONTEND"
    MOBILE = "mobile", "MOBILE"


class Student(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ism")
    last_name = models.CharField(max_length=200, verbose_name="Familiya")
    age = models.IntegerField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Student"
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Teacher(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ism")
    last_name = models.CharField(max_length=200, verbose_name="Familiya")
    subject = models.CharField(max_length=200, choices=SubjectChoice.choices)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Teacher"
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"


class Group(models.Model):
    group_name = models.CharField(max_length=300)
    subject = models.CharField(max_length=200, choices=SubjectChoice.choices)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self):
        return f"{self.group_name} | O'qituvchi: {self.teacher.name}"
    
    class Meta:
        db_table = "Group"
        verbose_name = "Group"
        verbose_name_plural = "Groups"


class GroupStudents(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group.group_name} | student:  {self.student.name}"
    
    class Meta:
        db_table = "Group_students"
