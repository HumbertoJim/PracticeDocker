from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import os


def hello_world(request : HttpRequest) -> HttpResponse:
    context = {
        'admin_message': os.environ.get('ADMIN_MESSAGE')
    }
    return render(request, 'hello_world.html', context)