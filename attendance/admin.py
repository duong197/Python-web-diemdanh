from django.contrib import admin
from .models import User, Class, Student, Fingerprint, Attendance

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'lecturer', 'start_date', 'end_date')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_info')

@admin.register(Fingerprint)
class FingerprintAdmin(admin.ModelAdmin):
    list_display = ('user', 'registered_at')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'timestamp')
