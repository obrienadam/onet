# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

import cantera as ct

from django.shortcuts import render

# Create your views here.
class Test(TemplateView):
    template_name = 'pages/test.html'

    def get_context_data(self, **kwargs):
        water = ct.Solution('water.cti', 'liquid_water')
        kwargs['name'] = water.name
        kwargs['TP'] = water.TP
        return super(Test, self).get_context_data(**kwargs)