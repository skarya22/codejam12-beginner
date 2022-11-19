import django_filters
from . models import Movie

class MovieFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Name')

    class Meta:
        model = Movie
        fields = ['name']
