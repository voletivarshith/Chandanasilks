from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import wholesaleuser,Cart
@receiver(post_save, sender=User)
def wholesaleusercreation(sender,instance,created,*args,**kwargs):
    if created:
        user = wholesaleuser.objects.create(user=instance)
        user.save()

