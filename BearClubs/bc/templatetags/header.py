from django import template
from datetime import datetime, date

register = template.Library()

@register.inclusion_tag('layout/header.html', takes_context=True)
def show_header(context):
    """ Render header template with given parameters """
    request = context['request'];
    return {'user' : request.user};
