from django.db import models

from api.indicativos import GCI


# Create your models here.
class Indicativos(models.Model):
    PAISES = []
    INDICATIVOS = None
    for p in GCI().paises():
        INDICATIVOS = GCI().indicativo_especifico(_pais=p)
        PAISES.append((INDICATIVOS, p))

    pais = models.CharField(max_length=50, choices=PAISES, unique=True)

    def __str__(self):
        return self.pais
