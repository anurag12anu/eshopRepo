from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path(' ', views.index, name='homepage'),  # Root URL mapped to 'home' view
    path('home', views.index),  # Explicit home page route
    path('signup', views.signup, name='signup'),   # Sign up route
    path('signin', views.signin),  # Sign in route
    path('logout', views.logout),  # Logout route
]
