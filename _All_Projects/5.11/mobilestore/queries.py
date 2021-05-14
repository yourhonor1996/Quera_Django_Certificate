from .models import Brand, Mobile
from django.db.models import F, Q, query


def all_brands_not_in_korea_china():
    query = Mobile.objects.exclude(made_in__in = ['Korea', 'China']).
    # query = Brand.objects.filter(~Q(nationality= 'Korea') & ~Q(nationality= 'China'))
    return query


def some_brand_mobiles(*brand_names):
    if len(brand_names) == 0:
        return Mobile.objects.all()
    query = Mobile.objects.filter(Q(brand__name__in = brand_names))
    return query

def mobiles_brand_nation_equals_made_in():
    query = Mobile.objects.filter(brand__nationality = F('made_in'))
    return query