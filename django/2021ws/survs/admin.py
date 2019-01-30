from django.contrib import admin
from .models import Choice, Question

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('content', 'votes',)

admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)
