"""Skills model module"""
from django.db import models
from curriculum.curriculums.models import Curriculum

class Skill(models.Model):
    """Skill model"""

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        error_messages={
            "null": "No puedes dejar a tu habilidad sin nombre",
            "max_length": "Procura que sea sólo una palabra... corta"
        }
    )
    level = models.IntegerField(default=1)
    skill_type = models.CharField(
        max_length=5,
        null=False,
        blank=False,
        choices=[
            ('Soft', 'Soft'),
            ('Hard', 'Hard')
        ],
        default='Soft'
    )

    curriculum = models.ForeignKey(
        Curriculum,
        on_delete=models.CASCADE,
    )
