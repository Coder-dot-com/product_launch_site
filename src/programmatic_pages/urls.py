from django.urls.conf import path
from . import views

urlpatterns = [
    path('templates/<slug>/', views.product_development_template, name="product_development_template"),

]