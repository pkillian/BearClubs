from django import template
from datetime import datetime, date

register = template.Library()

@register.inclusion_tag('footer.html')
def show_footer():
    """ Render footer template with given parameters """
    return {};
