"""
Le modèle Appointment comprend généralement les champs suivants :
* customer (ForeignKey):
Lié au modèle User de Django ou à un modèle Customer personnalisé.
Représente le client qui a pris le rendez-vous.

* service (ForeignKey): Lié au modèle Service défini dans django-appointment.
Représente le service pour lequel le rendez-vous est pris.

* date_time (DateTimeField): La date et l'heure du rendez-vous.

* status (CharField): Le statut du rendez-vous (par exemple : "scheduled", "completed", "cancelled").
Généralement implémenté avec des choix prédéfinis.

* created_at (DateTimeField): La date et l'heure de création du rendez-vous.
Généralement avec auto_now_add=True.

* updated_at (DateTimeField): La date et l'heure de la dernière mise à jour du rendez-vous.
Généralement avec auto_now=True.

* notes (TextField): Un champ optionnel pour des notes supplémentaires sur le rendez-vous.
"""
from django.db import models
from django.conf import settings
from appointment.models import Appointment as BaseAppointment, Service as BaseService

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rendezvous2_customer')
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class CustomService(BaseService):
    # Vous pouvez ajouter des champs supplémentaires ici si nécessaire
    class Meta:
        app_label = 'rendezvous2'

    def __str__(self):
        return self.name

class CustomAppointment(BaseAppointment):
    service = models.ForeignKey(CustomService, on_delete=models.CASCADE, related_name='rendezvous2_appointments')
    
    class Meta:
        app_label = 'rendezvous2'

    def __str__(self):
        return f"Rendez-vous pour {self.client} - {self.service}"

class StaffMember(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rendezvous2_staffmember')
    services = models.ManyToManyField(CustomService, related_name='rendezvous2_staffmembers')

    def __str__(self):
        return self.user.username

class Availability(models.Model):
    DAY_OF_WEEK_CHOICES = [
        (0, 'Lundi'),
        (1, 'Mardi'),
        (2, 'Mercredi'),
        (3, 'Jeudi'),
        (4, 'Vendredi'),
        (5, 'Samedi'),
        (6, 'Dimanche'),
    ]
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE, related_name='availabilities')
    day_of_week = models.IntegerField(choices=DAY_OF_WEEK_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.staff_member} - {self.get_day_of_week_display()} {self.start_time}-{self.end_time}"

class Conflict(models.Model):
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE, related_name='conflicts')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"{self.staff_member} - {self.date} {self.start_time}-{self.end_time}"