from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProductDevelopmentTemplate, FAQQuestionProductDevelopmentTemplate
from uuid import uuid4
from blog.utils.blog_page.create_title_image import create_title_image
from io import BytesIO
from django.core.files import File

from decouple import config
import time
from .tasks import create_product_template_intro, create_title_image_async, create_faq_product_templates

@receiver(post_save, sender=ProductDevelopmentTemplate, dispatch_uid=f'save_product_template{uuid4()}')
def save_profile(sender, instance, created, **kwargs):
    template = instance

    time.sleep(5)
    if not template.title_image:

            img = create_title_image(template.keyword.keyword)

            blob = BytesIO()
            img.save(blob, 'JPEG', quality=85)  
            template.title_image.save(f'{template.keyword.keyword}.jpg', File(blob), save=False)
            template.save() 
    time.sleep(1)
    create_title_image_async.delay(template.id)
    time.sleep(1)
    create_faq_product_templates.delay(template.id)







    