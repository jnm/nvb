from django.contrib import admin
from models import (
    Bike, Youth, Adult, Stand, SkillCategory, Skill, Part, ShopSession,
    Activity, ActivitySkill, ActivityPart)

class ActivitySkillInline(admin.TabularInline):
    model = ActivitySkill

class ActivityPartInline(admin.TabularInline):
    model = ActivityPart

class ActivityAdmin(admin.ModelAdmin):
    inlines = (ActivitySkillInline, ActivityPartInline,)

# Register your models here.
admin.site.register(Bike)
admin.site.register(Youth)
admin.site.register(Adult)
admin.site.register(Stand)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(Part)
admin.site.register(ShopSession)
admin.site.register(Activity, ActivityAdmin)
