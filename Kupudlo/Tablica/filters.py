import django_filters
from .models import ogloszenie

class ogloszenieFilter(django_filters.FilterSet):

    class Meta:
        model = ogloszenie
        fields = ('konstrukcja', 'typ_nadruku')