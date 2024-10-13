from django.db import models
from django.contrib.auth.models import User

# Mô hình App_User
class App_User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('lecturer', 'Lecturer'),
        ('student', 'Student'),
    ]
    
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username

# Mô hình Class
class Class(models.Model):
    name = models.CharField(max_length=255)
    lecturer = models.ForeignKey(App_User, on_delete=models.CASCADE, limit_choices_to={'role': 'lecturer'})
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

# Mô hình Student (liên kết giữa Student và Class)
class Student(models.Model):
    student = models.ForeignKey(App_User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    class_info = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.student.username} - {self.class_info.name if self.class_info else 'No Class'}"

# Mô hình Fingerprint (vân tay)
class Fingerprint(models.Model):
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    fingerprint_data = models.BinaryField()
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fingerprint of {self.user.username}"

# Mô hình Attendance (Điểm danh)
class Attendance(models.Model):
    student = models.ForeignKey(App_User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.timestamp}"
