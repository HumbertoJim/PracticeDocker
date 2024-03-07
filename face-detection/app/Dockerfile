FROM python:3.10

WORKDIR /usr/src/app

COPY . /usr/src/app/

# dependencies
RUN pip install -r requirements.torch.txt
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
RUN pip install -r requirements.txt
