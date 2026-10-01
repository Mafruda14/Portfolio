from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact

def home(request):
    #return HttpResponse('This is my homepage()')
    context = {'name': 'Mafruda Jaman'}
    return render(request, 'home.html', context)

def about(request):
    #return HttpResponse('This is my about page(about)')
    return render(request, 'about.html')

def project(request):
    #return HttpResponse('This is my project(project)')
    return render(request, 'project.html')

def certificate(request):
    #return HttpResponse('This is my project(project)')
    return render(request, 'certificate.html')    

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print('The data has been written to the db')

        

    #return HttpResponse('This is my contact(contact)') 
    return render(request, 'contact.html')           