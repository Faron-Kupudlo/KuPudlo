from django.shortcuts import render, get_object_or_404
from .models import Gielda_ogloszenie
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


class Gielda_oglo(ListView):
    model = Gielda_ogloszenie
    template_name = 'Gielda/gielda.html'
    context_object_name = 'gielda_oglo'

class User_Gielda(ListView):
    model = Gielda_ogloszenie
    template_name = ''
    context_object_name = ''

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))

class Gielda_detal(DetailView):
    model = Gielda_ogloszenie
    template_name = 'Gielda'

class Gielda_new(LoginRequiredMixin, CreateView):
    model = Gielda_ogloszenie
    fields = ["tytul", "typ", "opis", "ilosc", "lokalizacja", "cena"]
    template_name ='Gielda/gielda-create.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class Gielda_delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Gielda_ogloszenie
    template_name = ''
    success_url = ''

    def test_func(self):            #sprawdzenie czy to jest Twoje ogłoszenie, nie można usuwać nieswoich ogłoszeń
        Gielda_ogloszenie = self.get_object()
        if self.request.user == Gielda_oglo.autor:
            return True
        return False

class Gielda_Update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):    #edytowanie ogłoszenia
    model = Gielda_ogloszenie
    fields = ["tytul", "typ", "opis", "ilosc", "lokalizacja", "cena"]
    template_name = ''

    def form_valid(self, form):                                     #sprawdza zalogowanie
        form.instance.autor = self.request.user
        return super().form_valid(form)
    def test_func(self):                                            #sprawdza właścieciela ogłoszenia
        Gielda_ogloszenie = self.get_object()
        if self.request.user == Gielda_ogloszenie.autor:
            return True
        return False







