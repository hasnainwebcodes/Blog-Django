from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index" ),
    path('contact/', views.contact,name="contact" ),
    path('about/', views.about,name="about" ),
    path('search', views.search,name="search" ),
    path('login/', views.login_user,name="login" ),
    path('logout/', views.logout_user,name="logout" ),
    path('SignUp/', views.sign_up,name="signup" ),

]