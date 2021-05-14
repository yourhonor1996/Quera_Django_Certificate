# Import stuff
from .models import Brand, Mobile
from django.db.models import Sum, Min, Max, Avg
def total_value_of_products():
    query = Mobile.objects.aggregate(total_value= Sum('price'))
    return query


def total_value_of_products_with_brand_of(brand_name):
    query = Mobile.objects.filter(brand__name= brand_name).aggregate(total_value= Sum('price'))
    return query


def most_expensive_cheapest_price_with_nationality_of(nationality):
    query = Mobile.objects.filter(brand__nationality= nationality).aggregate(cheap= Min('price'), expensive= Max('price'))
    return query


def display_size_avg_in_available_mobiles_between_price(minimum, maximum):
    query = Mobile.objects.filter(price__gte= minimum, price__lte= maximum, is_available= 1).aggregate(avg= Avg('display_size'))
    return query
