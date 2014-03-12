import logging
from django.template import Library
from datetime import datetime, date
import calendar

logger = logging.getLogger(__name__)
register = Library()

@register.inclusion_tag('header.html')
def show_header():
    """ Render header template with given parameters """
    return {};
