from django.urls import path
from .views import (
    ogloszenieListView,
    ogloszenieDetailView,
    ogloszenieCreateView,
    ogloszenieUpdateView,
    ogloszenieDeleteView,
    UserogloszenieListView
)
from . import views

urlpatterns = [
    path('', ogloszenieListView.as_view(), name='index'),
    path('profil/<str:username>', UserogloszenieListView.as_view(), name='profil-ogloszenia'),
    path('ogloszenie/<int:pk>/', ogloszenieDetailView.as_view(), name='ogloszenie-detal'),
    path('ogloszenie/nowe/', ogloszenieCreateView.as_view(), name='ogloszenie-nowe'),
    path('ogloszenie/<int:pk>/edycja', ogloszenieUpdateView.as_view(), name='ogloszenie-edycja'),
    path('ogloszenie/<int:pk>/usun', ogloszenieDeleteView.as_view(), name='ogloszenie-usun'),
    path('about/', views.about, name='home-about'),
]

