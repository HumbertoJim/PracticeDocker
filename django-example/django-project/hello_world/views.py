from django.views import View
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import datetime


# Create your views here.
class HelloWorld(View):
    def get(self, request:HttpRequest) -> HttpResponse:
        context = {'datetime': datetime.datetime.now()}
        return render(request, 'hello_world.html', context)