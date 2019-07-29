from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request, 'blog/home.html', {'posts_lists':posts})

def new(request):
    if request.method=='POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.published_date=timezone.now()
            post.author=request.user
            post.save()
            return redirect('home')
    else:
        form=PostForm()
    return render(request, 'blog/new.html', {'form':form})

def post_detail(request, index):
    post=get_object_or_404(Post, pk=index)
    if request.method =='POST':
        form=CommentForm(request.POST)
        if form.is_valid:
            comment=form.save(commit=False)
            comment.author=request.user
            comment.post=post
            comment.save()
            return redirect('post_detail', index=post.pk)
    else:
        form=CommentForm()
        comments=Comment.objects.filter(post=post)
        return render(request, 'blog/post_detail.html', {'form':form, 'post':post, 'comments':comments})
 
def post_edit(request, index):
    post=get_object_or_404(Post, pk=index)
    if request.method =='POST':
        form=PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.published_date=timezone.now()
            post.author=request.user
            post.save()
            return redirect('post_detail', index=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    
def post_delete(request, pk):
     post=get_object_or_404(Post, pk=pk)
     post.delete()
     return redirect('home')
     
def comment_edit(request, index, cindex):
    comment=get_object_or_404(Comment, pk=cindex)
    post=get_object_or_404(Post, pk=index)
    if request.method=='POST':
        form=CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.save()
            return redirect('post_detail', index=post.pk)
    else:
        form=CommentForm(instance=comment)
        return render(request,'blog/comment_edit.html', {'form':form })

def comment_delete(request, index, cindex):
    comment=get_object_or_404(Comment, pk=cindex)
    post=get_object_or_404(Post, pk=index)
    comment.delete()
    return redirect('post_detail', index=post.pk)