import string
from importlib import import_module
import warnings

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save
from django.core.exceptions import FieldDoesNotExist, ObjectDoesNotExist
from django.db import models, DEFAULT_DB_ALIAS
from django.dispatch import receiver
from django.utils import timezone
from django.utils.functional import SimpleLazyObject
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    code = models.CharField(max_length=50, unique=True, editable=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    created_at = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=100, blank=True, null=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    company_logo = models.ImageField(blank=True)
    phone_number = PhoneNumberField(blank=True)
    
    class Meta:
        ordering = ('first_name', 'last_name', )
        verbose_name: "Customer"
        verbose_name_plural: "Customers"  # client 
        unique_together = [('email', ), ('email', 'first_name', 'last_name' ),]

    def __str__(self):
        return f"{self.code}-{self.first_name} {self.last_name}"
    
    #@property 
    def get_absolute_url(self):
        return reverse("customer:client-edit", kwargs={"pk": self.pk})

    def __repr__(self):
        return f"Custom: {self.first_name} {self.last_name}"

    def generate_invoice_number(self):
        today = timezone.now()
        year = today.strftime("%Y")
        month = today.strftime("%m")
        day = today.strftime("%d")

        # Générer le numéro de facture
        # Nous utilisons self.pk pour l'ID de la facture, qui sera disponible après la sauvegarde initiale
        new_code = f"CLI-{year}{month}{day}-00{self.pk:06d}"
        return new_code

    def save(self, *args, **kwargs):
        # Sauvegarder d'abord pour obtenir un ID (self.pk)
        super().save(*args, **kwargs)
        
        # Générer et sauvegarder le numéro de facture si ce n'est pas déjà fait
        if not self.code:
            self.code = self.generate_invoice_number()
            super().save(update_fields=['code'])



@receiver(user_logged_in)
def handle_customer_login(sender, **kwargs):
    """
    Update request.customer to an authenticated Customer
    """
    try:
        kwargs['request'].customer = kwargs['user'].customer
    except (AttributeError, ObjectDoesNotExist):
        kwargs['request'].customer = SimpleLazyObject(lambda: Customer.objects.get_from_request(kwargs['request']))


@receiver(user_logged_out)
def handle_customer_logout(sender, **kwargs):
    """
    Update request.customer to a visiting Customer
    """
    # defer assignment to anonymous customer, since the session_key is not yet rotated
    kwargs['request'].customer = SimpleLazyObject(lambda: Customer.objects.get_from_request(kwargs['request']))

