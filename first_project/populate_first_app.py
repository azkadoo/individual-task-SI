from faker import Faker
from first_app.models import Topic, Webpage, AccessRecord
import random
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

django.setup()

# Fake Pop Script

fakegen = Faker()
topics = ["Social", "Search", "Marketplace", "News", "Games"]


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):

        # Dapatkan topik untuk entri
        top = add_topic()

        # membuat data dummy untuk entri
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # buat input webpage
        webpg = Webpage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name)[0]

        # buat fake access
        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("Populate script...")
    populate(15)
    print("Populate selesai!")
