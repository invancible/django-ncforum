from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger

from .models import Post
from .forms import CreatePostForm, CreateCommentForm


class IndexView(ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        queryset = Post.objects.filter(Q(content__icontains=query)).order_by('-created_at')
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get('page')
        # return paginator.get_page(page_number)
        print(f"Number of results per page: {len(paginator.get_page(page_number))}")
        print(paginator.get_page(page_number).has_other_pages)    
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.get_page(1)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)

        return queryset

    def post(self, request):
        form = CreatePostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            
            image = request.FILES.get('image')
            print(image)
            if image:
                post.image = image
            
            post.save()

            return HttpResponseRedirect('/')
        
        self.object_list = self.get_queryset()
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreatePostForm()
        context['page_obj'] = self.get_queryset()
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
