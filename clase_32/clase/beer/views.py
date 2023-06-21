from django.views.generic import TemplateView


class LandingPage(TemplateView):
    template_name = "bloque/landing_page.html"
    extra_context = {
        "titulo" : "pagina de inicio"
    }


class ContactoPage(TemplateView):
    template_name = "bloque/contacto.html"
    extra_context = {
        "titulo" : "pagina de contacto"
    }

class WhoAreWe(TemplateView):
    template_name = "bloque/quienes_somos.html"
    extra_context = {
        "titulo" : "pagina de quienes somos"
    }