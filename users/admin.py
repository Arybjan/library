from django.contrib import admin
from users import models


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "username", "email", "birthday_date",
                    "gender", "occupation", "city", "role", "created_at"]


admin.site.register(models.User, UserAdmin)


class GendersAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(models.Genders, GendersAdmin)
