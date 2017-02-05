from hknWebsiteProject import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from datetime import datetime

from .forms import BlogForm
from .models import Blog

# Create your views here.
def show_blogposts(request):
    # TODO: add pagination
    blogs = Blog.objects.order_by('-pk')
    context = {
        'blogs' : blogs
    }
    return render(request, "eecSpeaks/show_blogposts.html", context)

@login_required()
def add_blogpost(request):
    context = {}
    if not request.user.is_superuser:
        context = {
            'error': True,
            'error_msg': 'You do not have permission to access this page'
        }
    else:
        form = BlogForm(request.POST or None)
        context = {
            'form': form
        }
        if request.POST:
            if form.is_valid():
                blog = form.save(commit=False)
                blog.publicationDate = datetime.now()
                blog.save()

                return redirect('/eecspeaks')

    return render(request, "eecspeaks/add_blogpost.html", context)

def view_post(request, blogid):
    b = Blog.objects.get(pk=blogid)
    context = {
        'blog': b
    }
    return render(request, "eecspeaks/show_post.html", context)

@login_required()
def edit_post(request, blogid):
    if not request.user.is_superuser:
        context = {
            'error': True,
            'error_msg': 'You do not have permission to access this page'
        }
    b = Blog.objects.get(pk=blogid)
    if request.POST:
        form = BlogForm(request.POST, instance=b)
        if form.is_valid():
            form.save()
            return redirect('eecspeaks/blog/%s/'%blogid)
    form = BlogForm(instance=b)
    context = {
        'form': form
    }
    return render(request, "eecspeaks/edit_blogpost.html", context)
