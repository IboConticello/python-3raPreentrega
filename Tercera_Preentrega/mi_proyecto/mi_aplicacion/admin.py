from django.contrib import admin
from .models import ClaseA

class ClaseAAdmin(admin.ModelAdmin):
    list_display = ('campo_a', 'clase_b', 'clase_c')

    def clase_b(self, obj):
        return obj.clase_b.campo_b

    def clase_c(self, obj):
        return obj.clase_c.campo_c

admin.site.register(ClaseA, ClaseAAdmin)
