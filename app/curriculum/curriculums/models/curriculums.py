"""Curriculum Model module"""
from django.db import models

class Curriculum(models.Model):
    """Curriculum model"""
    
    fullname = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        error_messages={
            "null": "Este campo no puede estar vacio" 
        },
        help_text="Nombre que aparecerá en el curriculum"
    )
    position = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        error_messages={
            "null": "Este campo no puede estar vacio",
            "max_length": "Has excedido la cantidad de letras disponible"
        },
        help_text="Tu puesto actual"
    )
    description = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        error_messages={
            "max_length": "Tiene que ser una descripción corta de 300 carácteres"
        },
        help_text="Breve descripción de ti"
    )
    birthdate = models.DateField(
        help_text="Tu fecha de nacimiento",
        null=False,
        blank=False,
        error_messages={
            "null": "Este campo no puede estar vacio"
        },
    )
    address = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        error_messages={
            "max_length": "Tiene que ser menor de 300 carácteres"
        },
        help_text="(Opcional) Tu dirección"
    )
    phone_number = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        error_messages={
            "null": "Necesitas un número donde te contacten"
        },
        help_text="Máx. 15 dígitos"
    )
    email = models.EmailField(
        max_length=100,
        null=False,
        blank=False,
        error_messages={
            "null": "Necesitas un correro donde te contacten",
            "max_length": "Has excedido el numero disponible de dígitos"
        },
    )
    website = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    facebook = models.URLField(
        null=True,
        blank=True
    )
    instagram = models.URLField(
        null=True,
        blank=True
    )
    twitter = models.URLField(
        null=True,
        blank=True
    )
    linkedin = models.URLField(
        null=True,
        blank=True
    )

    
