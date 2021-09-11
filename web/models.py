from django.db import models

# Create your models here.
class hospital(models.Model):
    """Model definition for hospital."""

    # TODO: Define fields here
    hospitalName = models.CharField(max_length=255)
    date_ctrated = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for hospital."""

        verbose_name = 'hospital'
        verbose_name_plural = 'hospitals'

    def __str__(self):
        """Unicode representation of hospital."""
        pass
    
class patient(models.Model):
    """Model definition for patient."""

    # TODO: Define fields here
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    sex = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    medic = models.CharField(max_length=255)
    date_ctrated = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for patient."""

        verbose_name = 'patient'
        verbose_name_plural = 'patients'

    def __str__(self):
        """Unicode representation of patient."""
        pass

class physician(models.Model):
    """Model definition for physician."""

    # TODO: Define fields here
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    expertise = models.CharField(max_length=50)
    hospital = models.CharField(max_length=255)
    date_ctrated = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for physician."""

        verbose_name = 'physician'
        verbose_name_plural = 'physicians'

    def __str__(self):
        """Unicode representation of physician."""
        pass
