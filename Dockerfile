FROM python:3.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Project Files and Settings
WORKDIR /code

# Copy project
COPY . /code/

# Install dependencies
RUN pip install pipenv && pipenv install --system

# Server
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]