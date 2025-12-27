from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    sno = models.AutoField(primary_key= True) 
    title= models.CharField(max_length= 50)
    subtitle= models.CharField(max_length= 50)
    author= models.CharField(max_length= 50)
    slug= models.CharField(max_length= 25)
    views= models.IntegerField(default=0)
    image= models.ImageField(upload_to="posts/" )
    content= models.TextField()
    published_at = models.DateTimeField(auto_now_add= True, blank= True)
    def __str__(self):
        return self.title+ " by "+ self.author

class Comment(models.Model):
    sno= models.AutoField(primary_key= True)
    comment= models.TextField()
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    parent = models.ForeignKey('self', on_delete= models.CASCADE, null = True, blank=True,
        related_name='replies')
    time= models.DateTimeField(default= now)
    def __str__(self):
        return self.comment[0:13]+".... by "+ self.user.username+ " on "+ self.post.title