from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.


class Postlist(generic.ListView):
    # model = Post // This displayed everything
    queryset = Post.objects.filter(status=1)
    # template = "post_list.html"