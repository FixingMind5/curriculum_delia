"""Curriculum serializers module"""
from rest_framework import serializers

# Models
from curriculum.curriculums.models import Curriculum

from curriculum.curriculums.serializers.skills import SkillModelSerializer
from curriculum.curriculums.serializers.insights import InsightModelSerializer

class CurriculumModelSerializer(serializers.ModelSerializer):
    """Curriculum model serializer"""
    skills = SkillModelSerializer(
        many=True,
        read_only=True,
        source="skill_set"
    )
    insights = InsightModelSerializer(
        many=True,
        read_only=True,
        source="insight_set"
    )

    class Meta:
        """Meta class"""
        model = Curriculum
        fields = (
            'fullname',
            'position',
            'description',
            'birthdate',
            'address',
            'phone_number',
            'email',
            'website',
            'facebook',
            'instagram',
            'twitter',
            'linkedin',
            'skills',
            'insights'
        )
        
