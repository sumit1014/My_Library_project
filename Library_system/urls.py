from django.contrib import admin
from django.urls import path, include
from Library_system import views
app_name = 'Library_system'
urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('add_book/', views.add_book, name="add_book"),
    path('books_list/', views.books_list, name="books_list"),
    path('edit_books/', views.edit_books, name="edit_books"),
    path('delete<int:id>', views.delete_book, name="delete"),
    path('update<int:id>', views.update_book, name="update"),
    path('signup', views.user_signup, name="signup"),
    path('logins', views.user_login, name="logins"),
    path('logout', views.user_logout, name="logout"),
]
