
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from peopleIn.views import UserCreateView, UserCreateDoneTV
from . import views
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings                         # 추가 1

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    # 계정 가입 처리하는 URL
    re_path(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    # 계정 가입 완료될 때 보여줄 URL
    re_path(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),
    url(r'^admin/', admin.site.urls, name='admin'),
    path('', views.IndexView.as_view(), name='index'),
    path('notice/', include('notice.urls')),
    path('franchise/', include('notice.urls')),
    path('map/', include('map.urls')),
    path('forSale/', include('forSale.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:                                       # 추가 2
    import debug_toolbar                                 # 추가 2
    urlpatterns += [                                     # 추가 2
        path('__debug__/', include(debug_toolbar.urls)), # 추가 2
    ]                                                    # 추가 2


