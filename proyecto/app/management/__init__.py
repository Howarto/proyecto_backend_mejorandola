#coding:utf-8
# Howarto: "Magia negra para que con syncdb se creen los objetos de dias de la semana"
# Consejo => Haced un snippet y automatizad todo'para no trabajar

from django.db.models import signals
from app import models as app
from app.models import DiaSemana

def crear_dias_semana(app, created_models, interactive, **kwargs):
    if DiaSemana in created_models:
        lunes = DiaSemana(nombre='Lunes')
        lunes.save()

        martes = DiaSemana(nombre='Martes')
        martes.save()

        miercoles = DiaSemana(nombre='Miércoles')
        miercoles.save()

        jueves = DiaSemana(nombre='Jueves')
        jueves.save()

        viernes = DiaSemana(nombre='Viernes')
        viernes.save()

        sabado = DiaSemana(nombre='Sábado')
        sabado.save()

        domingo = DiaSemana(nombre='Domingo')
        domingo.save()

signals.post_syncdb.connect(crear_dias_semana, sender=app, dispatch_uid='app.management.crear_dias_semana')