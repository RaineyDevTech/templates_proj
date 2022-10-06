from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
@stringfilter
def repeat(text, times=2):
    return text * times