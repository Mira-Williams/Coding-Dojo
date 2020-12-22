from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page),
    path('register', views.register),
    path('login_user', views.login_user),
    path('main', views.main),
    path('logout', views.logout),
    path('create_book', views.create_book),
    path('book_page/<int:book_id>', views.book_page),
    path('add_to_favs/<int:book_id>', views.add_to_favs),
    path('del_from_favs/<int:book_id>', views.del_from_favs),
    path('only_favs', views.only_favs),
    path('edit_page/<int:book_id>', views.edit_page),
    path('edit_book/<int:book_id>', views.edit_book),
]