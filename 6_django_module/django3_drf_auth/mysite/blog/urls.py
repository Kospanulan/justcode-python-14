from django.urls import path

from blog import views

urlpatterns = [
    path('posts/', views.PostListCreateView.as_view()),
    path('posts/<int:post_id>/', views.PostRetrieveUpdateDestroyView.as_view()),

    path('posts/<int:post_id>/comments/', views.CommentsListView.as_view()),
    path('posts/<int:post_id>/categories/', views.CategoriesAddView.as_view()),
    path('posts/<int:post_id>/categories/alt/', views.CategoriesUpdateView.as_view()),

    path('categories/', views.CategoriesListCreateView.as_view()),
]
