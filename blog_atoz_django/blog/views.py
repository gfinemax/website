from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    # template_name = 'blog/index.html'
    ordering = '-pk'

# FBV로 실습
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
    
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,    
#         }
#     )
    
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    
    return render(
        request,
        'blog/single_post_page.html',
        {
            'post':post,
        }
    )

