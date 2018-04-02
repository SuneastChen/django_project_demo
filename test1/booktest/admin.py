from django.contrib import admin
# Register your models here.
from booktest.models import *

# 为了让后台显示完整的数据库字段
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']
    search_fields = ['title']
    list_filter = ('title',)
    ordering = ('id',)

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'gender', 'book']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)


