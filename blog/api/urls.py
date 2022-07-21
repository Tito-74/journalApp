from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('details/', views.Blog_lists, name='details'),
    path('update_blog/<id>', views.update_Blog_list, name='update_blog'),
    path('delete_blog/<id>', views.delete_Blog, name='delete_Blog'),
    path('create_blog/', views.create_blog, name='create_blog'),
    
    path('category/', views.get_category_list, name='categories'),
    path('category/<id>', views.get_category, name='category'),
    path('create_category/', views.create_category, name='create_category'),
    path('update_category/<id>', views.update_category, name='update_category'),
    path('delete_category/<id>', views.delete_category, name='delete_category'),


    path('create_comment/', views.create_comment, name='create_comment'),
    path('comment/', views.get_comments_list, name='comments'),
    path('delete_comment/<id>', views.delete_comment, name='delete_comment'),

    
     path('likes/<id>', views.like_create_api, name='likes'),



    
]