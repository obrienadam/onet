from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', view=TemplateView.as_view(template_name='pages/index.html'), name='index')
]