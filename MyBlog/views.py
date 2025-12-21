from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Hi")
def postview(request, slug):
    return render(request, "blog/Post.html")