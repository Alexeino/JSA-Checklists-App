from django.contrib import admin

from .models import Checklist, JSAChecklist, Question

# Register your models here.

admin.site.register(Question)
admin.site.register(Checklist)
admin.site.register(JSAChecklist)