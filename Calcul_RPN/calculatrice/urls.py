from django.urls import path
from . import views
urlpatterns = [
    path("stack", views.push, name = "stack"),
    path("stack/<int:pk>", views.Delet, name = "stack"),
    path("op/<int:fk>", views.operation, name = "op")
]