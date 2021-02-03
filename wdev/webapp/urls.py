from django.urls import path
from . import views


urlpatterns = [
    #path('socialmedia', views.socialmedia, name = 'socialmedia'), 
    path('shop', views.creat_card, name = 'card'),
    #path('order', views.order, name = 'order'),
    #path('freeproducts', views.freeproducts, name = 'freeproducts'),
    #path('blog', views., name = 'blog'), dont need blog
    #path('signup', views.signup, name = 'signup'),
    #path('login', views.login, name = 'login'),
    path('home', views.index, name = 'home'),# dont miss comma
]