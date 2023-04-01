from django.urls import path
from Posts.views import home, post, create_post


urlpatterns = [
    path('pages/', home, name="home"),
    path('pages/<int:post_id>/', post, name="post"),
    path('pages/create_post/', create_post, name="CreatePost"),

]
