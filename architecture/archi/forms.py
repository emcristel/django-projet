from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class ArchitecteForm(ModelForm):
    class Meta:
        model=models.Architecte
        fields=('archit','oeuvre',)
        labels = {
            'archit': _('nom architecte'),
            'oeuvre': _('oeuvre'),
        }

class OeuvreForm(ModelForm):
    class Meta:
        model=models.Oeuvre
        fields=('nom','creation','localisation','type_oeuvre',)
        labels = {
            'nom': _('nom'),
            'creation': _('date de creation'),
            'localisation': _('localisation'),
            'type_oeuvre': _('type oeuvre'),
        }
        localized_fields = ('date_creation',)

