from django.urls import path

from blog import views
from blog.views import PostListView, PostDetailView, PostCreateView

# localhost:8000/posts/
urlpatterns = [
    # path('', PostListView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('new/', PostCreateView.as_view(), name="create"),
    path('login/', views.login_view, name="login"),
    # path('test/', views.test_view),
    path('<int:post_id>/', PostDetailView.as_view(), name="detail"),

    # path('home/', views.home),  # localhost:8000/posts/home/
    # path('home/<int:post_id>/', views.get_post)  # localhost:8000/posts/home/
]

#  http://127.0.0.1:8000/blog/posts/?id=1
#  http://127.0.0.1:8000/blog/posts/2/