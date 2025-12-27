from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from math import ceil
import json
from MyBlog.models import Post

def index(request):
    posts= Post.objects.all()
    if len(posts) < 1:
        messages.warning(request, "No Posts Found !")
    page = request.GET.get('page')
    if not page or not page.isnumeric():
        page = 1
    else:
        page = int(page)

    per_page =10
    last = ceil(len(posts) / per_page)
    if page==last:
         posts = posts[(page-1)*per_page :]
    else:
         posts = posts[(page-1)*per_page : (page-1)*per_page + per_page]

    if page <= 1:
         prev = "#"
    else:
         prev = f"/?page={page - 1}"

    if page >= last:
         nex = "#"
    else:
         nex = f"/?page={page + 1}"
    return render(request, "home/Index.html", {"posts": posts, 'nex': nex , 'prev' : prev})
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
def search(request):
    query= request.GET.get('q')
    if len(query)>25:
        posts= Post.objects.none()
    else:
        posts= Post.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) |Q(subtitle__icontains=query))
        messages.success(request, f"Search results for: <strong>{query}</strong>")
        if len(posts) < 1:
            messages.warning(request, "No Search results Found plz refine your query !")
    page = request.GET.get('page')
    if not page or not page.isnumeric():
        page = 1
    else:
        page = int(page)

    per_page =15
    last = ceil(len(posts) / per_page)
    if page==last:
         posts = posts[(page-1)*per_page :]
    else:
         posts = posts[(page-1)*per_page : (page-1)*per_page + per_page]

    if page <= 1:
         prev = "#"
    else:
         prev = f"/?page={page - 1}"

    if page >= last:
         nex = "#"
    else:
         nex = f"/?page={page + 1}"
    return render(request, "home/Index.html", {"posts": posts, 'nex': nex , 'prev' : prev})
def login_user(request):
    if request.method =="POST":
        username= request.POST['name']
        logpassword= request.POST['password']
        user = authenticate(username= username, password= logpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully ")
            return redirect("index")
        else: 
            messages.error(request,"Invalid Credentials! Try again ")
            return redirect("index")
    return render(request, "blog/login.html")
def sign_up(request):
        if request.method == "POST":
            username= request.POST['name']
            email= request.POST['email']
            password= request.POST['password']
            if not username.isalnum() :
                messages.error(request,"Username must not have Symbols! ")
                return redirect("index")
            if len(password) < 5:
                messages.error(request,"Your password is too short! ")
                return redirect("index")
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                messages.success(request,"Your Icoder account created  Successfully ")
                return redirect("index")
            except Exception as e :
                messages.error(request,"An error occured while creating Account Try again with another username!")
                return redirect("index")
        else:
            return render(request, "blog/signup.html")
def logout_user(request):
    logout(request)
    messages.success(request,"Successfully Logged out ")
    return redirect("index")
    