from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as drf_status

from fibonacci.forms import FibonacciForm
from fibonacci.tools import FibonacciSequence
from fibonacci.serializers import FibonacciSerializer

class FibonacciView(View):
    def get(self, request : HttpRequest) -> HttpResponse:
        form = FibonacciForm()
        context = {'form': form}
        return render(request, 'fibonacci.html', context)
    
    def post(self, request : HttpRequest) -> HttpResponse:
        form = FibonacciForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            steps = form.cleaned_data.get('steps')
            context['fibonacci_sequence'] = FibonacciSequence(steps)
        return render(request, 'fibonacci.html', context)
        
class FibonacciAPI(APIView):
    def post(self, request: HttpRequest) -> Response:
        serializer = FibonacciSerializer(data=request.data)
        response = dict(status=1, data=None, messages=None)
        status = None
        if serializer.is_valid():
            steps = serializer.validated_data.get('steps')
            response['data'] = FibonacciSequence(steps)
            status = drf_status.HTTP_200_OK
        else:
            response['status'] = 0
            response['messages'] = serializer.errors
            status = drf_status.HTTP_400_BAD_REQUEST
        return Response(response, status)