"""Insights module."""
from django.db import models

# Models
from curriculum.curriculums.models import Curriculum

# Utilities
from datetime import datetime

NULL_ERROR_MESSAGE = "No puedes dejar este campo vacío"

class Insight(models.Model):
    """Insight model"""
    INSTIGHT_TYPE_CHOICES = [
        ('Experience', 'experience'),
        ('Education', 'education')
    ]

    enterprise_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        error_messages={
            "null": NULL_ERROR_MESSAGE,
        },
        help_text=(
            "El nombre de la empresa donde trabajaste"
        )
    )
    position = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        error_messages={
            "null": NULL_ERROR_MESSAGE,
        },
        help_text=(
            "El cargo que desarrollaste"
        )
    )
    beggining_date = models.DateField(
        null=False,
    )
    end_date = models.DateField(
        default=datetime.now,
        help_text=(
            "Por favor define esta fecha "
            "de lo contrario será la actual y "
            "se tomara como trabajo actual"
        )
    )

    description = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        error_messages={
            "null": NULL_ERROR_MESSAGE,
        },
        help_text=(
            "Una breve descripción de lo que hiciste"
        )
    )
    curriculum = models.ForeignKey(
        Curriculum,
        on_delete=models.CASCADE,
    )
    insight_type = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=INSTIGHT_TYPE_CHOICES,
    )
