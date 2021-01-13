from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    url('images/', views.images, name = 'images'),
    url('', views.index, name='index'),
    url('search/', views.search_category_results, name = 'search_category_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
