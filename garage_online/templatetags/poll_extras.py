from garage_online.choices import get_genres
from django import template

register = template.Library()


@register.inclusion_tag('results.html')
def genres():
    gens = get_genres()
    genres_sorted = sorted(gens, key=lambda tup: tup[0])

    return {'genres': genres_sorted}
