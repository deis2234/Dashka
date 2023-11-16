from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Group
from django.contrib import admin
from .models import Day, Lesson, WeeklySchedule

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['surname', 'name', 'middlename', 'phone_number', 'email']
    list_display_links = ['surname', 'name', 'middlename', 'phone_number', 'email']

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Пользовательская информация',
            {
                'fields': (
                    'surname',
                    'name',
                    'middlename',
                    'fullname',
                    'phone_number',
                    'is_account_confirmed',
                    'groups',
                )
            }
        ),
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Пользовательская информация',
            {
                'fields': (
                    'surname',
                    'name',
                    'middlename',
                    'fullname',
                    'phone_number',
                    'is_account_confirmed'
                )
            }
        ),

    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Group)
admin.site.register(Day)
admin.site.register(Lesson)
admin.site.register(WeeklySchedule)