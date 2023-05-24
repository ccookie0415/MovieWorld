from django.urls import path
from . import views


urlpatterns = [
    path('myprofile/', views.my_profile),
    path('genres_movies/', views.genres_movies),
    path('new_kind_movies/', views.new_kind_movies),
    path('<int:user_id>/profile/', views.user_profile),
    path('<int:user_id>/profile/follow/', views.follow),

    # path('profiles/<int:user_id>/guestbook/', views.guestbook_list),
    path('profiles/<int:user_id>/guestbooks/', views.guestbook_create),
    path('profiles/<int:user_id>/guestbook/<int:guestbook_id>/', views.guestbook_detail),
]
