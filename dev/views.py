from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

#def post_list(request):
#    return render(request, 'blog/post_list.html', {})

def dev_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'dev/dev_list.html', {})
