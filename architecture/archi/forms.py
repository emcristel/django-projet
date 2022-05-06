from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class ArchitecteForm(ModelForm):
    class Meta:
        model=models.Architecte
        fields=('archit','style',)
        labels = {
            'archit': _('nom architecte'),
            'style': _('style'),
        }

class TableForm(ModelForm):
    class Meta:
        model=models.Table
        fields=('nom','creation','localisation','type_oeuvre','architecte')
        labels = {
            'nom': _('nom'),
            'creation': _('date de creation'),
            'localisation': _('localisation'),
            'type_oeuvre': _('type oeuvre'),
            'architecte': _('architecte')
        }
        localized_fields = ('date_creation',)

