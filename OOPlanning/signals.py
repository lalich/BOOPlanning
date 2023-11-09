# OOPlanning/signals.py

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    # Class One Groups
    investor_groups = ['<1M', '1M-<10M', '10M-<100M', '>100M']
    for group_name in investor_groups:
        Group.objects.get_or_create(name=f"Investor - {group_name}")

    # Class Two Groups
    wvc_groups = ['Junior', 'Senior', 'Partner']
    for group_name in wvc_groups:
        Group.objects.get_or_create(name=f"WVC - {group_name}")
