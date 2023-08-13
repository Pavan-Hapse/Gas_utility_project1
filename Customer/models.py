from django.db import models

# Create your models here.

class ServiceRequest(models.Model):
    Service_Types = (
        ('Gas Leak', 'Gas Leak'),
        ('Meter Installation', 'Meter Installation'),
        ('Billing Inquiry','Billing Inquiry'),
    )

    status = models.CharField(max_length = 20, choices = Service_Types, default = 'Gas Leak' )
    details = models.TextField()
    attachments = models.FileField(upload_to = 'attachments/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"ServiceRequest #{self.id}: {self.status}"