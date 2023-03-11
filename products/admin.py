from django.contrib import admin
from .models import *

# Register your models here.

class ColorInline(admin.TabularInline):
    model = ProductColors
    extra = 3


class ProductImageInline(admin.TabularInline):
    model = ProductImages
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_added','name', 'price')
    ordering = ('-date_added',)
    search_fields = ('pk', 'name',)
    inlines = [ColorInline,ProductImageInline]
    
admin.site.register(Product,ProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category')
    ordering = ('-date_added',)
    search_fields = ('pk', 'category',)
    
admin.site.register(Category,ProductCategoryAdmin)


class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'sub_category')
    ordering = ('-date_added',)
    search_fields = ('pk', 'sub_category',)
    
admin.site.register(SubCategory,ProductSubCategoryAdmin)


class ProductCompanyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    ordering = ('-date_added',)
    search_fields = ('pk', 'name',)
    
admin.site.register(Company,ProductCompanyAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display = ('pk',)
    ordering = ('-date_added',)
    search_fields = ('pk',)
    
admin.site.register(Banners,BannerAdmin)



