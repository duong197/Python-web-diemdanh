from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Attendance

@csrf_exempt
def mark_attendance(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            student = Student.objects.get(student_id=student_id)
            Attendance.objects.create(student=student)
            return JsonResponse({'status': 'success'})
        except Student.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Student not found'})
    return JsonResponse({'status': 'invalid method'})

def home(request):
    return render(request, 'index.html')
