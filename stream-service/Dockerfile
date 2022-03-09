FROM continuumio/miniconda3
WORKDIR /home
RUN mkdir -p stream-service
RUN mkdir -p shared-files
ADD . stream-service
RUN conda install -c conda-forge ffmpeg libsndfile
RUN pip install -r /home/stream-service/code/requirements.txt
RUN apt-get update
EXPOSE 8081
