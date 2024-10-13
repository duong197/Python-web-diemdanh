from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Fingerprint, Attendance, Student
@csrf_exempt
def attendance_check(request):
    if request.method == 'POST':
        try:
            # ESP8266 sẽ gửi ID dạng int trong body của POST request
            user_id = int(request.POST.get('id'))
            
            # Tìm kiếm thông tin sinh viên dựa trên ID
            student = Student.objects.get(user__id=user_id)
            
            # Tạo bản ghi điểm danh
            Attendance.objects.create(student=student)

            return JsonResponse({'status': 'success', 'message': 'Attendance recorded successfully'})

        except Student.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User not found'}, status=404)
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid ID format'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def home(request):
    return render(request, 'index.html')
