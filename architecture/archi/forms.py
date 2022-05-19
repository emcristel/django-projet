from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class ArchitecteForm(ModelForm):
    class Meta:
        model=models.Architecte
        fields=('archit','style',)
        labels = {
            'archit': _('NOM ARCHITECTE'),
            'style': _('STYLE'),
        }

class OeuvreForm(ModelForm):
    class Meta:
        model=models.Oeuvre
        fields=('nom','creation','localisation','type_oeuvre','architecte')
        labels = {
            'nom': _('NOM'),
            'creation': _('DATE DE CREATION'),
            'localisation': _('LOCALISATION'),
            'type_oeuvre': _('TYPE OEUVRE'),
            'architecte': _('ARCHITECTE')
        }

