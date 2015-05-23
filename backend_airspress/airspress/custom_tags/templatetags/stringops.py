from django import template
from django.template.defaultfilters import stringfilter 
 
register = template.Library()
 
# truncate chars but no adding '...' 
@register.filter(name='nodottruncatechars')
@stringfilter
def no_dot_truncate_chars(value, max_length):
 
    if len(value) > max_length:
        # limits the number of characters in value to max_length (blunt cut)
        truncd_val = value[:max_length]
 
        return truncd_val
 
    return value