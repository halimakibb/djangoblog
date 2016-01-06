from django.shortcuts import render
from .models import Post 

def index(request):
    posts = Post.objects.order_by('updated')
    context_dict = {'posts': posts}
    return render(request, 'blog/index.html', context_dict)