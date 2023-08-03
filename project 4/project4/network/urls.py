
from django.urls import path

from . import views

urlpatterns = [
    # index == all posts
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newpost", views.new_post, name="new_post"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("following", views.following_posts, name="following_posts"),
    
]

