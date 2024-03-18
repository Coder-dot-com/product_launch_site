from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProductDevelopmentTemplate, FAQQuestionProductDevelopmentTemplate
from uuid import uuid4

from openai import OpenAI

from decouple import config
import time
from .tasks import create_faq_product_templates

@receiver(post_save, sender=ProductDevelopmentTemplate, dispatch_uid=f'save_product_template{uuid4()}')
def save_profile(sender, instance, created, **kwargs):
    template = instance

    result = create_faq_product_templates.delay(template.id)







    