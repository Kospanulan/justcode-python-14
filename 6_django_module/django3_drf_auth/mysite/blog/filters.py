from django_filters import rest_framework as filters

from blog.models import Post


def icontains_distinct(queryset, name, value):
    lookup = f"{name}__icontains"  # comments__content__icontains="vkopdfv"
    return queryset.filter(**{lookup: value}).distinct()
    # return queryset.filter(comments__content__icontains=value)


class PostFilter(filters.FilterSet):

    start_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    end_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")

    comment_contains = filters.CharFilter(field_name="comments__content", method=icontains_distinct)

    class Meta:
        model = Post
        fields = {
            'title': ['exact', 'contains', 'icontains'],
            'content': ['exact'],
        }

    # def filter_queryset(self, queryset):
    #     queryset = super().filter_queryset(queryset)
    #     return queryset.distinct()

