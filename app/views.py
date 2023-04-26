from django.shortcuts import render

# Create your views here.
from app.models import *
from .forms import *

def Student(request):
    SFO=StudentForms()
    d={'SFO':SFO}
    if request.method=='POST':
        SOQ=StudentForms(request.POST)
        # print(request.POST)
        if SOQ.is_valid():
            # print(SOQ.cleaned_data)
            name=SOQ.cleaned_data['name']
            sid=SOQ.cleaned_data['sid']
            age=SOQ.cleaned_data['age']
            email=SOQ.cleaned_data['email']
            password=SOQ.cleaned_data['password']
            # SO=Students.objects.all()
            CR=Students.objects.get_or_create(sid=sid,name=name,age=age,email=email,password=password)[0]
            CR.save()
            SO=Students.objects.all()
            d1={'SO':SO}
            return render(request,'display_student.html',d1)

    return render(request,'StudentForm.html',d)