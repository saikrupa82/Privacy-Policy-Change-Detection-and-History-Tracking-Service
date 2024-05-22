from django.urls import path
from django.contrib.auth import views as auth_views
from authen import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name="signup"),
    path('homepage/', views.homepage_view, name="homepage"),  # Ensure this matches the redirect call
    path('tracker/', views.tracker, name="tracker"), # Ensure this matches the redirect call
    path('trackingstatus/<str:string>/', views.trackingstatus_view, name='trackingstatus'),
]



# When passing 'auth/login.html' for template_name parameter, we tell auth.views.LoginView that the path will be used for login form 

# Using auth.views.LogoutView helps us handle logout request automatically, we only need to call {% url 'logout' %} where we want to make logout event in the HTML template.

