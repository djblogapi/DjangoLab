from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from user.models import File, User


class CustomUserAdmin(UserAdmin):
    list_display = ('uuid', 'username', 'email', 'preview')
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", 'face',
                                         'encoding'
                                         )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ("uuid", 'encoding')

    def preview(self, obj):
        if not obj.face:
            return

        return mark_safe('<img src="http://localhost/media/%s" width="150" height="150" />' % obj.face)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.encode_img()


class PublicApiClientAdmin(admin.ModelAdmin):
    autocomplete_fields = ("user",)


class FileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
        "preview",
        "user"
    )

    def preview(self, obj):
        return mark_safe('<img src="http://localhost/media/%s" width="150" height="150" />' % obj.image)


admin.site.register(User, CustomUserAdmin)
admin.site.register(File, FileAdmin)
