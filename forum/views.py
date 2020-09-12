from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
 
# Create your views here.
def landing(request):
    return render(request,'mainlanding.html')

def forummain(request):
    post=Post.objects.all()
    return render(request,'mainpage.html',{'post':post})

def displaycomments(request,id):
    post=Post.objects.get(id=id)
    comment_details=Comment.objects.filter(post=post)
    return render(request,'comments.html',{'comment_details':comment_details})

def postnew(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = Post()
            obj.post_description = form.cleaned_data['post_description']
            obj.author=request.user
            obj.save()
            return redirect('/')
    else:
        form=PostForm()
        return render(request,'postform.html',{'form':form})

def commentnew(request,id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = Comment()
            obj.post=Post.objects.get(id=id)
            obj.comment_description = form.cleaned_data['comment_description']
            obj.commentor=request.user
            obj.save()
            return redirect('/')
    else:
        form=CommentForm()
        return render(request,'commentform.html',{'form':form})

def myposts(request):
    post=Post.objects.filter(author=request.user)
    return render(request,'myposts.html',{'post':post})

def mycomments(request):
    comment=Comment.objects.filter(commentor=request.user)
    return render(request,'mycomments.html',{'comment':comment})

def editpost(request,id):
    post=Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.post_description = form.cleaned_data['post_description']
            post.save()
            return redirect('/')
    else:
        form=PostForm()
        return render(request,'editpostform.html',{'form':form})

def editcomment(request,id):
    comment=Comment.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.comment_description = form.cleaned_data['comment_description']
            comment.save()
            return redirect('/')
    else:
        form=CommentForm()
        return render(request,'editcommentform.html',{'form':form})

def deletepost(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('/')

def deletecomment(request,id):
    comment=Comment.objects.get(id=id)
    comment.delete()
    return redirect('/')

"""def like_comment(request,id):
    comment=Comment.objects.get(id=id)
    post=comment.post
    comment.likes.add(request.user)
    return redi"""
