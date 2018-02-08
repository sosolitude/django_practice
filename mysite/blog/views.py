# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    #ctx={"posts":posts}
    return render(request, 'blog/post_list.html', {'posts':posts})

