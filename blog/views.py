from datetime import date
from django.shortcuts import render
from .models import Post, Author, Tag


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "posts": all_posts
    })


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": post,
        "post_tags": post.tags.all()
    })
