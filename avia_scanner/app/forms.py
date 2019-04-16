from django.forms import Form, ChoiceField, ModelChoiceField, DateField
from django.forms.widgets import SelectDateWidget
from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(Form):
    departure = ChoiceField(label='Город отправления',
                            widget=AjaxInputWidget(url='api/city_ajax',
                                                   attrs={'class': 'inline right-margin'}))
    arrival = ModelChoiceField(queryset=City.objects.all(),
                               label='Город прибытия')
    date = DateField(label='Дата',
                     widget=SelectDateWidget)
