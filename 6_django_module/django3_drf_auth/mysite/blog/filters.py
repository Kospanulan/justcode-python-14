from django_filters import rest_framework as filters

from blog.models import Post


class PostFilter(filters.FilterSet):

    test_contains = filters.CharFilter(field_name="title", lookup_expr="icontains")
    test_exact = filters.CharFilter(field_name="title", lookup_expr="iexact")

    # min_age = filters.NumberFilter(field_name='age', lookup_expr="gte")
    # max_age = filters.NumberFilter(field_name='age', lookup_expr="lte")

    # start_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    # end_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")

    comment_contains = filters.CharFilter(field_name="comments__content", lookup_expr="icontains")

    class Meta:
        model = Post
        # fields = ['title', 'content']
        fields = {
            'title': ['exact', 'contains', 'icontains'],
            'content': ['exact'],
            'created_at': ['gte', 'lte'],
            # 'age': ['gte', 'lte']
        }


