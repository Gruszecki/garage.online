from country_list import countries_for_language
import pycountry


def get_default_colors():
    primary_color = '#b5a578'
    text_color = '#ffffff'
    background_color = '#000000'
    background_medium_color = '#202020'
    background_light_color = '#505050'

    return [{
        'primary_color': primary_color,
        'text_color': text_color,
        'background_color': background_color,
        'background_medium_color': background_medium_color,
        'background_light_color': background_light_color
    }]

def get_filters():
    # Keys cannot have dashes (-) in names because later they will be split by dashes

    bands = {
        'active': 'aktywne',
        'not_active': 'nieaktywne',
        'with_songs': 'z utworami',
        'without_songs': 'bez utworów'
    }

    songs = {
        'with_lyrics': 'z tekstami',
        'without_lyrics': 'bez tekstów'
    }

    genres = get_genres()

    search_fields = {
        'name': 'nazwa',
        'desc': 'opis',
        'song': 'utwór',
        'tag': 'tag',
        'city': 'miejscowość',
    }

    sort_options = {
        'newest': 'od najnowszych',
        'oldest': 'od najstarszych',
        'a_z': 'a-z',
        'z_a': 'z-a'
    }

    return {
        'bands': bands,
        'songs': songs,
        'genres': genres,
        'search_fields': search_fields,
        'sort_options': sort_options
    }


def get_genres():
    genres = {
        (0, 'other'),
        (1, 'acoustic'),
        (2, 'alternative'),
        (3, 'ambient'),
        (4, 'blues'),
        (5, 'classical'),
        (6, 'country'),
        (7, 'devotional'),
        (8, 'electronic'),
        (9, 'experimental'),
        (10, 'folk'),
        (11, 'funk'),
        (12, 'jazz'),
        (13, 'latin'),
        (14, 'metal'),
        (15, 'pop'),
        (16, 'punk'),
        (17, 'R&B/soul'),
        (18, 'rap'),
        (19, 'rap - instrumental beat'),
        (20, 'reggae'),
        (21, 'rock'),
        (22, 'soundtrack'),
        (23, 'world')
    }

    genres_sorted = sorted(genres, key=lambda tup: tup[0])

    return genres_sorted


def get_socials():
    socials = {
        (0, 'Facebook'),
        (1, 'Bandcamp'),
        (2, 'Spotify'),
        (3, 'YouTube'),
        (4, 'SoundCloud'),
        (5, 'iTuens'),
        (6, 'Instagram'),
        (7, 'inne'),
    }

    return socials


def get_countries():
    countries = countries_for_language('pl')
    return countries


