from django.conf.urls import url
from django.views.generic import TemplateView

import views

urlpatterns = [
    url(r'^$', view=TemplateView.as_view(template_name='pages/index.html'), name='index'),
    url(r'^test/$', view=views.Test.as_view(), name='test')
]