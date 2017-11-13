from django.shortcuts import render

# Create your views here.

def index(request):
    print(type(request.user))
    return render(request,'index.html')


def student_index(request):
    return render(request,'student_index.html')


def sale_index(request):
    return render(request,'sale_index.html')

def customer_index(request):
    return render(request,'customer_index.html')

def teacher_index(request):
    return render(request,'teacher_index.html')

def customerfollowup(request):
    return render(request,'customerfollowup.html')
