from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProductDevelopmentTemplate, FAQQuestionProductDevelopmentTemplate
from uuid import uuid4

from openai import OpenAI

from decouple import config
import time
from .tasks import create_product_template_intro, create_title_image_async, create_faq_product_templates, create_product_template_second_title,create_product_template_idea_generation, create_product_template_validation, create_product_template_prototyping_content, create_product_template_marketing_content, create_product_template_launch_content, create_product_template_evaluating_content, create_product_template_meta_description

@receiver(post_save, sender=ProductDevelopmentTemplate, dispatch_uid=f'save_product_template{uuid4()}')
def save_profile(sender, instance, created, **kwargs):
    template = instance

    create_product_template_intro.delay(template.id)
    create_product_template_second_title.delay(template.id)
    create_title_image_async.delay(template.id)
    create_product_template_idea_generation.delay(template.id)
    create_product_template_validation.delay(template.id)
    create_product_template_prototyping_content.delay(template.id)
    create_product_template_marketing_content.delay(template.id)
    create_product_template_launch_content.delay(template.id)
    create_product_template_evaluating_content.delay(template.id)
    create_product_template_meta_description.delay(template.id)


    create_faq_product_templates.delay(template.id)







    