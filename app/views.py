from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def first(request):
    return HttpResponse('this is our first view ra ballayya')
def narikesta(request):
    return HttpResponse('<marquee>sattireddy narikeyali nakodukuni')