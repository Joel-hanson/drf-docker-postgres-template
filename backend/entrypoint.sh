
#!/bin/sh

# Collect static files
echo "Collect static files"
# python manage.py collectstatic --noinput


echo "Apply database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Creating superuser
echo "Creating superuser"
python manage.py createsu

# Creating superuser
echo "Run populate data"
python manage.py populate_data

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000