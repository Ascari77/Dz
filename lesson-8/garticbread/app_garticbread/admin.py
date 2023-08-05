from django.contrib import admin
from .models import Advertisement

class AdvAdmin(admin.ModelAdmin):
    list_display = ['id','title','description', 'price', 'created_date', 'updated_date', 'auction']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_false', 'make_auction_true']
    fieldsets = (
        ('общие', {'fields':('title','description')}),
        ('Финансы',{'fields': ('price', 'auction')})
        )

    @admin.action(description='Убрать возможность торгов')
    def make_auction_false(self,request,queryset):
        queryset.update(auction=False)

    @admin.action(description="Вернуть возможность торгов")
    def make_action_true(self, request, queryset):
        queryset.update(auction=True)
# Register your models here.
admin.site.register(Advertisement, AdvAdmin)