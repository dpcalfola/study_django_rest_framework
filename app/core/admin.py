"""
Django admin customization
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from . import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users"""

    # 'ordering', 'list_display' are come out from BaseUserAdmin
    ordering = ['id']
    list_display = ['email', 'name']

    fieldsets = (
        (
            # None means that there's no title of the fieldset
            None,
            {
                'fields':
                    (
                        'email',
                        'password'
                    )
            }
        ),
        (
            # 'Permissions' is the title of the fieldset
            _('Permissions'),
            {
                'fields':
                    (
                        'is_active',
                        'is_staff',
                        'is_superuser'
                    )
            }
        ),
        (
            # Title of ...
            _('Important dates'),
            {
                'fields':
                    (
                        # Warning: Do not miss Comma(,)
                        # Value of 'fields' must be tuple
                        # Comma makes value to tuple - python syntax
                        'last_login',
                    )
            }
        )
    )

    readonly_fields = ['last_login']


admin.site.register(models.User, UserAdmin)
