from django.db import models
from django.utils.translation import gettext_lazy as _

class ClassTypes(models.TextChoices):
        ECONOMIC = 'ECON', _('Economic')
        EXECUTIVE = 'EXEC', _('Executiva')
        FIRST_CLASS = 'STCL', _('First class')
