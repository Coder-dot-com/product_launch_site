from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProductDevelopmentTemplate, FAQQuestionProductDevelopmentTemplate
from uuid import uuid4

from openai import OpenAI

from decouple import config
import time

@receiver(post_save, sender=ProductDevelopmentTemplate, dispatch_uid=f'save_product_template{uuid4()}')
def save_profile(sender, instance, created, **kwargs):
    template = instance
    from .tasks import my_task

    result = my_task.delay(3, 5)

    # if not FAQQuestionProductDevelopmentTemplate.objects.filter(product_development_template=template).exists():

    #         client = OpenAI(
    #         api_key=config("OPENAI_API_KEY"),
    #         )
    #         response = client.chat.completions.create(
    #         model="gpt-4-turbo-preview",
    #         messages=[
    #             {
    #             "role": "system",
    #             "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about product development templates. Do not include numbers, use a new line for each question"
    #             },
    #             {
    #             "role": "user",
    #             "content": f"Write 5 frequently asked questions for a page titled: '{instance.keyword.keyword}'"
    #             },
    #         ],
    #         temperature=1,
    #         max_tokens=1000,
    #         top_p=1,
    #         frequency_penalty=0,
    #         presence_penalty=0
    #         )

    #         content = (response.choices[0].message.content)

    #         print('content', content)

    #         questions = [x for x in content.split('\n') if x != ""]

    #         for question in questions:
    #             time.sleep(1)

    #             client = OpenAI(
    #             api_key=config("OPENAI_API_KEY"),
    #             )
    #             response = client.chat.completions.create(
    #             model="gpt-4-turbo-preview",
    #             messages=[
    #                 {
    #                 "role": "system",
    #                 "content": "Write in plaintext. Write like a human. Do not use markdown formatting. Do not use * or #. Do not talk about product development templates."
    #                 },
    #                 {
    #                 "role": "user",
    #                 "content": f"Answer the following in approximately 250 words '{question}' for {instance.keyword.keyword}"
    #                 },
    #             ],
    #             temperature=1.1,
    #             max_tokens=512,
    #             top_p=1,
    #             frequency_penalty=0,
    #             presence_penalty=0
    #             )
    #             answer = (response.choices[0].message.content)

    #             faq_section = FAQQuestionProductDevelopmentTemplate.objects.create(question=question, answer=answer, product_development_template=instance)







    