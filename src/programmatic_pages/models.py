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
        if not self.intro:

            intros = [
                f"When it comes developing new products because this {self.keyword.keyword.lower()} is sure to help. It is the perfect way to streamline your development process, saving your precious time and ensuring that nothing is left out. "
            ]   
            self.intro = random.choice(intros)

        
        if not self.title_image:
            img = create_title_image(self.keyword.keyword)

            blob = BytesIO()
            img.save(blob, 'JPEG', quality=85)  
            self.title_image.save(f'{self.keyword.keyword}.jpg', File(blob), save=False) 

        

        if not self.second_title:
            time.sleep(1)
            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #."
                },
                {
                "role": "user",
                "content": f"Rephrase the seo phrase '{self.keyword.keyword}'"
                },
            ],
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            self.second_title = content



        if not self.second_intro:
            time.sleep(1)

            second_intros = [
                f"This template provides a structured framework for planning and executing product development projects, guiding teams through each stage from concept to launch. Using a template can enhance efficiency and effectiveness in bringing new products to market. Whether you are a seasoned product manager incorporating the {self.keyword.keyword.lower()} into your workflow can drive innovation and drive success in today's dynamic market. ",

            ]   
            self.second_intro = random.choice(second_intros)

        if not self.idea_generation_content:
            time.sleep(1)

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #."
                },
                {
                "role": "user",
                "content": f"Write an approximately 100 word intro to a template for idea generation for a post titled '{self.keyword.keyword}'"
                },
            ],
            temperature=1.2,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            self.idea_generation_content = content

        if not self.validation_content:
            time.sleep(1)

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #."
                },
                {
                "role": "user",
                "content": f"Write an approximately 100 word intro to a template for idea validation for a post titled '{self.keyword.keyword}'"
                },
            ],
            temperature=1.2,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            self.validation_content = content


        if not self.prototyping_content:
            time.sleep(1)

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #."
                },
                {
                "role": "user",
                "content": f"Write an approximately 100 word intro to a section on prototyping/creating a mvp for a post titled '{self.keyword.keyword}'"
                },
            ],
            temperature=1.1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            self.prototyping_content = content


        if not self.marketing_content:
            time.sleep(1)

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about product development templates"
                },
                {
                "role": "user",
                "content": f"Write an approximately 100 word intro to a subsection on a single marketing template for a post titled '{self.keyword.keyword}'"
                },
            ],
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            self.marketing_content = content


        if not self.launch_content:
            time.sleep(1)

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about what it covers"
                },
                {
                "role": "user",
                "content": f"Write an approximately 100 word intro to a subsection on a product launch template for a post titled '{self.keyword.keyword}'"
                },
            ],
            temperature=1.2,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            self.launch_content = content

        if not self.evaluating_content:
            time.sleep(1)

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about product development templates"
                },
                {
                "role": "user",
                "content": f"Write an approximately 100 word intro to a subsection on evaluating the success of a product template for a post titled '{self.keyword.keyword}'"
                },
            ],
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            self.evaluating_content = content


        if not self.meta_description:
            time.sleep(1)

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about product development templates"
                },
                {
                "role": "user",
                "content": f"Write an approximately 160 character meta description for a page titled: '{self.keyword.keyword}'"
                },
            ],
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            self.meta_description = content

   
                

        return super().save(*args, **kwargs)