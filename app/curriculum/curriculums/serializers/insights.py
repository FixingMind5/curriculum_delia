"""Insights Module"""
from rest_framework import serializers

from curriculum.curriculums.models import Insight

class InsightModelSerializer(serializers.ModelSerializer):
    """Insight Model Serializer"""
    class Meta:
        model = Insight
        fields = '__all__'
        
