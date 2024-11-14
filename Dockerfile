# Dockerfile

# Use the official Python image with the desired version
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Run the Django development server ( or any other commands)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
