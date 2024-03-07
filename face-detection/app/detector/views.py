from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse

from PIL import Image, ImageDraw
from io import BytesIO
import base64
from facenet_pytorch import MTCNN

from detector.forms import ImageForm


mtcnn = MTCNN(margin=50)


# Create your views here.
class FaceDetectorView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = ImageForm()
        context = {'form': form}
        return render(request, 'detector.html', context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = ImageForm(files=request.FILES)
        context = {'form': form}
        if form.is_valid():
            # read image
            image = Image.open(form.cleaned_data.get('image'))
            buffer = BytesIO()

            # detect faces
            boxes, probs = mtcnn.detect(image)
            if boxes is not None:
                drawer = ImageDraw.Draw(image)
                for i, box in enumerate(boxes):
                    if probs[i] > 0.95:
                        drawer.rectangle(
                            box.tolist(),
                            width=4,
                            outline='lime'
                        )

            # show image
            image.save(buffer, format=image.format)
            im_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            context['image'] = im_base64
        return render(request, 'detector.html', context)
