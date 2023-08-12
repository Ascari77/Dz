from django.contrib import admin
from .models import Advertisement

class AdvAdmin(admin.ModelAdmin):
    list_display = ['id','title','description', 'price','user','created_date','updated_date','auction','miniature']
    list_filter = ['auction','created_at']
    actions = ['make_auction_false','make_auction_true']
    fieldsets = [
        ("общие", {'fields':['title','description','image']}),
        ("Финансы", {'fields': ['price','auction','user']}),
    ]

    @admin.action(description="Убрать возможность торгов")
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Вернуть возможность торгов")
    def make_auction_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvAdmin)
# Register your models here.
