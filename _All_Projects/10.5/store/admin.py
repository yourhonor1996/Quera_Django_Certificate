from django.contrib import admin

from .models import Address, Category, Company, Product

class ProductInline(admin.StackedInline):
    '''Stacked Inline View for Product'''

    model = Product
    extra = 0

class ProductTabularInline(admin.TabularInline):
    '''Tabular Inline View for Product'''
    
    model = Product
    extra = 0



@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['postal_address', 'city']
    list_filter = ['city']
 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
 

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [ProductTabularInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'company', 'price']
    list_filter = ['category', 'company']
    sortable_by = ['price']
    list_display_links = ['id', 'name']
 
 
# Add the rest of admin models here
