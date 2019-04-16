import time
import random

from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


class TicketPageView(FormMixin, TemplateView):
    form_class = SearchTicket
    template_name = 'app/ticket_page.html'


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    city_from_request = request.GET.get('term')
    cities_list = list()
    for city in City.objects.filter(name__contains=city_from_request):
        cities_list.append(city.name)
    cache.set('cities', cities_list)
    results = cache.get('cities')
    print(results)
    return JsonResponse(results, safe=False)
