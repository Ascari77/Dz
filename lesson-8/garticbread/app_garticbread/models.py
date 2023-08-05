from django.db import models
from django.utils.html import format_html
from django.contrib import admin

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", default=False, help_text="Отметьте если торг уместен")
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color:green">Сегодня в {}</span>', created_time)
        
        return self.created_at.strftime("%d.%m.%Y %H:%M:%S")
    
    @admin.display(description='Дата Обновление')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color:green">Сегодня в {}</span>',created_time)
        return self.updated_at.strftime("%d.%m.%Y %H:%M:%S")

    def __str__(self):
        return f"id = {self.id}, title= {self.title}, price = {self.price}"
    class Meta:
        db_table = "adveratisments"
