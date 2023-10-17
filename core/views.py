from django.views.generic import TemplateView


class StaticTemplateView(TemplateView):
    template_name = 'frontend/salekcodes-static/index.html'
