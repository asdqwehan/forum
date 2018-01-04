from django.contrib import admin

# Register your models here.
from myforum.models import Bbs, Catepory, Comments

#定制样式
class Bbs_admin(admin.ModelAdmin):
    #以列显示内容
    list_display = ('title', 'author', 'add_time')
    #过滤
    list_filter = ('add_time',)
    #搜索,注：author需外键
    search_fields = ('title', 'author__user__username')


admin.site.register(Bbs, Bbs_admin)
admin.site.register(Catepory)
admin.site.register(Comments)
