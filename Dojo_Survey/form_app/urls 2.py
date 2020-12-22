from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_survey),
    path('results', views.results),
    path('redir_funct', views.redir_funct),
]
