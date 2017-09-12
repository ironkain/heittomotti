from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.demo_list, name='demo_list'),
    url(r'^www.heittomotti.fi$', views.demo_list, name='demo_list'),
    url(r'^tilaaminen$', views.tilaaminen, name='tilaaminen'),
    url(r'^tilaus$', views.tilaus, name='tilaus'),
    url(r'^kuvat$', views.kuvat, name='kuvat'),
    url(r'^videot$', views.videot, name='videot'),
    url(r'^tuoteinfo$', views.tuoteinfo, name='tuoteinfo'),
    url(r'^toimitusalueet$', views.toimitusalueet, name='toimitusalueet'),
    url(r'^palvelut$', views.palvelut, name='palvelut'),
    url(r'^hinnasto$', views.hinnasto, name='hinnasto'),
    url(r'^yhteystiedot$', views.yhteystiedot, name='yhteystiedot'),
    url(r'^puh$', views.puh, name='puh'),
]
