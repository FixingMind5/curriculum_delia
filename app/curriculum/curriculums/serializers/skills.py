"""Skill serializers module"""
from rest_framework import serializers

# Models
from curriculum.curriculums.models import Skill

class SkillModelSerializer(serializers.ModelSerializer):
    """Skill Model Serializer"""
    
    class Meta:
        """Meta class"""
        model = Skill
        fields = '__all__'