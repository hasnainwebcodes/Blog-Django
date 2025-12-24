from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('postComment/', views.postComment, name="postComment"),
    path('', views.index, name="home"),
    path('<str:slug>/', views.postview, name="postview"),
]

