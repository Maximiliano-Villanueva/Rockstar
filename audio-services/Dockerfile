FROM continuumio/miniconda3
WORKDIR /home
RUN mkdir -p audio-services
RUN mkdir -p shared-files
ADD . audio-services
RUN conda install -c conda-forge ffmpeg libsndfile
RUN pip install -r /home/audio-services/code/requirements.txt
RUN apt-get update
RUN apt-get -y install libsndfile1
RUN apt-get -y install timidity
RUN apt-get -y install ffmpeg
RUN apt-get install -y --no-install-recommends gcc
RUN apt-get install -y --reinstall build-essential
RUN pip install -r /home/audio-services/code/external/chord_extractor/requirements.txt
EXPOSE 8081
#CMD ["python", "/home/audio-services/main.py"]
