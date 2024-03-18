from django.urls.conf import path
from . import views

urlpatterns = [
    path('templates/', views.product_development_template_listing_page, name="product_development_template_listing_page"),

    path('templates/<slug>/', views.product_development_template, name="product_development_template"),

]