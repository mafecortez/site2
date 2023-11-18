from django.urls import path

from . import views

app_name = 'museus'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('search/', views.search_posts, name='search'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('create/', views.PostCreateView.as_view(), name='create'), 
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:post_id>/comment/', views.create_comment, name='comment'),
]
