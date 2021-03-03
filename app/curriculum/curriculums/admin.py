"""Curriculums app admin module"""
from django.contrib import admin

# Models
from curriculum.curriculums.models import Curriculum, Insight, Skill

class CurriculumsAdmin(admin.ModelAdmin):
    """Curriculums admin"""
    pass


class InsightsAdmin(admin.ModelAdmin):
    """Insights admin"""
    pass


class SkillsAdmin(admin.ModelAdmin):
    """Skills admin"""
    pass


admin.site.register(Curriculum, CurriculumsAdmin)
admin.site.register(Insight, InsightsAdmin)
admin.site.register(Skill, SkillsAdmin)
