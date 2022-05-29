from country_list import countries_for_language


def get_genres():
    genres = {
        (0, 'inne'),
        (1, 'rock'),
        (2, 'metal'),
        (3, 'pop'),
        (4, 'reggae'),
        (5, 'muzyka akustyczna'),
        (6, 'muzyka elektroniczna'),
        (7, 'rap'),
        (8, 'jazz')
    }

    return genres


def get_countries():
    countries = dict(countries_for_language('pl'))
    return countries
