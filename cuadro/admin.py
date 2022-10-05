from django.contrib import admin

from.models import Ingreso_notas
admin.site.register(Ingreso_notas)

from.models import Institucion_env
admin.site.register(Institucion_env)

from.models import Expediente
admin.site.register(Expediente)

from.models import Victima
admin.site.register(Victima)
# Register your models here.

from.models import hijos
admin.site.register(hijos)

from.models import Agresor
admin.site.register(Agresor)

from.models import Medidas
admin.site.register(Medidas)

