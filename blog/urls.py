from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url, include
from posts.views import index, blog, post



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='post-list'),
    path('blog/', blog, name='post-list'),
    path('post/<id>/', post, name='post-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)