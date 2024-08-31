# FROM tensorflow/tensorflow:2.7.0-gpu
# # for jupyter you can use the following:
# # tensorflow/tensorflow:latest-gpu-jupyter

# # from parent directory multilingual_kws:
# # docker build -t mkws docker/ 

# # inference and visualization can be run via the below command:
# # note: if you do not have nvidia-docker installed, remove "--gpus all"

# # docker run --gpus all -p 8080:8080 --rm -u $(id -u):$(id -g) -it \
# #    -v $(pwd):/demo_data \
# #    mkws \
# #    --keyword mask \
# #    --modelpath /demo_data/xfer_epochs_4_bs_64_nbs_2_val_acc_1.00_target_mask \
# #    --groundtruth /demo_data/mask_groundtruth_labels.txt \
# #    --wav /demo_data/mask_stream.wav \
# #    --transcript /demo_data/mask_full_transcript.json \
# #    --visualizer


# # switch to bash within the container



# ENV SHELL /bin/bash
# SHELL ["/bin/bash", "-c"]

# RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys A4B469963BF863CC

# ENV DEBIAN_FRONTEND noninteractive
# RUN apt update \
#     && apt install --yes --no-install-recommends \
#         fontconfig \
#         unzip \
#         locales\
#         wget \
#         curl \ 
#         sox libsox-fmt-all libsox-dev \ 
#         ffmpeg \
#         software-properties-common \
#         git \
#         opus-tools \
#         build-essential cmake \
#         libmad0-dev \ 
#         libid3tag0-dev libsndfile1-dev libgd-dev libboost-filesystem-dev \
#         libboost-program-options-dev \
#         libboost-regex-dev \
#         vim \
#     && rm -rf /var/lib/apt/lists/*

# RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
#     locale-gen
# ENV LC_ALL en_US.UTF-8
# ENV LANG en_US.UTF-8
# ENV LANGUAGE en_US.UTF-8

# # for bbc/peaks.js visualization
# RUN git clone https://github.com/bbc/audiowaveform.git \
#     && cd audiowaveform \
#     && mkdir build \
#     && cd build \
#     && cmake -D ENABLE_TESTS=0 .. \
#     && make \ 
#     && make install
# RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
#     && apt install -y nodejs \
#     && npm install -g serve

# RUN pip install dataclasses sox matplotlib seaborn pandas pydub fire fastapi

# FROM python:3.10-slim

# # Copy the FastAPI application

# EXPOSE 8000

# # Run FastAPI application with uvicorn
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# # RUN echo "alpha-0.0.0"
# RUN git clone https://github.com/Satyam709/KwsModel /multilingual_kws

# WORKDIR /multilingual_kws

# RUN wget https://github.com/harvard-edge/multilingual_kws/releases/download/v0.1-alpha/multilingual_context_73_0.8011.tar.gz && \
#     tar xf multilingual_context_73_0.8011.tar.gz
# RUN wget https://github.com/harvard-edge/multilingual_kws/releases/download/v0.1-alpha/unknown_files.tar.gz && \
#     tar xf unknown_files.tar.gz
# RUN chmod -R 777 /multilingual_kws/visualizer/

# ENTRYPOINT ["bash"]




# Use TensorFlow base image with GPU support
FROM tensorflow/tensorflow:2.7.0-gpu AS base

# Install system dependencies and Python packages
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys A4B469963BF863CC
RUN apt-get update && \
    apt-get install -y \
        fontconfig \
        unzip \
        locales \
        wget \
        curl \
        sox \
        libsox-fmt-all \
        libsox-dev \
        ffmpeg \
        software-properties-common \
        git \
        opus-tools \
        build-essential \
        cmake \
        libmad0-dev \
        libid3tag0-dev \
        libsndfile1-dev \
        libgd-dev \
        libboost-filesystem-dev \
        libboost-program-options-dev \
        libboost-regex-dev \
        vim \
    && rm -rf /var/lib/apt/lists/*


RUN git clone https://github.com/Satyam709/KwsModel /multilingual_kws

RUN wget https://github.com/harvard-edge/multilingual_kws/releases/download/v0.1-alpha/multilingual_context_73_0.8011.tar.gz && \
    tar xf multilingual_context_73_0.8011.tar.gz
RUN wget https://github.com/harvard-edge/multilingual_kws/releases/download/v0.1-alpha/unknown_files.tar.gz && \
    tar xf unknown_files.tar.gz
RUN chmod -R 777 /multilingual_kws/visualizer/


# Set locale
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# Install Python packages
RUN pip install --no-cache-dir \
        dataclasses \
        sox \
        python-multipart \
        matplotlib \
        seaborn \
        pandas \
        pydub \
        fire \
        fastapi \
        uvicorn \
    && rm -rf /root/.cache

RUN pip install --upgrade typing_extensions

# Copy FastAPI application code
WORKDIR /multilingual_kws
# Expose the port that FastAPI will run on

WORKDIR /app

EXPOSE 8080

# Copy the FastAPI application files into the container

# Run FastAPI application with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

# You can optionally install other Python dependencies or setup as needed
