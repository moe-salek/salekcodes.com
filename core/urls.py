from django.urls import path

from core.views import StaticTemplateView

urlpatterns = [
    path(
        '',
        StaticTemplateView.as_view(template_name='salekcodes-static/index.html'),
        name='static_template_view',
    ),
]
