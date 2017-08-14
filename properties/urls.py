from django.conf.urls import url

import views

urlpatterns = [
    url(r'^solutions/(?P<input>[_\w\W]+)/$', view=views.SolutionView.as_view(), name='solutions'),
]