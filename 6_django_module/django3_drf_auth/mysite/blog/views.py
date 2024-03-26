from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    lookup_field = 'pk'

# Pillow
# cv2 - opencv-python


@api_view(['GET'])
def choices(request):

    gender_choices = dict(Post.GENDERS)
    print(gender_choices)

    return Response({"choices": gender_choices})


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


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
    """
    Retrieve - Чтение одной записи по айди - GET
    List - чтение списка записей - GET
    Create - создание
    Destroy - Удаление
    Update - обновление по айди

    """
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
