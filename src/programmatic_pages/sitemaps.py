from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import BlogPage
from .models import ProductDevelopmentTemplate

class TemplateListingPage(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = 'https'

    def items(self):
        return ['product_development_template_listing_page', ]

    def location(self, item):
        return reverse(item)



# Example dynamic sitemap with models
class ProductDevelopmentTemplateArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6  
    protocol = 'https'

    def items(self):
        return ProductDevelopmentTemplate.objects.all()

        
    def location(self,obj):
        return '/resources/templates/%s' % (obj.keyword.slug)