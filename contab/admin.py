from django.contrib import admin
from contab.models import Material,Compra,Stock,Firme,StockFirme,PedidoFirme

# Register your models here.

class StockAdmin(admin.ModelAdmin):
	list_display = ('material','canti','total_cant','total_soles','actualizado')


admin.site.register(Material,)
admin.site.register(Compra,)
admin.site.register(Stock,StockAdmin)
admin.site.register(Firme)
admin.site.register(PedidoFirme,)
admin.site.register(StockFirme)