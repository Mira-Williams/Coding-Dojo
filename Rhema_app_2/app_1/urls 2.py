from django.urls import path
from . import views, initialize

urlpatterns = [
    path('', views.main),
    path('initialize', initialize.initialize),
    path('delete_all', views.delete_all),
    path('no_choice', views.no_choice),
]

