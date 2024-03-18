from django.contrib import admin

from .models import Keyword, ProductDevelopmentTemplate, FAQQuestionProductDevelopmentTemplate

# Register your models here.


class KeywordAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('keyword',)}
    list_display = ('keyword', 'slug', 'template_type')

class ProductDevelopmentFAQInline(admin.TabularInline):
    model = FAQQuestionProductDevelopmentTemplate
    extra = 1

class ProductDevelopmentTemplateAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'meta_description',)
    inlines = [ProductDevelopmentFAQInline]

class FAQQuestionProductDevelopmentTemplateAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')

admin.site.register(Keyword, KeywordAdmin)
admin.site.register(ProductDevelopmentTemplate, ProductDevelopmentTemplateAdmin)
admin.site.register(FAQQuestionProductDevelopmentTemplate, FAQQuestionProductDevelopmentTemplateAdmin)