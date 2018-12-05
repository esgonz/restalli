from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "comun/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HomePageViewMovil(TemplateView):

    template_name = "comun/dashboard_movil.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context