from django.contrib import admin

# Register your models here.
from UserApi.models import UserVerification, User

# Register your models here.
admin.site.register(User)
admin.site.register(UserVerification)
