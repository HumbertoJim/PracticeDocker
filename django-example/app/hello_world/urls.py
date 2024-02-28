from django.urls import path
from hello_world.views import HelloWorld

urlpatterns = [
    path('', HelloWorld.as_view(), name='hello_world')
]