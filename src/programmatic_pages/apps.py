from __future__ import unicode_literals
from django.apps import AppConfig
class ProgrammaticPagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'programmatic_pages'
    
    def ready(self):
        import programmatic_pages.signals  