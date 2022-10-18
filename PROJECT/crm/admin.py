from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm

# Register your models here.
class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_date', 'comment_text') # Создания поля комментария
    readonly_fields = ('comment_date',)
    extra = 1



class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'orders_status', 'order_name', 'order_phone', 'order_dt') #расширяет админ палень
    list_display_links = ('id', 'order_name') #делает имя к икабельным
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt') #виджет поиска
    list_filter = ('orders_status',) #виджет поиска по статусу
    list_editable = ('orders_status', 'order_phone') #изменения в админ панели
    list_per_page = 10 # количество на странице 
    list_max_show_all = 100 # максимально
    fields = ('id', 'orders_status', 'order_dt', 'order_name', 'order_phone') #отображение полей в карточки
    readonly_fields = ('id', 'order_dt') # неизменяемые поля
    inlines = [Comment,]





admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)



