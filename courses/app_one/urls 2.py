from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('comments/<int:id>', views.comments_page),
    path('comments/<int:id>/create', views.create_comment),
    path('create_course', views.create_course),
    path('delete_alert/<int:id>', views.delete_alert),
    path('delete_course/<int:id>', views.delete_course),
]
