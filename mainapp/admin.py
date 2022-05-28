from django.contrib import admin

from mainapp.models import TestCategory, Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    fields = ('title', 'description', ('category', ))
    search_fields = ('title', )
    ordering = ('title', )


@admin.register(TestCategory)
class TestCategory(admin.ModelAdmin):
    list_display = ('name', 'description')
