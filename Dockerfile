# FROM face-extractor:latest
# keep the container active
# ENTRYPOINT ["tail", "-f", "/dev/null"]
FROM orgoro/dlib-opencv-python:latest
COPY requirements.txt  /
COPY extract-face.py  /
#RUN apt-get upgrade && apt-get update
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python extract-face.py