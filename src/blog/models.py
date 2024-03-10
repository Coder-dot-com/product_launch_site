from datetime import datetime
from random import randint
from uuid import uuid4
from xml.dom.minidom import Attr
from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.search import index
from wagtail import blocks
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalManyToManyField
from django import forms
from django.shortcuts import render, redirect
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path, route

from blog.utils.blog_page.create_gradient import create_gradient
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.core.files import File

from blog.utils.blog_page.wrap_text import wrap_text
from product_launch_site.settings import BASE_DIR
import requests

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import urllib


@register_snippet
class BlogCategory(models.Model):
    """Blog category for a snippet."""

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='A slug to identify posts by this category',
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name



class BlogListingPage(RoutablePageMixin, Page):
    """Listing page lists all the Blog Detail Pages."""

    template = "blog/blog_listing_page.html"
    ajax_template = "blog/blog_listing_page_ajax.html"
    max_count = 1


    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = BlogPage.objects.live().public()

        page = request.GET.get("page")
        posts = all_posts
        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["posts"] = posts
        context["categories"] = BlogCategory.objects.all()
        return context


    @route(r"^category/(?P<cat_slug>[-\w]*)/$", name="category_view")
    def category_view(self, request, cat_slug):
        """Find blog posts based on a category."""
        context = self.get_context(request)

        try:
            # Look for the blog category by its slug.
            category = BlogCategory.objects.get(slug=cat_slug)
        except Exception:
            # Blog category doesnt exist (ie /blog/category/missing-category/)
            # Redirect to self.url, return a 404.. that's up to you!
            category = None
        context["posts"] = BlogPage.objects.live().public().filter(categories__in=[category]).order_by('date').reverse()
        context['category'] = category

        if category is None and cat_slug == 'all':
            # This is an additional check.
            # If the category is None, do something. Maybe default to a particular category.
            # Or redirect the user to /blog/ ¯\_(ツ)_/¯
            context["posts"] = BlogPage.objects.live().public().order_by('date').reverse()
        elif category == None:
            return redirect('home')


        # Note: The below template (latest_posts.html) will need to be adjusted
        return render(request, "blog/blog_listing_page.html", context)




    def get_sitemap_urls(self, request):
        # Uncomment to have no sitemap for this page
        # return []
        sitemap = super().get_sitemap_urls(request)
        
        categories = BlogCategory.objects.all()
        sitemap.append(
                {
                    "location": self.full_url + self.reverse_subpage("category_view", kwargs={'cat_slug': 'all'}),
                    "lastmod": (self.last_published_at or self.latest_revision_created_at),
                    "priority": 0.6,
                    'protocol': 'https',

                }
            )

        for category in categories:
            sitemap.append(
                {
                    "location": self.full_url + self.reverse_subpage("category_view", kwargs={'cat_slug': category.slug}),
                    "lastmod": (self.last_published_at or self.latest_revision_created_at),
                    "priority": 0.6,
                    'protocol': 'https',

                }
            )

        return sitemap
    """Listing page lists all the Blog Detail Pages."""

  

class ArticleSectionBlock(blocks.StructBlock):
    header = blocks.CharBlock(required=False)
    content = blocks.RichTextBlock(required=False)

class ContentBlock(blocks.StructBlock):
    content = blocks.RichTextBlock(required=False)

def default_date_time():
    now = datetime.now().date
    return now 



class BlogPage(Page):
    date = models.DateField("Post date", default=default_date_time)
    intro = StreamField(
        [("article_section", ContentBlock())],
        null=True,
        blank=True,
    )
    title_image = models.ImageField(upload_to="blog_images/title", null=True, blank=True)
    second_intro = StreamField(
        [("article_section", ContentBlock())],
        null=True,
        blank=True,
    )

    secondary_title = models.CharField(max_length=300)
    secondary_title_image = models.ImageField(upload_to="blog_images/secondary", null=True, blank=True)
    text_before_content = StreamField(
        [("article_section", ContentBlock())],
        null=True,
        blank=True,
    )
    content = StreamField(
        [("article_section", ArticleSectionBlock())],
        null=False,
        blank=False,
    )

    categories = ParentalManyToManyField("blog.BlogCategory", blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('content'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('title_image'),
        FieldPanel('second_intro'),
        FieldPanel('secondary_title'),
        FieldPanel('secondary_title_image'),
        FieldPanel('text_before_content'),

        FieldPanel("content"),
        MultiFieldPanel(
            [
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Categories"
        ),
    ]


    def save(self, *args, **kwargs):
  

        return super().save(*args, **kwargs)

    def get_next_article(self):
        try:
            return BlogPage.objects.live().public().filter(id__gt=self.id).order_by("id")[0]
        except IndexError:
            return None

    def get_previous_article(self):
        try:
            return BlogPage.objects.live().public().filter(id__lt=self.id).order_by("id").reverse()[0]
        except IndexError:
            return None   
    def get_5_next_in_same_category(self):
        # Make sure get_next_article is excluded
        try:
            categories = self.categories.all().values_list('id', flat=True)
            return BlogPage.objects.live().public().exclude().filter(
                id__gt=self.id,categories__in=categories).order_by("id")[0:5]
        except IndexError:
            return None
        except AttributeError:
            return None







