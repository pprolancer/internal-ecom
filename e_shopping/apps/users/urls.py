from django.conf.urls import include, url
from django.contrib import admin
from users.views import (
    RegisterView, LoginView, LogoutView)
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [

	url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', RegisterView.as_view(), name="user-register"),
    url(r'^accounts/login/$', LoginView.as_view(), name="user-login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    
]

if settings.DEBUG:
    urlpatterns += [

        url(r'^media/(.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    ]