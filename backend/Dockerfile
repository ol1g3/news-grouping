FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_PORT=8000

# Set the working directory inside the container
WORKDIR /app/backend

# Copy the requirements file first for better caching
COPY requirements.txt /app/backend

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/backend/

VOLUME /home/app/backend/news_grouping/static

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && gunicorn news_grouping.wsgi:application --bind 0.0.0.0:${APP_PORT}"]

EXPOSE ${APP_PORT}