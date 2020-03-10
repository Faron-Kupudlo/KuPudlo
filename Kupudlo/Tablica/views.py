from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
from .models import ogloszenie
from .filters import ogloszenieFilter

from django.http import HttpResponse





class ogloszenieListView(ListView):         #View strony głównej, używamy wbudowanego modułu ListView
    model = ogloszenie                      #wybieramy co będzie naszym modelem w tym View (ogloszenie)
    template_name = 'Tablica/home.html'     #nazwa pliku html
    context_object_name = 'ogloszenie'
    ordering = ['-data_dodania']            #segregowanie listy po dacie dodania
    paginate_by = 5                         #tyle powinno wyświetlać się ogłoszeń na jednej stronie



    def get_context_data(self, **kwargs):                   #moduł filtrów
        context = super().get_context_data(**kwargs)
        context['filter'] = ogloszenieFilter(self.request.GET, queryset=self.get_queryset())
        return context

class UserogloszenieListView(ListView):    #podobnie jak View dla wyświetlania z tą różnicą, że dla jednego użytkownika
    model = ogloszenie
    template_name = 'Tablica/profil-ogloszenia.html'
    context_object_name = 'ogloszenie'
    paginate_by = 5

    def get_queryset(self):                 #ten def odpowiada za pogranie uzytkownika oraz posegregowanie wg daty
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return ogloszenie.objects.filter(autor=user).order_by('-data_dodania')



class ogloszenieDetailView(DetailView):     #z wbudowanego modułu wyświetlanie detali ogłoszenia
    model = ogloszenie
    template_name = 'Tablica/ogloszenie-detal.html'

class ogloszenieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #też wbudowany moduł, tym razem do usuwania ogłoszeń
    model = ogloszenie
    template_name = 'Tablica/ogloszenie-usun.html'
    success_url = '/'

    def test_func(self):            #sprawdzenie czy to jest Twoje ogłoszenie, nie można usuwać nieswoich ogłoszeń
        ogloszenie = self.get_object()
        if self.request.user == ogloszenie.autor:
            return True
        return False


class ogloszenieCreateView(LoginRequiredMixin, CreateView):     #moduł tworzenia nowego ogłoszenia
    model = ogloszenie
    fields = ['nazwa_opakowania', 'treść', 'termin_dostawy', 'konstrukcja',
              'typ_nadruku', 'ilość_kolorów', 'powierzchnia_zadruku',
              'Paleta', 'ilość', 'długość_mm','szerokość_mm',
              'wysokość_mm', 'województwo', 'miejscowość']
    template_name = 'Tablica/ogloszenie-nowe.html'

    def form_valid(self, form):                                 #sprawdza zalogowanie, jeśli wylogowany to przekierowuje na stronę zalogowania
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ogloszenieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):    #edytowanie ogłoszenia
    model = ogloszenie
    fields = ['nazwa_opakowania', 'treść', 'termin_dostawy', 'konstrukcja',
              'typ_nadruku', 'ilość_kolorów', 'powierzchnia_zadruku',
              'Paleta', 'ilość', 'długość_mm','szerokość_mm',
              'wysokość_mm', 'województwo', 'miejscowość']
    template_name = 'Tablica/ogloszenie-nowe.html'

    def form_valid(self, form):                                     #sprawdza zalogowanie
        form.instance.autor = self.request.user
        return super().form_valid(form)
    def test_func(self):                                            #sprawdza właścieciela ogłoszenia
        ogloszenie = self.get_object()
        if self.request.user == ogloszenie.autor:
            return True
        return False

def about(request):                                                 #View od "O nas"
    return render(request, 'Tablica/about.html', {'title':'info'})


