from django.urls import path
from django.contrib.auth import views as auth_views


from django.urls import path
from .views import custom_logout

from . import views
app_name="accounts"
urlpatterns = [

    path("signup/",views.signup, name="signup"),
    path("profile/<slug:slug>",views.profile, name="profile"),

    

    path("accounts/login/", auth_views.LoginView.as_view(template_name="accounts/login.html")),

    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),




    path("accounts/logout/", custom_logout, name="logout"),
]






