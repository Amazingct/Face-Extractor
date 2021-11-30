FROM python:3.7
COPY ./main  /main
WORKDIR /main
RUN pip install -r requirements.txt
CMD python extract-face.py