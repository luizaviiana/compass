FROM public.ecr.aws/lambda/python:3.9

WORKDIR /build

RUN yum install -y zip

COPY requirements.txt .

RUN pip install -r requirements.txt -t python

RUN zip -r9 requests-layer.zip python
