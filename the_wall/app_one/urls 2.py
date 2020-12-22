from django.urls import path
from . import views

urlpatterns = [
    path("", views.log_n_reg),
    path("register", views.register),
    path("the_wall", views.the_wall),
    path("login", views.login),
    path("logout", views.logout),
    path("process_post", views.process_post),
    path("add_like/<int:id>", views.add_like),
    path("add_dislike/<int:id>", views.add_dislike),
    path("add_comment/<int:id>", views.add_comment),
    path("add_comment_like/<int:id>", views.add_comment_like),
    path("add_comment_dislike/<int:id>", views.add_comment_dislike),
    path("delete_post/<int:id>", views.delete_post),
    path("delete_comment/<int:id>", views.delete_comment),
]