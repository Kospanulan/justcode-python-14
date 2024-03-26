from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.forms import CreatePostForm, LoginForm
from blog.models import Post


# views - Представления
# templates - Шаблоны
# urls - ссылки


class PostListView(ListView):

    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')


    # def get(self, request):
    #     posts = Post.objects.all().order_by('-created_at')
    #
    #     context = {
    #         'all_posts': posts
    #     }
    #
    #     return render(request, 'blog/index.html', context)


@login_required
def index(request):  # PostListView
    posts = Post.objects.all().order_by('-created_at')
    # template = loader.get_template('blog/index.html')

    context = {
        'all_posts': posts
    }

    # return HttpResponse(template.render(context, request))

    return render(request, 'blog/index.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self):
        post_id = self.kwargs.get('post_id')
        return Post.objects.get(pk=post_id)


def detail(request, post_id):  # PostDetailView
    p = Post.objects.get(id=post_id)
    return HttpResponse(f"<h1> id: {p.id}. {p.title} </h1>"
                        f"<p> {p.content} test </p>")


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('index')
    form_class = CreatePostForm

    def form_valid(self, form):
        print("form instance", form.instance.id)
        form.instance.author_id = 1
        return super().form_valid(form)


def new_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.author_id = 1
            post.save()

            return redirect("index")
        else:
            return HttpResponse('Error creating!')

    # GET
    context = {
        'form': CreatePostForm()
    }

    return render(request,
                  'blog/create_post.html',
                  context=context)

# def posts(request):
#     post_id = request.GET.get('id', 1)
#     p = Post.objects.get(id=post_id)
#     return HttpResponse(f"<h1> id: {p.id}. {p.title} </h1>"
#                         f"<p> {p.content} test </p>")

# def index(request):
#     posts = Post.objects.all().order_by('-created_at')
#     response = (f"<ul>"
#                 f"{ ''.join([f'<li>{post.title}</li>' for post in posts]) }"
#                 f"</ul>")
#     return HttpResponse(response)



# class LoginView(FormView):
#
#     model = get_user_model()
#     template_name = 'blog/login.html'
#     context_object_name = 'user'
#
#     def get_queryset(self):
#         return Post.objects.all().order_by('-created_at')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

            return redirect("index")
        else:
            return HttpResponse('Error creating!')

    context = {
        'form': LoginForm()
    }

    return render(request,
                  'blog/login.html',
                  context=context)











def home(request):
    posts = Post.objects.all()
    context = {
        'my_posts': posts
    }
    return render(request, 'blog/home.html', context=context)

    # result = ""

    # for post in posts:
    #     result += (f"<h1>{post.title}</h1>"
    #                f"<p>{post.id}. {post.content}...</p></br>")

    # return HttpResponse(result)


def get_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'my_post': post
    }
    return render(request,
                  'blog/post.html',
                  context=context)
    # return HttpResponse(f"<h1>{post.title}</h1>"
    #                     f"<p>{post.content}...</p>")























































