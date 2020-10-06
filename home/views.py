from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'message':'Welcome ,Guest User',
        'dob':'Your date of birth is 12-06-1991'
    }
    #return HttpResponse("This is home page")
    return render(request,'index.html',context)

def about(request):
   # return HttpResponse("This is about page")
    return render(request,'about.html')
def services(request):
   # return HttpResponse("This is services page")
    return render(request,'services.html')
def contact(request):
    #return HttpResponse("This is contact page")
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,phone=contact,message=message,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message have been sent.')
    return render(request,'contact.html')
