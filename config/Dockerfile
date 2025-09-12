# base image
FROM sddcunit/downstream:scmorpho-1.1.0

# avoid interactive prompts 
ENV DEBIAN_FRONTEND=noninteractive

# specify the working directory
WORKDIR /app
COPY requirements.txt /app

# install additional packages for python
RUN pip install -r requirements.txt


 
