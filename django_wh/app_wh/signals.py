from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .handlers import create_handler, update_handler


@receiver(post_save, sender=Order)
def sync_call(sender, instance, created, **kwargs):
    payload = {
        "status": instance.status,
        "label": instance.label,
        "warehouse": instance.warehouse.id,
    }
    if created:
        create_handler(instance, payload)
    else:
        update_handler(instance, payload)