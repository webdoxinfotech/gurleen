from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    posts = Post.objects.all()
    print(posts)
    # return HttpResponse("hello")
    return render(request, "home.html", {'posts': posts})


def single(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, pk=id)
    return render(request, "single.html", {'post': post})


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")