from django import template
from django.utils.safestring import mark_safe
from decimal import Decimal
from django.conf import settings
from ..models import Translation

register = template.Library()


@register.filter(name='translate')
def translate(phrase, language):

    translation = Translation.objects.filter(phrase=phrase, language=language, is_deleted=0).first()
    if translation:
        return mark_safe(translation)
    else:
        return mark_safe(phrase)