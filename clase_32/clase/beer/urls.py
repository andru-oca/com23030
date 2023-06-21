from django.contrib import admin
from django.urls import path

from .views import LandingPage ,ContactoPage , WhoAreWe

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", LandingPage.as_view(), name="landing_page" ),
    path("contacto", ContactoPage.as_view(), name="contacto" ),
    path("quienes_somos", WhoAreWe.as_view(), name="quienes_somos" ),
]
