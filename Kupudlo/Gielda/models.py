from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User

class Gielda_ogloszenie(models.Model):

    tytul = models.CharField(max_length=50)
    TYP_KONSTRUKCJI = [
        ('KL','KLAPÓWKA'),
        ('TC', 'TACKA'),
        ('WR', 'WRAP'),
        ('AR', 'ARKUSZ'),
        ('PR', 'PRZEKŁADKA'),
        ('AT', 'AUTOMATYCZNE')
    ]
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    typ = models.CharField(max_length=2, choices=TYP_KONSTRUKCJI, default= 'KL')
    #konieczna informacja dla dodającego o wymaganych informacjach typu wymiary/format,
    opis = models.TextField(default='Brak')
    ilosc = models.IntegerField(default=0, validators=[MaxValueValidator(1000000), MinValueValidator(0)])
    data_dodania = models.DateTimeField(default=timezone.now())
    lokalizacja = models.CharField(max_length=30)
    cena = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.tytul