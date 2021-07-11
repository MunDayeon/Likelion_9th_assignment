from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from postcrud.models import Post
from commentcrud.models import Comment

def commentcreate(request, post_id):
    #수행 역할
    # 1. 처음 html에 들어갔을 때 빈 입력공간 띄우기 => GET 가져옴
    # 2. 이용자가 뭘 입력하면 그 입력값들 처리하기 => POST 처리
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('postshow', post_id=post.pk)
        else:
            redirect('list')
    else:
        form = CommentForm()
        return render(request, 'postshow.html', {'form':form, 'post':post})

def commentupdate(request, comment_id, post_id):
    comment = Comment.objects.get(id=comment_id)
    form = CommentForm(instance=comment)
    if request.method == "POST":
        update_form = CommentForm(request.POST, instance=comment)
        if update_form.is_valid():
            update_form.save()
            return redirect('postshow', post_id)
    return render(request, 'edit.html', {'form':form})

def commentdelete(request, comment_id, post_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('postshow', post_id)