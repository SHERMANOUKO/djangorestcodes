from django.db import models
from django.utils import timezone

# Create your models here.
class Classes(models.Model):
    CLASS_CHOICES = [
        ('1', 'Form 1'),
        ('2', 'Form 2'),
        ('3', 'Form 3'),
        ('4', 'Form 4')
    ]

    classID = models.AutoField(primary_key=True)
    className = models.CharField(max_length=100, unique=True, choices=CLASS_CHOICES)

class Students(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    studentID = models.AutoField(primary_key=True)
    studentName = models.CharField(max_length=100)
    studentAdmNo = models.CharField(max_length=100, unique=True)
    studentGender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    studentBirthYear = models.IntegerField()

class Teachers(models.Model):
    teacherID = models.AutoField(primary_key=True)
    teacherName = models.CharField(max_length=100)
    teacherTscNo = models.CharField(max_length=100, unique=True)
    teacherJoinDate = models.DateField(auto_now_add=True)

class Subjects(models.Model):
    subjectID = models.AutoField(primary_key=True)
    subjectCode = models.IntegerField(unique=True)
    subjectName = models.CharField(max_length=100, unique=True)
    subjectGroup = models.IntegerField()

class TeacherRole(models.Model):
    roleID = models.AutoField(primary_key=True)
    teacherID = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True)
    subjectCode = models.ForeignKey(Subjects, on_delete=models.CASCADE, to_field='subjectCode')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['teacherID', 'subjectCode'], name='unique_teacher_subject')
        ]

class Marks(models.Model):
    markID = models.AutoField(primary_key=True)
    studentAdmNo = models.ForeignKey(Students, on_delete=models.CASCADE, to_field=studentAdmNo)
    subjectCode = models.ForeignKey(Subjects, on_delete=models.CASCADE, to_field='subjectCode')
    marks = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['studentAdmNo', 'subjectCode'], name='unique_student_subject')
        ]

