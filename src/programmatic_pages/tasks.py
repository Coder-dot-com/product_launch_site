from product_launch_site.celery import app
from celery.utils.log import get_task_logger
from .models import ProductDevelopmentTemplate, FAQQuestionProductDevelopmentTemplate

from openai import OpenAI
from decouple import config
import time
logger = get_task_logger(__name__)



@app.task
def create_product_template_intro(product_template_object_id):
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
def create_faq_product_templates(product_template_object_id):
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
                "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about product development templates. Do not include numbers, use a new line for each question"
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


