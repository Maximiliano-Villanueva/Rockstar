FROM continuumio/miniconda3
WORKDIR /home
RUN mkdir -p instrument-separator
RUN mkdir -p shared-files
ADD code instrument-separator
RUN conda install -c conda-forge ffmpeg libsndfile
RUN pip install -r /home/instrument-separator/requirements.txt
EXPOSE 8081
#CMD ["python", "/home/instrument-separator/main.py"]
