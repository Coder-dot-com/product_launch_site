from django.shortcuts import redirect, render, HttpResponse

from .tasks import API_KEY

from .models import UserEmail
from .forms import EmailForm
import requests
from django.contrib import messages
# Create your views here.



def subscribe(request):

    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            email_object = UserEmail.objects.get_or_create(email=email)[0]
            email_object.promo_consent = True
            email_object.save()
        else:
            return HttpResponse("Email is not valid")
        
    else:
        form = EmailForm()
        context = {'form': form}
        return render(request, 'home_site/includes/subscribe_.html', context=context)

def unsubscribe(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            email_object = UserEmail.objects.filter(email=email)
            email_object.update(promo_consent=False)

            #Return message of successfully unsubscribed and also unsubscribe from sendinblue

    else:
        form = EmailForm()
        context = {'form': form}
        return render(request, 'home_site/unsubscribe.html', context=context)