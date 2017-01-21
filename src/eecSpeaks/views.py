from hknWebsiteProject import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from datetime import datetime

from .forms import BlogForm
from .models import Blog

# Create your views here.
def show_blogposts(request):
    blogs = Blog.objects.all()
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