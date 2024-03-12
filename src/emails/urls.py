from django.urls.conf import path
from . import views

urlpatterns = [
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('subscribe_email/', views.subscribe_email, name='subscribe_email'),

]