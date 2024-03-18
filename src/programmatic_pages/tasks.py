from product_launch_site.celery import app
from celery.utils.log import get_task_logger
from .models import ProductDevelopmentTemplate, FAQQuestionProductDevelopmentTemplate
from openai import OpenAI
from decouple import config
import time
from blog.utils.blog_page.create_title_image import create_title_image
from io import BytesIO
from django.core.files import File
logger = get_task_logger(__name__)



@app.task
def create_product_template_intro(product_template_object_id):
    try:
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    except ProductDevelopmentTemplate.DoesNotExist:
        time.sleep(10)
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)


    if not template.intro:

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about other websites"
                },
                {
                "role": "user",
                "content": f"Write an approximately 75 word intro for a page titled: '{template.keyword.keyword}'"
                },
            ],
            temperature=1.2,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )

            content = (response.choices[0].message.content)

            print('content', content)

            template.intro = content
            template.save()



@app.task
def create_product_template_second_title(product_template_object_id):
    try:
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    except ProductDevelopmentTemplate.DoesNotExist:
        time.sleep(10)
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)


    if not template.second_title:

            time.sleep(1)
            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not use the word welcome."
                },
                {
                "role": "user",
                "content": f"Rephrase the seo phrase '{template.keyword.keyword}'"
                },
            ],
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            template.second_title = content
            template.save()

@app.task
def create_product_template_idea_generation(product_template_object_id):
    try:
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    except ProductDevelopmentTemplate.DoesNotExist:
        time.sleep(10)
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)

    if not template.idea_generation_content:
            time.sleep(1)

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not use the word welcome. Do not mention any websites."
                },
                {
                "role": "user",
                "content": f"Write an approximately 100 word intro to a template for idea generation for a post titled '{template.keyword.keyword}'"
                },
            ],
            temperature=1.1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            template.idea_generation_content = content
            template.save()


@app.task
def create_product_template_idea_generation(product_template_object_id):
    try:
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    except ProductDevelopmentTemplate.DoesNotExist:
        time.sleep(10)
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)

    if not template.idea_generation_content:
            time.sleep(1)

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not use the word welcome."
                },
                {
                "role": "user",
                "content": f"Write an approximately 100 word intro to a template for idea generation for a post titled '{template.keyword.keyword}'"
                },
            ],
            temperature=1.1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            template.idea_generation_content = content
            template.save()

@app.task
def create_product_template_validation(product_template_object_id):
    try:
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    except ProductDevelopmentTemplate.DoesNotExist:
        time.sleep(10)
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    if not template.validation_content:
            time.sleep(1)

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not use the word welcome. Do not mention any websites."
                },
                {
                "role": "user",
                "content": f"Write an approximately 100 word pre-amble on a template for idea validation for a post titled '{template.keyword.keyword}'"
                },
            ],
            temperature=1.1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            template.validation_content = content
            template.save()


@app.task
def create_product_template_prototyping_content(product_template_object_id):
    try:
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    except ProductDevelopmentTemplate.DoesNotExist:
        time.sleep(10)
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)

    if not template.prototyping_content:

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not use the word welcome. Do not mention any websites."
                },
                {
                "role": "user",
                "content": f"Write an approximately 100 word intro to a section on prototyping/creating a mvp for a post titled '{template.keyword.keyword}'"
                },
            ],
            temperature=1.1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            template.prototyping_content = content
            template.save()


@app.task
def create_product_template_marketing_content(product_template_object_id):
    try:
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    except ProductDevelopmentTemplate.DoesNotExist:
        time.sleep(10)
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)

    if not template.marketing_content:

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about product development templates. Do not mention any websites."
                },
                {
                "role": "user",
                "content": f"Write an approximately 100 word intro to a subsection on a single marketing template for a post titled '{template.keyword.keyword}'"
                },
            ],
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            template.marketing_content = content
            template.save()



@app.task
def create_product_template_launch_content(product_template_object_id):
    try:
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    except ProductDevelopmentTemplate.DoesNotExist:
        time.sleep(10)
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)

    if not template.launch_content:

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about what it covers. Do not mention any websites."
                },
                {
                "role": "user",
                "content": f"Write an approximately 100 word intro to a subsection on a product launch template for a post titled '{template.keyword.keyword}'"
                },
            ],
            temperature=1.1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            template.launch_content = content
            template.save()

@app.task
def create_product_template_evaluating_content(product_template_object_id):
    try:
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    except ProductDevelopmentTemplate.DoesNotExist:
        time.sleep(10)
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)

    if not template.evaluating_content:

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about product development templates. Do not mention any websites."
                },
                {
                "role": "user",
                "content": f"Write an approximately 100 word intro to a subsection on evaluating the success of a product template for a post titled '{template.keyword.keyword}'"
                },
            ],
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            template.evaluating_content = content
            template.save()

@app.task
def create_product_template_meta_description(product_template_object_id):
    try:
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    except ProductDevelopmentTemplate.DoesNotExist:
        time.sleep(10)
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)

    if not template.meta_description:

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about product development templates. Do not mention any websites."
                },
                {
                "role": "user",
                "content": f"Write an approximately 160 character meta description for a page titled: '{template.keyword.keyword}'"
                },
            ],
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            content = (response.choices[0].message.content)
            template.meta_description = content
            template.save()


@app.task
def create_title_image_async(product_template_object_id):
    try:
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    except ProductDevelopmentTemplate.DoesNotExist:
        time.sleep(10)
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    if not template.title_image:

            img = create_title_image(template.keyword.keyword)

            blob = BytesIO()
            img.save(blob, 'JPEG', quality=85)  
            template.title_image.save(f'{template.keyword.keyword}.jpg', File(blob), save=False)
            template.save() 



@app.task
def create_faq_product_templates(product_template_object_id):
    try:
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)
    except ProductDevelopmentTemplate.DoesNotExist:
        time.sleep(10)
        template = ProductDevelopmentTemplate.objects.get(id=product_template_object_id)

    if not FAQQuestionProductDevelopmentTemplate.objects.filter(product_development_template=template).exists():

            client = OpenAI(
            api_key=config("OPENAI_API_KEY"),
            )
            response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                "role": "system",
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about product development templates. Do not include numbers, use a new line for each question. Do not talk about examples"
                },
                {
                "role": "user",
                "content": f"Write 5 frequently asked questions for a page titled: '{template.keyword.keyword}'"
                },
            ],
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )

            content = (response.choices[0].message.content)

            print('content', content)

            questions = [x for x in content.split('\n') if x != ""]

            for question in questions:
                time.sleep(1)

                client = OpenAI(
                api_key=config("OPENAI_API_KEY"),
                )
                response = client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {
                    "role": "system",
                    "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about product development templates. Do not mention any other websites."
                    },
                    {
                    "role": "user",
                    "content": f"Answer the following in approximately 250 words '{question}' for {template.keyword.keyword}"
                    },
                ],
                temperature=1.1,
                max_tokens=512,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
                answer = (response.choices[0].message.content)

                faq_section = FAQQuestionProductDevelopmentTemplate.objects.create(question=question, answer=answer, product_development_template=template)


