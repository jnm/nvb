from django.contrib import admin
from models import (
    Bike, Youth, Adult, Stand, SkillCategory, Skill, Part, Activity,
    ActivityPartCount)

class ActivityPartCountInline(admin.TabularInline):
    model = ActivityPartCount

class ActivityAdmin(admin.ModelAdmin):
    inlines = (ActivityPartCountInline,)

# Register your models here.
admin.site.register(Bike)
admin.site.register(Youth)
admin.site.register(Adult)
admin.site.register(Stand)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(Part)
admin.site.register(Activity, ActivityAdmin)
