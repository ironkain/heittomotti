from django.shortcuts import render

# Create your views here.

from .models import Tilaus
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from time import gmtime, strftime

#def post_list(request):
#    return render(request, 'blog/post_list.html', {})

def demo_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'demo/home.html', {})

def tilaaminen(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.title = post.nimi + ' : ' + str(strftime("%Y-%m %d %H:%M:%S", gmtime()));
            post.save()
            #return redirect('post_detail', pk=post.pk)

            try:
                import smtplib
                from email.MIMEMultipart import MIMEMultipart
                from email.MIMEText import MIMEText
                from email.MIMEBase import MIMEBase
                from email import encoders
                from email.mime.multipart import MIMEMultipart
                msg = MIMEMultipart()
                msg['From'] = 'myynti@heittomotti.fi'
                msg['To'] = 'ismo.ronkainen@gmail.com'
                msg['Subject'] = "Klapitilaus : " + post.nimi
                body = post.nimi + "\n" + post.osoite + "\n" + post.puhelin + "\n" + post.sposti + "\n" + post.koivuklapeja + " heittomottia"
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('localhost')
                server.sendmail('myynti@heittomotti.fi','ismo.ronkainen@gmail.com',msg.as_string())
                server.quit()
            except:
                pass

            return render(request, 'demo/kiitos.html', {})
    else:
        form = PostForm()
    return render(request, 'demo/tilaaminen.html', {'form': form})

def tilaus(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
            return render(request, 'demo/home.html', {})
    else:
        form = PostForm()
    return render(request, 'demo/tilaus.html', {'form': form})

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

