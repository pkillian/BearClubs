from django import template
from datetime import datetime, date

register = template.Library()

@register.inclusion_tag('layout/header.html')
def show_header():
    """ Render header template with given parameters """
    return {};
