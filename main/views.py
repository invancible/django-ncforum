from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.db.models import Q
from django.views.generic.base import TemplateView

from .models import Post
from .forms import CreatePostForm, CreateCommentForm


def index(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''

    posts = Post.objects.filter(
        Q(content__icontains=query)
    )

    if request.method == 'POST':
        form = CreatePostForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        
    else:
        form = CreatePostForm()

    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'main/index.html', context)


def post_detail(request, id):
    post = Post.objects.get(pk=id)
    comments = post.comments.all()
    # comments_count = comments.count()

    if request.method == 'POST':
        form = CreateCommentForm(post, request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', id=post.id)
    else: 
        form = CreateCommentForm(post)

    context = {
        'post': post,
        'comments': comments,
        'form': form,
        # 'comments_count': comments_count,
    }
    return render(request, 'main/post-detail.html', context)
