from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging #useful for debugging problems,checking what is code doing while running 
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator


#Static Demo data
# posts =[
#         {'id' : 1,'title' : 'post1', 'content' :'content of post1'},
#         {'id' : 2,'title' : 'post2', 'content' :'content of post2'},
#         {'id' : 3,'title' : 'post3', 'content' :'content of post3'},
#         {'id' : 4,'title' : 'post4', 'content' :'content of post4'},
#     ]

# Create your views here.
def index(request):
    blog_title = "Latest Posts"

    #getting data from the  postmodels
    all_posts=Post.objects.all()

    #pagination
    paginator = Paginator(all_posts,6)
    page_number = request.GET.get('page')
    page_obj =  paginator.get_page(page_number)


    return render(request,'blog/index.html',{'blog_title' : blog_title,'page_obj' : page_obj})


def detail(request,slug):
    # Static data 
    #post =  next((item for item in posts if item["id"]==int(post_id) ),None)# next function to return the item as the iteration reachs

    try:
        #getting post data by id from post model
       post = Post.objects.get(slug=slug)  #  lookup by slug
       related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)             #showing related posts

    except Post.DoesNotExist:
     
        raise Http404("Post Does Not exist ")
    
    #logger = logging.getLogger("TESTING")#general syntax with name Testing
    #logger.debug (f'post variable is {post}')
    return render(request, 'blog/detail.html', {'post': post,'related_posts' : related_posts})


def pazhaiya_url_redirect(request):
    return redirect(reverse('blog:puthu_url'))#reverse function for dynamic urls (not disturbing any url getting edited)

def puthu_url_paaru(request):
    return HttpResponse("This is a new URL")