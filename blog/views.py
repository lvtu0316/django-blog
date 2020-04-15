import re

import markdown
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from markdown.extensions.toc import  TocExtension
from pure_pagination import PaginationMixin

from blog.models import Post, Category, Tag


class IndexView(PaginationMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 10
# def index(request):
#     post_list = Post.objects.all().order_by('-created_at')
#     return render(request, 'blog/index.html', locals())


class ArchiveView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchiveView, self).get_queryset().filter(created_at__year=year, created_at__month=month)

# def archive(request, year, month):
#     post_list = Post.objects.all().filter(created_at__year=year,
#                                           created_at__month=month).order_by('-created_at')
#     return render(request, 'blog/index.html', locals())
#


class CategoryView(IndexView):
    def get_queryset(self):

        category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=category)


# def category(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     post_list = Post.objects.filter(category=category).order_by('-created_at')
#     return render(request, 'blog/index.html', context={'post_list': post_list})


class TagView(IndexView):
    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)


# def tag(request, pk):
#     tag = get_object_or_404(Tag, pk=pk)
#     post_list = Post.objects.filter(tags=tag).order_by('-created_at')
#     return render(request, 'blog/index.html', context={'post_list': post_list})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/show.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response


# def show(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.increase_views()
#     return render(request, 'blog/show.html', context={'post': post})


def search(request):
    q = request.GET.get('q')

    if not q:
        error_msg = "请输入搜索关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('blog:index')

    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'post_list': post_list})


def about(request):
    return render(request, 'blog/about.html')


