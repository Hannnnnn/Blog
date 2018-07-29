from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from article.models import Article
from django.http import Http404

from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  #添加包


def home(request):
    post_list = Article.objects.all()

    return render(request, 'home.html', {'post_list' : post_list})


def detail(request,my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s"
           % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)

def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def detail(request,id):
    try:
        post = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list,
                                            'error' : False})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list})

