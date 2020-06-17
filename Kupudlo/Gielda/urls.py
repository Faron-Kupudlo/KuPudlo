from django.urls import path
from .views import (
    Gielda_oglo,
    Gielda_detal,
    User_Gielda,
    Gielda_new,
    Gielda_delete,
    Gielda_Update
)
from . import views

urlpatterns = [
    path('', Gielda_oglo.as_view(), name='gielda-index'),
    path('<str:username>/', User_Gielda.as_view(), name='profil-gielda'),
    path('<int:pk>/', Gielda_detal.as_view(), name='gielda-detal'),
    path('nowe/', Gielda_new.as_view(), name='gielda-nowe'),
    path('<int:pk>/edycja', Gielda_Update.as_view(), name='gielda-edycja'),
    path('<int:pk>/usun', Gielda_delete.as_view(), name='gielda-usun'),
]
