import os
import django
from django.db import connection

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcrm.settings")
django.setup()

# Database connection parameters
dbname = "dcrm_test"

# Create the database using Django's connection
with connection.cursor() as cursor:
    cursor.execute(f"CREATE DATABASE {dbname}")

print(f"Database '{dbname}' created successfully.")
