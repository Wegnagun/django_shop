from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Мой интернет магазин'
admin.site.index_title = 'Разделы админки магазина'
admin.site.site_title = 'Админка магазина'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
]
