from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class ogloszenie(models.Model):
    #informacje z automatu
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_dodania = models.DateTimeField(auto_now=True)
    #informacje ogólne
    nazwa_opakowania = models.CharField(max_length=100)
    termin_dostawy = models.DateTimeField(default="")
    ilość = models.IntegerField(default=0, validators=[MaxValueValidator(1000000), MinValueValidator(0)])

    treść = models.TextField(blank=True)

    #informacje o opakowaniu

    długość_mm = models.PositiveSmallIntegerField(null=True, blank=True)
    szerokość_mm = models.PositiveSmallIntegerField(null=True, blank=True)
    wysokość_mm = models.PositiveSmallIntegerField(null=True, blank=True)

    class konstrukcje (models.TextChoices):
        fefco_201 = "aa", _('Fefco 201 (klapówka)')
        fefco_422 = "ab", _('Fefco 422 (tacka skladana recznie)')
        fefco_451 = "ac", _('Fefco 451 (tacka klejona)')
        fefco_700 = "ad", _('Fefco 700 (dno automatyczne)')
        inne = "ae", _('Inne')

    konstrukcja = models.CharField(max_length=30, choices=konstrukcje.choices, default=konstrukcje.fefco_201)

    class nadruk(models.TextChoices):
        bez_nadruku = "bz", ('Bez nadruku')
        flexo = "fl",_('Flexo')
        offset = "of",_('Offset')

    typ_nadruku = models.CharField(max_length=2, choices=nadruk.choices, default=nadruk.bez_nadruku)

    LICZBA_KOLOROW = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ]
    ilość_kolorów = models.CharField(max_length=30, choices=LICZBA_KOLOROW, default='0', blank=True)
    powierzchnia_zadruku = models.IntegerField('Powierzchnia zadruku [%]', validators=[MaxValueValidator(100), MinValueValidator(0)], null=True, blank=True)
    #logistyka
    # miejsce dostawy

    class wojewodztwa(models.TextChoices):
        brak = "BK", _("---")
        dolnoslaskie = "DS", _("dolnośląskie")
        kujawsko_pomorskie = "KP", _("kujawsko-pomorskie")
        lubelskie = "LU", _("lubelskie")
        lubuskie = "LB", _("lubuskie")
        lodzkie = "LDZ", _("łódzkie")
        malopolskie = "MP", _("małopolskie")
        mazowieckie = "MZ", _("mazowieckie")
        opolskie = "OP", _("opolskie")
        podkarpackie = "PK", _("podkarpackie")
        podlaskie = "PL", _("podlaskie")
        pomorskie = "PM", _("pomorskie")
        slaskie = "SL", _("śląskie")
        swietokrzyskie = "SK", _("świętokrzyskie")
        warminsko_mazurskie = "WM", _("warmińsko-mazurskie")
        wielkopolskie = "WP", _("wielkopolskie")
        zachodniopomorskie = "ZP", _("zachodniopomorskie")

    województwo = models.CharField(max_length=30, choices=wojewodztwa.choices, default=wojewodztwa.brak)
    miejscowość = models.CharField(max_length=100, default="")
    class palety(models.TextChoices):
        Euro_paleta = "EU", _('Paleta EURO')
        Paleta_UK = "UK", _('Paleta UK')
        Paleta_jednorazowa = "PJ", _('Paleta jednorazowa')

    Paleta = models.CharField(max_length=100, choices=palety.choices, default=palety.Euro_paleta)

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('ogloszenie-detal', kwargs={'pk': self.pk})