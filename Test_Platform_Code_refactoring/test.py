import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Test_Platform_Code_refactoring.settings")  # NoQA
import django
django.setup()  # NoQA
from django.utils import timezone

a=timezone.now()

print(a)