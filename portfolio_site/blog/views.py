from django.shortcuts import render, get_object_or_404 
from .models import Post

# Create your views here.
def post_list(request):
    posts= Post.objects.filter(published_status= True).order_by("-date_created")
    context = {
        "posts": posts
    }
    if not posts.exists():
        pass
    
    return render(request,"blog/list.html",context)

def post_detail(request, slug):
    post= get_object_or_404(Post,slug=slug, published_status= True)
    context= {
        "post": post
    }

    return render(request, "blog/detail.html", context)