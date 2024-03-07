from django.urls import path
from detector.views import FaceDetectorView


urlpatterns = [
    path('', FaceDetectorView.as_view(), name='detector')
]
