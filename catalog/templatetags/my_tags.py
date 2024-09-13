from django import template

register = template.Library()

@register.filter()
def media_filter(path):
    if path:
        return f'/media/{path}'
    return '#'


@register.filter()
def truncate_chars(text):
    if len(text) > 100:
        return text[:100]
    return text