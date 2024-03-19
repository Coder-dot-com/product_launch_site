"""
URL configuration for product_launch_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf.urls.static import static
from django.conf import settings

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.views.generic.base import TemplateView #import TemplateView
from . import views



from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap 
from programmatic_pages.sitemaps import TemplateListingPage, ProductDevelopmentTemplateArticleSitemap

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.sitemap_generator import Sitemap as wgsitemap

sitemaps = {
      'static':StaticSitemap, #add StaticSitemap to the dictionary
      'wagtail': wgsitemap,
      'TemplateListingPage': TemplateListingPage,
      'ProductDevelopmentTemplateArticleSitemap': ProductDevelopmentTemplateArticleSitemap,

}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  

    path('admin/1a/', admin.site.urls),

    path("", views.home, name="home"),
    
    re_path("robots.txt\/?$",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),  #add the robots.txt file
    path('emails/', include('emails.urls')),

    path('resources/', include('programmatic_pages.urls')),


    
    #wagtail keep at end due to wildcard
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('blog/', include(wagtail_urls)),
    path('', include(wagtail_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
