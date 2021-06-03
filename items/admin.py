from django.contrib import admin
from .models import ListContainer, ListItem


class ListItemInline(admin.TabularInline):
    model = ListItem
    raw_id_fields = ['parent']
    extra = 1


@admin.register(ListContainer)
class ListContainerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_editable = ['name']
    inlines = [ListItemInline]


@admin.register(ListItem)
class ListItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'parent']
    list_editable = ['name']
    raw_id_fields = ['parent']
