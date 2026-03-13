from django.urls import path
from . import views

urlpatterns=[
    path("register/",views.register,name="register"),
    path("login/",views.login_view,name="login_view"),
    path("logout/",views.logout_view,name="logout_view"),
    path("home/",views.home,name="home"),
    path("profile/",views.profile,name="profile"),
    path("profile_edit/",views.edit_profile,name="edit_profile"),
    path("add_movie/",views.add_movie,name="add_movie"),
    path("movies_list/",views.movie_list,name="movie_list"),
    path("movie_detail/<int:id>",views.movie_detail,name="movie_detail"),
    path("edit_movie/<int:id>",views.edit_movie,name="edit_movie"),
    path("delete_movie/<int:id>",views.delete_movie,name="delete_movie"),
    path("my_movies/",views.my_movies,name="my_movies"),
    path("category_movies/<int:id>",views.category_movies,name="category_movies"),
    path("search/",views.search_movies,name="search_movies"),
    
]

