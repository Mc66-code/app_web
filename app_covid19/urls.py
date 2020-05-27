from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'^passion/', views.passion, name='passion'),
    path('prediction/', views.prediction, name='prediction'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







