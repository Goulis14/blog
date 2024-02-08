from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.db.models import Q


# Create your views here.
def post_list(request):
    cat = request.GET.get('cat', '')
    txt = request.GET.get('txt', '')
    try:
        cat = int(cat)
    except:
        cat = False

    if cat is False:
        if txt == '':
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        else:
            posts = Post.objects.filter((Q(text__contains=txt) | Q(
                title__contains=txt)) & Q(published_date__lte=
                                          timezone.now())).order_by('published_date')
    else:
        posts = (Post.objects.filter(published_date__lte=timezone.now())
                 .filter(category=cat).order_by('published_date'))

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def aboutus(request):
    return render(request, 'blog/aboutus.html')
