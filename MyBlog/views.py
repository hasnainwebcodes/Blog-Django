from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Comment
from django.contrib import messages 
def index(request):
    return HttpResponse("Hi")
def postview(request, slug):
    post= Post.objects.filter(slug=slug).first()
    post.views= post.views +1 
    post.save()
    comments = Comment.objects.filter(
    post=post,
    parent=None
    ).order_by('-time')

    context= {'post': post, 'comments': comments, "user": request.user}
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
def postReply(request):
    if request.method == "POST":
        comment_text = request.POST.get("comment")
        parentSno = request.POST.get("parentSno")
        postSno = request.POST.get("postSno")

        post = Post.objects.get(sno=postSno)
        parent = Comment.objects.get(sno=parentSno)

        Comment.objects.create(
            comment=comment_text,
            user=request.user,
            post=post,
            parent=parent
        )
        messages.success(request,"Your reply added ")

    return redirect(request.META.get('HTTP_REFERER'))

