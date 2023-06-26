from django.urls import path
from django.views.static import serve 

from . import views

app_name = "blackbook"

urlpatterns = [
    path("", views.index, name="index"),
    path("marketplace/", views.marketplace, name="marketplace"),
    path("data/completely-safe-url", views.tracking, name="completelysafeurl"),
]