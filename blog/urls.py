from django.urls import path
from . import views
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [path('', views.post_list, name='post_list'),
               path('post/<int:pk>/', views.post_detail, name='post_detail'),
               path('aboutus',views.aboutus,name='aboutus')]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
