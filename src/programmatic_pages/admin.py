from django.contrib import admin

from .models import Keyword, ProductDevelopmentTemplate

# Register your models here.


class KeywordAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('keyword',)}
    list_display = ('keyword', 'slug', 'template_type')



class ProductDevelopmentTemplateAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'meta_description')


admin.site.register(Keyword, KeywordAdmin)
admin.site.register(ProductDevelopmentTemplate, ProductDevelopmentTemplateAdmin)