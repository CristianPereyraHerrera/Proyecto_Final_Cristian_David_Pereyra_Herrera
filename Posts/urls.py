from django.urls import path
from .views import home, post, create_post, update_post, delete_post

urlpatterns = [
    path('pages/', home, name="home"),
    path('pages/<int:post_id>/', post, name="post"),
    path('pages/create_post/', create_post, name="CreatePost"),
    path('pages/update_post/<int:post_id>/', update_post, name="UpdatePost"),
    path('delete-post/<int:post_id>/', delete_post, name="DeletePost"),
]
