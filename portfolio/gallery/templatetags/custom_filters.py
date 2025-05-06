from django import template

register = template.Library()

@register.filter
def field_max_words(value, arg):

    try:
        n = int(arg)
    except ValueError:
        return value
    
    words = value.split()
    lines = [' '.join(words[i:i+n]) for i in range(0, len(words), n)]
    return '<br>'.join(lines)