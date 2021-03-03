"""Curriculums viewsets module"""
from rest_framework import mixins, viewsets

from curriculum.curriculums.serializers import CurriculumModelSerializer
from curriculum.curriculums.models import Curriculum


class CurriculumViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Curriculum viewset"""
    queryset = Curriculum.objects.all()

    def get_serializer_class(self):
        """Retrieve serializer based on action"""
        
        return CurriculumModelSerializer