from django.contrib import admin
from models import Categoria, UserProfile, DiaSemana, Proyecto
from django.contrib.auth.models import User

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'days_of_week', 'tiempo_de', 'tiempo_a',)
	raw_id_fields = ('user', 'localidad',)


admin.site.register(Categoria)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Proyecto)
