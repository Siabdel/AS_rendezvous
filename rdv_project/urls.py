
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Pour la gestion de l'authentification
    path('appointments/', include('appointment.urls')),  # Inclut les URLs de django-appointment
    path('i18n/', include('django.conf.urls.i18n')),
    path('customers/', include('customer.urls')),
    path('', include('rendezvous2.urls')),
]

urlpatterns += [
    path('api/', include('rendezvous2.api_urls')),
]


# Ajoutez ces lignes pour servir les fichiers média en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)