from django.urls import path
from .views import *

urlpatterns = [
    path("", posts_list, name="posts_list_url"),
    path("post/<str:slug>/", post_deail, name="post_detail_url"),
    path("tags/", tags_list, name="tags_list_url"),
    path("tag/<str:slug>", tag_detail, name="tag_detail_url")
]