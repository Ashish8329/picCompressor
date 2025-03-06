from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
