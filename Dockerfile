# backend/Dockerfile

# Base image
FROM nvidia/cuda:10.2-cudnn7-runtime-ubuntu18.04

# Update PATH environment variables to use commands like conda
ENV PATH="/root/miniconda3/bin:${PATH}" 
ARG PATH="/root/miniconda3/bin:${PATH}"

# Download shell apps and miniconda for the container (-y assume yes if prompted)
RUN apt-get update \
    && apt-get install -y htop wget sudo curl make nano libc-dev \
    && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir root/.conda \
    && sh Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

# Install cv2 dependencies 
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "server.py", "--precache-models"]