from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .models import Post
from .forms import CreatePostForm, CreateCommentForm


class IndexView(ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Post.objects.filter(Q(content__icontains=query)).order_by('-created_at')

    def post(self, request):
        form = CreatePostForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        
        self.object_list = self.get_queryset()
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreatePostForm()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'main/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all()
        context['comments'] = comments
        context['form'] = CreateCommentForm(post=post)
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CreateCommentForm(post=post, data=request.POST)
        if form.is_valid():
            form.instance.post = post
            form.save()
            return redirect('post-detail', pk=post.pk)
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)
