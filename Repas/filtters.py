import django_filters

from .models import Repas , Repa

class RepasFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    keyword = django_filters.filters.CharFilter(field_name="name",lookup_expr="icontains")
    minPrice = django_filters.filters.NumberFilter(field_name="price" or 0,lookup_expr="gte")
    maxPrice = django_filters.filters.NumberFilter(field_name="price" or 100000,lookup_expr="lte")

    class Meta:
        model = Repas
    
        fields = ('category','keyword','minPrice','maxPrice')
class RepaFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    keyword = django_filters.filters.CharFilter(field_name="name",lookup_expr="icontains")
    minPrice = django_filters.filters.NumberFilter(field_name="price" or 0,lookup_expr="gte")
    maxPrice = django_filters.filters.NumberFilter(field_name="price" or 100000,lookup_expr="lte")

    class Meta:
        model = Repa
    
        fields = ('category','keyword','minPrice','maxPrice')