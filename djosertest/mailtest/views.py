from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):

    send_mail(
        'Subject here',
        'Here is the message.',
        'sherin@gmail.com',
        ['nixutuvo@webmail24.top'],
        fail_silently=False,
    )
    return HttpResponse('Email send')

