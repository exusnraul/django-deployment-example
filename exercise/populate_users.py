import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','exercise.settings')

import django
django.setup()

from faker import Faker

import random
from user_app.models import user_info

fakegen = Faker()

def populate(N=5):
    for entry in range (N):
        fake_first_name=fakegen.first_name()
        fake_last_name=fakegen.last_name()
        fake_email=fakegen.free_email()

        user = user_info.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email_id=fake_email)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(50)
    print('Populating Complete')

