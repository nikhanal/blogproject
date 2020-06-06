from django.shortcuts import render, get_object_or_404, redirect,reverse
from .models import Post, Author, PostView
from marketing.models import  Signup
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from django.db.models import Count, Q
from .forms import CommentForm


def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories'))
    return queryset

def index(request):
    featured = Post.objects.filter(feature = True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    content= {
        'object_list':featured,
        'latest':latest
    }
    return render(request,'index.html',context=content)

def blog(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    content = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
        'category_count': category_count
    }
    return render(request, 'blog.html', context=content)

def post(request, id):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post = get_object_or_404(Post, id = id)
    
    
    PostView.objects.get_or_create(user = request.user , post = post )

    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post-detail',kwargs={
                'id':post.pk
            }))
    content = {
        'form': form,
        'post':post,
        'most_recent': most_recent,
        'category_count': category_count
    }
    return render(request, 'post.html', context=content)
