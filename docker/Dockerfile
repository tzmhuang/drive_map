FROM registry.access.redhat.com/ubi9/python-39:1-117.1684741281

# By default, listen on port 8081
EXPOSE 8081/tcp
ENV FLASK_PORT=8081

# Set the working directory in the container
WORKDIR /projects

# Copy the content of the local src directory to the working directory
COPY . .

RUN cd /projects
# ADD ./map_webapp ./map_webapp

# location to mount volumn
USER 0
RUN mkdir /volumn
RUN mkdir /volumn/uploads

# symlink to volumn
RUN ln -s /volumn ./static/volumn

# # TEST
# ADD  data/vids /volumn/vids

# RUN yum install vim-enhanced -y  

# Install any dependencies
RUN \
  if [ -f requirements.txt ]; \
    then pip install -r requirements.txt; \
  elif [ `ls -1q *.txt | wc -l` == 1 ]; \
    then pip install -r *.txt; \
  fi

# Specify the command to run on container start
CMD [ "python", "./app.py" ]
