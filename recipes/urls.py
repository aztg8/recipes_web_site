from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/',
         sort_recipes_by_category_view,
         name="sort_by_category"),
    path('difficulty/<int:difficulty_id>/',
         sort_by_difficulty_view,
         name="difficulty"),
    path('recipe/<int:recipe_id>/',
         recipe_detail_view,
         name="recipe_detail"),
    path('about_us/',
         about_us_page_view,
         name="about_us"),
    path('our_team/',
         our_team_page_view,
         name="our_team"),
    path('services/',
         services_page_view,
         name="services"),
    path("search/",
         search_view,
         name="search"),
    path("login/",
         user_login_view,
         name='login'),
    path("registration/",
         user_registration_view,
         name='registration'),
    path('logout/',
         user_logout_view,
         name="logout"),
    path('profile/<int:user_id>/',
         check_profile_view,
         name="profile"),
    path('change_profile/<int:user_id>/',
         change_profile_data,
         name="change_profile"),
    path('add_recipe/',
         add_recipe_view,
         name="add_recipe"),
    path('update_recipe/<int:recipe_id>/',
         update_recipe_view,
         name="update_recipe"),
    path('delete_recipe/<int:recipe_id>/',
         delete_recipe_view,
         name="delete_recipe")
]