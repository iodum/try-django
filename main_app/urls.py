from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^treasures/([a-z0-9-]+)/$', views.detail, name='detail'),
    url(r'^post_url/$', views.post_treasure, name='post_treasure'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^like_treasure/$', views.like_treasure, name='like_treasure'),
    url('', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
    ]
