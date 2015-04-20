from django.shortcuts import render
from django.views.generic import TemplateView


monitor_view = TemplateView.as_view(template_name='monitor.html')