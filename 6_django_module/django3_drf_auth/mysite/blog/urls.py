from django.urls import path

from blog import views

urlpatterns = [
    path('', views.PostListCreateView.as_view()),
    # path('gender-choices/', views.choices),
    path('<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view()),

    # path('all/', views.PostCRUDView.as_view()),
    # path('all/<int:pk>/', views.PostCRUDView.as_view()),
    #
    # path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    # path('<int:pk>/', views.PostDetailView.as_view(), name='detail')
]
