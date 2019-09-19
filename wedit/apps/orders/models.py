from django.db import models
from wedit.apps.profiles.models import Profile


class Order(models.Model):
    """ Design order. """

    STATUS_CHOICES = (('pending', 'Pending'), ('approved',
                                               'Approved'), ('rejected', 'Rejected'))
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order_title = models.TextField(max_length=255)
    order_summary = models.TextField()
    order_file = models.CharField(max_length=255)
    description_file = models.CharField(max_length=255)
    order_status = models.CharField(
        choices=STATUS_CHOICES, default='pending', max_length=30)
