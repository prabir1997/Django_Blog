from django.urls import path
from .views import HomePageView,CreatePostView,BlogDetailView,BlogUpdateView,BlogDeleteView


urlpatterns = [
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),

    path('<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'), # new
    path("",HomePageView.as_view(),name="home"),
    path("post/",CreatePostView.as_view(),name="add_post"),
    path('<int:pk>/', BlogDetailView.as_view(),
    name='post_detail'), # new
    


]
