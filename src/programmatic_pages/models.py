from django.db import models
import random
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

class ProductDevelopmentTemplate(models.Model):


    keyword = models.OneToOneField(Keyword, on_delete=models.CASCADE)
    meta_description = models.TextField(max_length=160)
    intro = models.TextField(max_length=1000, blank=True, null=True)
    title_image = models.ImageField(upload_to='resources/templates/', blank=True, null=True)



    def save(self, *args, **kwargs):
        if not self.intro:

            intros = [
                f"No need to reinvent the wheel when it comes developing new products because this {self.keyword} is sure to help. It is the perfect way to streamline your development process, saving your precious time and ensuring that nothing falls through the cracks. "
            ]   
            self.intro = random.choice(intros)





        return super().save(*args, **kwargs)