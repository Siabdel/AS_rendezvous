from django.urls import path
from . import views 
from . import api_views 

app_name = 'customer'

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    ## Create
    path('create_client/', views.ClientCreateView.as_view(), name='client-create'),
     # Clients
    path("", views.ClientListView.as_view(), name="client-list"),
    path("list/", views.ClientListView.as_view(), name="client-list"),
    path("<int:pk>/", views.ClientDetailView.as_view(), name="client-detail"),
    path("edit/<int:pk>/", views.ClientUpdateView.as_view(), name="client-edit"),
    path("del/<int:pk>/", views.ClientDeleteView.as_view(), name="client-delete",),
]

#---------
# API's
#---------
urlpatterns += [
    path('api/v1/clients/', api_views.ClientListView.as_view(), name='api-client-list'),
    path('api/v1/clients/<int:pk>/', api_views.ClientDetailView.as_view(), name='api-client-detail'),
]


