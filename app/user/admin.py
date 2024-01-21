
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from user.models import User, File


class CustomUserAdmin(UserAdmin):
    list_display = ('uuid', 'username', 'email', )


class PublicApiClientAdmin(admin.ModelAdmin):
    autocomplete_fields = ("user",)


# class TeamMemberInline(admin.TabularInline):
#     fields = (
#         "email",
#         "first_name",
#         "last_name",
#         "company_name",
#         "date_joined",
#         "last_login",
#         "role",
#         "is_registration_finished",
#     )
#     readonly_fields = (
#         "date_joined",
#         "last_login",
#         "role",
#         "is_registration_finished",
#     )
#     extra = 0
#     show_change_link = True
#
#     model = User
#     verbose_name = "Team Member"
#     verbose_name_plural = "Team Members"
#
#     def has_add_permission(self, request, obj):
#         return False
#
#     def has_change_permission(self, request, obj=None):
#         return False
#
#     def has_delete_permission(self, request, obj=None):
#         return False
#
#
class FileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
    )

#
#
admin.site.register(User, UserAdmin)
admin.site.register(File, FileAdmin)

