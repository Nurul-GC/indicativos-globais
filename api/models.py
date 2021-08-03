from django.db import models

from api.indicativos import GCI


# Create your models here.
class Paises(models.Model):
    PAISES = []
    for p in GCI().paises():
        PAISES.append((p, p))

    pais = models.CharField(max_length=50, choices=PAISES)

    def __str__(self):
        return self.pais


class Indicativos(models.Model):
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    indi_esp = GCI().indicativo_especifico(_pais=pais.name)
    indicativo = models.CharField(max_length=10, default=indi_esp, editable=False)

    def __str__(self):
        return self.indicativo
