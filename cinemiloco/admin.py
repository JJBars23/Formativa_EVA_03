from django.contrib import admin
from django.utils.html import format_html
from .models import Pelicula, Genero, tickets

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'precio', 'disponible')
    readonly_fields = ('miniatura',)
    fields = ('titulo', 'miniatura', 'imagen')

    @admin.display(description='Vista previa')
    def miniatura(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="height:60px; border-radius:4px;">',
                obj.imagen.url
                )
        return '-'


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ('pelicula', 'cantidad', 'fecha_compra')