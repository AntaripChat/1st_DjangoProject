from django.shortcuts import redirect, render,HttpResponse
from .models import studentdata

# Create your views here.
def index(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll = request.POST.get('roll')
        phone = request.POST.get('phone')
        stu = studentdata(name=name,email=email,roll=roll,phone=phone)
        stu.save()
    return render(request,'index.html')
