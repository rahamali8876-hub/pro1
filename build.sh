#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

# Create superuser automatically if not exists
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = "SuperUser"
password = "superuser"
email = "superuser@example.com"
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created")
else:
    print("Superuser already exists")
EOF
