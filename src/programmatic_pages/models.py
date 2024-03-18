from django.db import models
import random
from blog.utils.blog_page.create_title_image import create_title_image
from io import BytesIO
from django.core.files import File
from openai import OpenAI
from decouple import config
import time
# Create your models here.

choices = [
    ("ProductDevelopmentTemplate", "ProductDevelopmentTemplate"),
]
class Keyword(models.Model):
    keyword = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    template_type = models.CharField(max_length=300, choices=choices)


    def __str__(self):
        return self.keyword

class FAQQuestionProductDevelopmentTemplate(models.Model):
    question = models.TextField(max_length=1000, blank=True, null=True)
    answer = models.TextField(max_length=5000, blank=True, null=True)
    product_development_template = models.ForeignKey('ProductDevelopmentTemplate', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.question 

class ProductDevelopmentTemplate(models.Model):

    keyword = models.OneToOneField(Keyword, on_delete=models.CASCADE)
    meta_description = models.TextField(max_length=300, blank=True, null=True)
    intro = models.TextField(max_length=1000, blank=True, null=True)
    title_image = models.ImageField(upload_to='resources/templates/', blank=True, null=True)
    second_title =  models.TextField(max_length=300, null=True, blank=True)
    second_intro = models.TextField(max_length=1000, blank=True, null=True)
    idea_generation_content = models.TextField(max_length=2000, blank=True, null=True)
    validation_content = models.TextField(max_length=2000, blank=True, null=True)
    prototyping_content = models.TextField(max_length=2000, blank=True, null=True)
    marketing_content = models.TextField(max_length=2000, blank=True, null=True)
    launch_content = models.TextField(max_length=2000, blank=True, null=True)
    evaluating_content = models.TextField(max_length=2000, blank=True, null=True)


    def get_FAQ(self):
        return FAQQuestionProductDevelopmentTemplate.objects.filter(product_development_template=self)

    def save(self, *args, **kwargs):


        if not self.second_intro:
            time.sleep(1)

            second_intros = [
                f"This template provides a structured framework for planning and executing product development projects, guiding teams through each stage from concept to launch. Using a template can enhance efficiency and effectiveness in bringing new products to market. Whether you are a seasoned product manager incorporating the {self.keyword.keyword.lower()} into your workflow can drive innovation and drive success in today's dynamic market. ",

                f"With the help of this template, teams may plan and carry out product development initiatives in an organised manner, following it from concept to launch. Introducing new products to the market can be done more effectively and efficiently by using a template. In today's dynamic market, integrating {self.keyword.keyword.lower()} into your workflow can foster creativity and success, regardless of your level of experience.",

                f"This template offers a methodical approach to organising and carrying out product development initiatives, assisting groups at every phase from ideation to introduction. When introducing new products to the market, using a template can increase efficacy and efficiency. Using {self.keyword.keyword.lower()} in your workflow can spur creativity and success in today's fast-paced market, regardless of experience level as a product manager.",

                f"By leading teams through every phase of the process, from concept to launch, this template offers an organised framework for organising and carrying out product development projects. When launching new items, using a template can increase efficacy and efficiency. No matter how experienced you are, adding {self.keyword.keyword.lower()} to your workflow can spur success in the fast-paced market of today."

            ]   
            self.second_intro = random.choice(second_intros)




   
                

        return super().save(*args, **kwargs)