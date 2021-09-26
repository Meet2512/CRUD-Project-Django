from django.http.response import HttpResponseRedirect
from .forms import StudentRegistration
from django.shortcuts import redirect, render
from .models import student

# Create your views here.
#This is add function and display as well
def addshow(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():  
            nm = fm.cleaned_data['name'] 
            em = fm.cleaned_data['email'] 
            pw = fm.cleaned_data['password'] 
            reg = student(name =nm , email = em, password = pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = student.objects.all()   
    return render(request, 'enroll/addshow.html', {'form':fm, 'stu':stud})


#This is to edit/update

def update_d(request, id):
    if request.method == 'POST':
        pi = student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = student.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    
    return render(request, 'enroll/updateentry.html', {'form':fm})


# This function is for deleting

def delete_d(request, id):
    if request.method == 'POST':
        dele = student.objects.get(pk=id)
        dele.delete()
        return HttpResponseRedirect('/')