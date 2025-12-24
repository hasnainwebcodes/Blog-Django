from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Comment
from django.contrib import messages 
def index(request):
    return HttpResponse("Hi")
def postview(request, slug):
    post= Post.objects.filter(slug=slug).first()
    comments= Comment.objects.filter(post=post)
    context= {'post': post, 'comments': comments}
    return render(request, "blog/Post.html", context)
def postComment(request):
    if request.method== "POST":
        comment= request.POST.get('comment')
        user= request.user
        sno= request.POST.get('postSno')
        post= Post.objects.filter(sno=sno).first()
        new = Comment(comment=comment,user=user,post=post)
        new.save()
        messages.success(request, "Your comment was posted Successfully")
    return redirect(f"/blog/{post.slug}")
