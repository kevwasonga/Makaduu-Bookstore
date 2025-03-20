from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from model_utils import FieldTracker

class User(AbstractUser):
    tracker = FieldTracker(['verified_publisher'])
    
    is_publisher = models.BooleanField(
        _('publisher status'),
        default=False,
        help_text=_('Designates whether this user can publish books.')
    )
    company_name = models.CharField(max_length=100, blank=True)
    publisher_bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    verified_publisher = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.get_full_name() or self.username

@receiver(post_save, sender=User)
def notify_publisher_verification(sender, instance, **kwargs):
    if instance.is_publisher and instance.verified_publisher:
        # Check if verified_publisher field was just changed to True
        if instance.tracker.has_changed('verified_publisher') and instance.verified_publisher:
            send_mail(
                'Publisher Account Verified',
                'Your publisher account has been verified. You can now access all publisher features.',
                'from@example.com',
                [instance.email],
                fail_silently=True,
            )
