from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect

from app.forms import ComplaintsForm, NotificationForm, StudentForm
from app.models import  Complaints, Notification, Login


# Create your views here.

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        print(username)
        password=request.POST.get('pass')
        print(password)
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            Login(request,user)
            if user.is_staff:
                return redirect('admin_Temp')
            elif user.is_student:
                return redirect('student_Temp')
    else:
        messages.info(request,'INVALID CREDENTIALS')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

def home(request):
    return render(request,'home.html')

def admin_Temp(request):
    return render(request,'admin_Temp/index.html')

def add_Notification(request):
    form=NotificationForm()
    if request.method=='POST':
        form=NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_Notification')
    return render(request,'admin_Temp/add_Notification.html',{'form':form})

def view_Notification(request):
    data=Notification.objects.all()
    return render(request,'admin_Temp/view_Notification.html',{'data':data})



##################################################################################################################
def add_Studenta(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            return redirect('login_view')
    return render(request, 'add_Studenta.html', {'form': form})

def view_Studenta(request):
    data=Login.objects.all()
    return render(request,'admin_Temp/view_Studenta.html',{'data':data})

def view_Complaint(request):
    data=Complaints.objects.all()
    return render(request,'admin_Temp/view_Complaint.html',{'data':data})

##################################################################################################################

def student_Temp(request):
    return render(request,'student_Temp/index.html')

def add_Complaints(request):
    form=ComplaintsForm()
    if request.method=='POST':
        form=ComplaintsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.student_name = request.user
            form.save()
            return redirect('view_Complaints')
    return render(request,'student_Temp/add_Complaints.html',{'form':form})

def view_Complaints(request):
    data=Complaints.objects.all()
    return render(request,'student_Temp/view_Complaints.html',{'data':data})

def view_Notifications(request):
    data=Notification.objects.all()
    return render(request,'student_Temp/view_Notifications.html',{'data':data})

def view_Students(request):
    data=Login.objects.all()
    return render(request,'student_Temp/view_Students.html',{'data':data})
