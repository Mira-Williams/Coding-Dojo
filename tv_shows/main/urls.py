from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('add_form', views.add_form),
    path('add_show', views.add_show),
    path('single_show/<int:id>', views.single_show_page),
    path('edit_show_form/<int:id>', views.edit_show_form),
    path('update_show/<int:id>', views.update_show),
    path('delete_alert/<int:id>', views.delete_alert),
    path('delete_show/<int:id>', views.delete_show),
]
