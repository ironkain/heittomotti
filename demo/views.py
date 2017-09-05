from django.shortcuts import render

# Create your views here.

from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

#def post_list(request):
#    return render(request, 'blog/post_list.html', {})

def demo_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'demo/home.html', {})

def tilaaminen(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'demo/tilaaminen.html', {})

def kuvat(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'demo/kuvat.html', {})

def videot(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'demo/videot.html', {})

def tuoteinfo(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'demo/tuoteinfo.html', {})

def toimitusalueet(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'demo/toimitusalueet.html', {})

def palvelut(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'demo/palvelut.html', {})

def yhteystiedot(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'demo/yhteystiedot.html', {})

def hinnasto(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'demo/hinnasto.html', {})

