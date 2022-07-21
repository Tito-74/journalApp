from django.urls import path
from . import views
from .serializers import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



app_name = 'accounts'
urlpatterns = [ 
    # path('details/', views.Blog_lists, name='details'),
    # path('update_blog/<id>', views.update_Blog_list, name='update_blog'),
    # path('delete_blog/<id>', views.delete_Blog, name='delete_Blog'),
    path('register/', views.register_views, name='register'),
     path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]