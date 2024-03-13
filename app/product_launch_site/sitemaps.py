from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import BlogPage

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return ['home', ]

    def location(self, item):
        return reverse(item)

