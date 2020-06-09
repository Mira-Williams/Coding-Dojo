from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('cave', views.cave),
    path('castle', views.castle),
    path('ship', views.ship),
    path('casino', views.casino),
    path('reset', views.reset),
]
