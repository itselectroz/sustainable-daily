FROM python:3.11-buster

# Setup environment
ENV DockerHOME=/home/app/sustainable_daily
ENV PORT=8000
ENV CRONTAB_TASK=dailytask

## Python vars

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# Create work directory
RUN mkdir -p $DockerHOME

# Install dependencies
RUN apt-get update && \
    apt-get -y install cron

# Set working directory and permissions
WORKDIR $DockerHOME

# Copy project over
COPY . $DockerHOME

# Install pip and python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose working port
EXPOSE ${PORT}

# Setup server
RUN python manage.py migrate

# Start cron and runserver
CMD ["sh", "-c", "python manage.py dummydata && python manage.py migrate && python manage.py runserver 0.0.0.0:${PORT}"]
