from django.shortcuts import render
from django.db.models import Q

from .models import Post


def index(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''

    posts = Post.objects.filter(
        Q(content__icontains=query)
    )

    context = {
        'posts': posts
    }
    return render(request, 'main/index.html', context)


def post_detail(request, id):
    post = Post.objects.get(pk=id)
    comments = post.comments.all()
    # comments_count = comments.count()

    context = {
        'post': post,
        'comments': comments,
        # 'comments_count': comments_count,
    }
    return render(request, 'main/post-detail.html', context)