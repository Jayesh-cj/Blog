# from django import template
# from django.utils.html import format_html

# register = template.Library()

# @register.filter
# def truncate_html(value, length=100):
#     if len(value) > length:
#         return format_html('{}...', value[:length])
#     return value

from django import template
from django.utils.html import format_html, escape
from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def truncate_html(value, length=100):
    soup = BeautifulSoup(value, 'html.parser')
    text = soup.get_text()
    if len(text) > length:
        truncated_text = text[:length] + '...'
        truncated_html = BeautifulSoup(truncated_text, 'html.parser').prettify()
        return format_html(truncated_html)
    return value
