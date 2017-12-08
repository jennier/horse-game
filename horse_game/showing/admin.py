from django.contrib import admin

# Register your models here.
from .models import Discipline, Show, ClassName

admin.site.register(Discipline)
admin.site.register(ClassName)
admin.site.register(Show)