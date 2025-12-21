from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
def index(request):
    return render(request, "home/Index.html")
def contact(request):
    if request.method== "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if len(name)<2 or len(email)<10 or len(phone)<10 or len(message)<5:
            messages.error(request, "Plz Fill the form correctly !")
        else:
            contact= Contact(name=name,phone=phone,email=email,message=message)
            contact.save()
            messages.success(request, "Your meesage has been sent Successfully. ")
    return render(request, "home/Contact.html")
def about(request):
    return render(request, "home/About.html")
