
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Schedule API",
      default_version='v1',
      description="API documentation for Schedule application",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@schedule.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Pour la gestion de l'authentification
    path('appointments/', include('appointment.urls')),  # Inclut les URLs de django-appointment
    path('i18n/', include('django.conf.urls.i18n')),
    path('customers/', include('customer.urls')),
    ##
    path('', include('rendezvous2.urls')),
    path('schedule/', include('schedule.urls')),
    path('agenda/', include('scheduler.urls')),
]

urlpatterns += [
    path('api/v1/', include('rendezvous2.api_urls')),
    path('api/v2/', include('scheduler.api_urls')),
]
## API endpoints docs
urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


# Ajoutez ces lignes pour servir les fichiers média en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)