def get_languages():
    languages = [
        ('aa', 'Afar'),
        ('ab', 'Abkhazian'),
        ('af', 'Afrikaans'),
        ('ak', 'Akan'),
        ('sq', 'Albanian'),
        ('am', 'Amharic'),
        ('ar', 'Arabic'),
        ('an', 'Aragonese'),
        ('hy', 'Armenian'),
        ('as', 'Assamese'),
        ('av', 'Avaric'),
        ('ae', 'Avestan'),
        ('ay', 'Aymara'),
        ('az', 'Azerbaijani'),
        ('ba', 'Bashkir'),
        ('bm', 'Bambara'),
        ('eu', 'Basque'),
        ('be', 'Belarusian'),
        ('bn', 'Bengali'),
        ('bh', 'Bihari languages'),
        ('bi', 'Bislama'),
        ('bo', 'Tibetan'),
        ('bs', 'Bosnian'),
        ('br', 'Breton'),
        ('bg', 'Bulgarian'),
        ('my', 'Burmese'),
        ('ca', 'Catalan; Valencian'),
        ('cs', 'Czech'),
        ('ch', 'Chamorro'),
        ('ce', 'Chechen'),
        ('zh', 'Chinese'),
        ('cu', 'Church Slavic;'),
        ('cv', 'Chuvash'),
        ('kw', 'Cornish'),
        ('co', 'Corsican'),
        ('cr', 'Cree'),
        ('cy', 'Welsh'),
        ('cs', 'Czech'),
        ('da', 'Danish'),
        ('de', 'German'),
        ('dv', 'Divehi; Dhivehi; Maldivian'),
        ('nl', 'Dutch; Flemish'),
        ('dz', 'Dzongkha'),
        ('el', 'Greek'),
        ('en', 'English'),
        ('eo', 'Esperanto'),
        ('et', 'Estonian'),
        ('eu', 'Basque'),
        ('ee', 'Ewe'),
        ('fo', 'Faroese'),
        ('fa', 'Persian'),
        ('fj', 'Fijian'),
        ('fi', 'Finnish'),
        ('fr', 'French'),
        ('fy', 'Western Frisian'),
        ('ff', 'Fulah'),
        ('Ga', 'Georgian'),
        ('de', 'German'),
        ('gd', 'Gaelic; Scottish Gaelic'),
        ('ga', 'Irish'),
        ('gl', 'Galician'),
        ('gv', 'Manx'),
        ('el', 'Greek, Modern (1453-)'),
        ('gn', 'Guarani'),
        ('gu', 'Gujarati'),
        ('ht', 'Haitian; Haitian Creole'),
        ('ha', 'Hausa'),
        ('he', 'Hebrew'),
        ('hz', 'Herero'),
        ('hi', 'Hindi'),
        ('ho', 'Hiri Motu'),
        ('hr', 'Croatian'),
        ('hu', 'Hungarian'),
        ('hy', 'Armenian'),
        ('ig', 'Igbo'),
        ('is', 'Icelandic'),
        ('io', 'Ido'),
        ('ii', 'Sichuan Yi; Nuosu'),
        ('iu', 'Inuktitut'),
        ('ie', 'Interlingue; Occidental'),
        ('ia', 'Interlingua'),
        ('id', 'Indonesian'),
        ('ik', 'Inupiaq'),
        ('is', 'Icelandic'),
        ('it', 'Italian'),
        ('jv', 'Javanese'),
        ('ja', 'Japanese'),
        ('kl', 'Kalaallisut; Greenlandic'),
        ('kn', 'Kannada'),
        ('ks', 'Kashmiri'),
        ('ka', 'Georgian'),
        ('kr', 'Kanuri'),
        ('kk', 'Kazakh'),
        ('km', 'Central Khmer'),
        ('ki', 'Kikuyu; Gikuyu'),
        ('rw', 'Kinyarwanda'),
        ('ky', 'Kirghiz; Kyrgyz'),
        ('kv', 'Komi'),
        ('kg', 'Kongo'),
        ('ko', 'Korean'),
        ('kj', 'Kuanyama; Kwanyama'),
        ('ku', 'Kurdish'),
        ('lo', 'Lao'),
        ('la', 'Latin'),
        ('lv', 'Latvian'),
        ('li', 'Limburgan; Limburger; Limburgish'),
        ('ln', 'Lingala'),
        ('lt', 'Lithuanian'),
        ('lb', 'Luxembourgish; Letzeburgesch'),
        ('lu', 'Luba-Katanga'),
        ('lg', 'Ganda'),
        ('mk', 'Macedonian'),
        ('mh', 'Marshallese'),
        ('ml', 'Malayalam'),
        ('mi', 'Maori'),
        ('mr', 'Marathi'),
        ('ms', 'Malay'),
        ('Mi', 'Micmac'),
        ('mk', 'Macedonian'),
        ('mg', 'Malagasy'),
        ('mt', 'Maltese'),
        ('mn', 'Mongolian'),
        ('mi', 'Maori'),
        ('ms', 'Malay'),
        ('my', 'Burmese'),
        ('na', 'Nauru'),
        ('nv', 'Navajo; Navaho'),
        ('nr', 'Ndebele, South; South Ndebele'),
        ('nd', 'Ndebele, North; North Ndebele'),
        ('ng', 'Ndonga'),
        ('ne', 'Nepali'),
        ('nl', 'Dutch; Flemish'),
        ('nn', 'Norwegian, Nynorsk'),
        ('nb', 'Bokmål, Norwegian; Norwegian Bokmål'),
        ('no', 'Norwegian'),
        ('oc', 'Occitan (post 1500)'),
        ('oj', 'Ojibwa'),
        ('or', 'Oriya'),
        ('om', 'Oromo'),
        ('os', 'Ossetian; Ossetic'),
        ('pa', 'Panjabi; Punjabi'),
        ('fa', 'Persian'),
        ('pi', 'Pali'),
        ('pl', 'Polish'),
        ('pt', 'Portuguese'),
        ('ps', 'Pushto; Pashto'),
        ('qu', 'Quechua'),
        ('rm', 'Romansh'),
        ('ro', 'Romanian; Moldavian; Moldovan'),
        ('rn', 'Rundi'),
        ('ru', 'Russian'),
        ('sg', 'Sango'),
        ('sa', 'Sanskrit'),
        ('si', 'Sinhala; Sinhalese'),
        ('sk', 'Slovak'),
        ('sl', 'Slovenian'),
        ('se', 'Northern Sami'),
        ('sm', 'Samoan'),
        ('sn', 'Shona'),
        ('sd', 'Sindhi'),
        ('so', 'Somali'),
        ('st', 'Sotho, Southern'),
        ('es', 'Spanish; Castilian'),
        ('sq', 'Albanian'),
        ('sc', 'Sardinian'),
        ('sr', 'Serbian'),
        ('ss', 'Swati'),
        ('su', 'Sundanese'),
        ('sw', 'Swahili'),
        ('sv', 'Swedish'),
        ('ty', 'Tahitian'),
        ('ta', 'Tamil'),
        ('tt', 'Tatar'),
        ('te', 'Telugu'),
        ('tg', 'Tajik'),
        ('tl', 'Tagalog'),
        ('th', 'Thai'),
        ('bo', 'Tibetan'),
        ('ti', 'Tigrinya'),
        ('to', 'Tonga (Tonga Islands)'),
        ('tn', 'Tswana'),
        ('ts', 'Tsonga'),
        ('tk', 'Turkmen'),
        ('tr', 'Turkish'),
        ('tw', 'Twi'),
        ('ug', 'Uighur; Uyghur'),
        ('uk', 'Ukrainian'),
        ('ur', 'Urdu'),
        ('uz', 'Uzbek'),
        ('ve', 'Venda'),
        ('vi', 'Vietnamese'),
        ('vo', 'Volapük'),
        ('cy', 'Welsh'),
        ('wa', 'Walloon'),
        ('wo', 'Wolof'),
        ('wy', 'Wymysorys'),
        ('xh', 'Xhosa'),
        ('yi', 'Yiddish'),
        ('yo', 'Yoruba'),
        ('za', 'Zhuang; Chuang'),
        ('zh', 'Chinese'),
        ('zu', 'Zulu')
    ]
    return languages
