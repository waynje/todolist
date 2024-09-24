from django.contrib import admin
from .models import Category, Task

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'user', 'execution_date', 'complete')
    search_fields = ('name', 'description')
    ordering = ('execution_date',)
    list_filter = ('category', 'user', 'execution_date', 'complete')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('category', 'user')