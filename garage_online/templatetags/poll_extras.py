from garage_online.choices import get_genres
from django import template

register = template.Library()


@register.inclusion_tag('results.html')
def genres():
    gens = get_genres()
    return {'genres': gens}
