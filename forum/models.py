
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_description=models.TextField(blank=True, null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    submition_date=models.DateTimeField(auto_now_add=True)
    updation_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-submition_date']

    def __str__(self):
        return self.post_description

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_description=models.TextField(blank=True, null=True)
    commentor=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_posts',default=None)
    submit_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    likes=models.ManyToManyField(User,related_name='comment_likes',blank=True)
    class Meta:
        ordering=['-submit_date']

    def __str__(self): 
        return self.comment_description

