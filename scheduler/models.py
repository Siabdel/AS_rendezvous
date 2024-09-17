from django.db import models

# Create your models here.


    Gestion des événements récurrents :
        rule : ForeignKey vers un modèle Rule pour définir des règles de récurrence
        end_recurring_period : DateTimeField pour la fin de la période de récurrence
    Méthodes pour gérer les occurrences :
        get_occurrences() : retourne les occurrences entre deux dates
        occurrences_after() : génère les occurrences après une date donnée
        get_occurrence() : récupère une occurrence spécifique
    Fonctionnalités de relations :
        create_relation() : crée une relation avec un objet générique
        get_related_objects() : récupère les objets liés à l'événement
    Méthodes utilitaires :
        get_absolute_url() : génère l'URL de l'événement
        str() : représentation textuelle de l'événement
    Gestion des chevauchements :
        has_overlap() : vérifie si l'événement chevauche d'autres événements
    Intégration avec le système de permissions Django

