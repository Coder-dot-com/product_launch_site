from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Keyword, ProductDevelopmentTemplate

# Create your views here.


def product_development_template(request, slug):
    keyword = get_object_or_404(Keyword, slug=slug)

    template = get_object_or_404(ProductDevelopmentTemplate, keyword=keyword)

    context = {'template': template}

    return render(request, 'product_development_template.html', context=context)



def product_development_template_listing_page(request):

    templates  = ProductDevelopmentTemplate.objects.all()

    context = {'templates': templates}

    return render(request, "product_development_template_listing_page.html", context)
