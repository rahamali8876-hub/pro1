from django.contrib.auth import get_user_model
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pro1.settings")
django.setup()

User = get_user_model()

if not User.objects.filter(username="SuperUser").exists():
    User.objects.create_superuser("SuperUser", "superuser@example.com", "superuser")
    print("Superuser created")
else:
    print("Superuser already exists")
    