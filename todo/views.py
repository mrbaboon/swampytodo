from django.shortcuts import render
from django.views.generic import TemplateView


todo_view = TemplateView.as_view(template_name='todo.html')