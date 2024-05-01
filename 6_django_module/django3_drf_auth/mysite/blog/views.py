from django.db.models import Count
from django.shortcuts import get_object_or_404

from rest_framework import generics, mixins, permissions, viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.filters import PostFilter
from blog.models import Post, Comment, Category
from blog.permissions import DjangoModelPermissionsWithRead
from blog.serializers import PostListCreateSerializer, PostRetrieveUpdateDestroySerializer, CommentSerializer, \
    CategoriesSerializer


# class CustomPageNumberPagination(PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 5
#
#     def get_paginated_response(self, data):
#         return Response(data)


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostListCreateSerializer
    filter_backends = []

    def get_queryset(self):
        queryset = (Post.objects.all()
                    .annotate(comments_count=Count('comments'))
                    .order_by('-created_at'))
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveUpdateDestroySerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs['post_id'])
        self.check_object_permissions(self.request, obj)
        return obj


class CommentsListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = (
            Comment.objects.all()
            .filter(post_id=self.kwargs['post_id'])
            .order_by('-created_at')
        )
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs['post_id']
        )


class CategoriesListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesAddView(APIView):

    def post(self, request, *args, **kwargs):
        categories_ids = request.data.get('categories')
        post_id = kwargs.get('post_id')

        post = Post.objects.get(id=post_id)
        post.categories.add(*categories_ids)

        return Response({"detail": "Categories added to post successfully"})


class CategoriesUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveUpdateDestroySerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs['post_id'])
        self.check_object_permissions(self.request, obj)
        return obj

"""
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    lookup_field = 'pk'


@api_view(['GET'])
def choices(request):

    gender_choices = dict(Post.GENDERS)
    print(gender_choices)

    return Response({"choices": gender_choices})






class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [permissions.DjangoModelPermissions]

    lookup_field = 'pk'


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [permissions.DjangoModelPermissions]

    lookup_field = 'pk'


class PostCRUDView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    Retrieve - Чтение одной записи по айди - GET
    List - чтение списка записей - GET
    Create - создание
    Destroy - Удаление
    Update - обновление по айди

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):  # keyword arguments
        print("kwargs: ", kwargs)
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # kwargs['partial'] = True
        # return self.update(request, *args, **kwargs)
        return self.partial_update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author_id=3)







# class PostCreateView(generics.CreateAPIView):
#     serializer_class = PostSerializer
#
#     def perform_create(self, serializer):
#         # title = serializer.validated_data.get('title')
#         # content = serializer.validated_data.get('content', None)
#         # if content == "":
#         #     content = title
#
#         serializer.save(author_id=1)
#
#
# class PostListView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer






"""

# @api_view(['GET', 'POST'])
# def index(request):
#
# if request.method == 'POST':
#     # print(request.POST)
#     print(request.data)
#     instance = PostSerializer(data=request.data)
#
#     if instance.is_valid(raise_exception=True):
#         instance.save()
#         # post.author_id = 1
#         # post.save()
#         return Response(instance.data, status=status.HTTP_201_CREATED)
# return Response({"detail": "Error creating", "status": status.HTTP_400_BAD_REQUEST})
#
#     elif request.method == 'GET':
#         post_id = request.GET.get('post_id')
#         if post_id is not None:
#             post = Post.objects.get(pk=post_id)
#             if post:
#                 instance = PostSerializer(post)
#                 return Response(instance.data)
#
#             return Response({"detail": "Post does not exist", "status": status.HTTP_404_NOT_FOUND})
#         else:
#             posts = Post.objects.all()
#             if posts:
#                 instance = PostSerializer(posts, many=True)
#                 return Response(instance.data)
