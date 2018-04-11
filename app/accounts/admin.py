from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import Profiel


class ProfielInline(admin.StackedInline):
    model = Profiel
    can_delete = False
    verbose_name_plural = 'Profiel'
    fk_name = 'gebruiker'

    readonly_fields = ["avatar_display"]

    def avatar_display(self, obj):
        return mark_safe(
            '<img src="{url}" width="150" height="150" class="lazyload" />'.format(
                url=obj.static_avatar_url(),
                width=obj.avatar.width,
                height=obj.avatar.height,
            )
        )


class CustomUserAdmin(UserAdmin):
    inlines = (ProfielInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
