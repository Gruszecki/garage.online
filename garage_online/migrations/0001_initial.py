# Generated by Django 4.0.4 on 2022-05-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_desc', models.TextField(max_length=150)),
                ('long_desc', models.TextField()),
                ('genre', models.CharField(choices=[(3, 'pop'), (5, 'muzyka akustyczna'), (4, 'reggae'), (7, 'rap'), (8, 'jazz'), (1, 'rock'), (6, 'muzyka elektroniczna'), (0, 'inne'), (2, 'metal')], default=0, max_length=2)),
                ('image', models.ImageField(upload_to='bands_photos')),
                ('country', models.PositiveSmallIntegerField(choices=[('AF', 'Afganistan'), ('AL', 'Albania'), ('DZ', 'Algieria'), ('AD', 'Andora'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarktyda'), ('AG', 'Antigua i Barbuda'), ('SA', 'Arabia Saudyjska'), ('AR', 'Argentyna'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbejdżan'), ('BS', 'Bahamy'), ('BH', 'Bahrajn'), ('BD', 'Bangladesz'), ('BB', 'Barbados'), ('BE', 'Belgia'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermudy'), ('BT', 'Bhutan'), ('BY', 'Białoruś'), ('BO', 'Boliwia'), ('BA', 'Bośnia i Hercegowina'), ('BW', 'Botswana'), ('BR', 'Brazylia'), ('BN', 'Brunei'), ('IO', 'Brytyjskie Terytorium Oceanu Indyjskiego'), ('VG', 'Brytyjskie Wyspy Dziewicze'), ('BG', 'Bułgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('CL', 'Chile'), ('CN', 'Chiny'), ('HR', 'Chorwacja'), ('CI', 'Côte d’Ivoire'), ('CW', 'Curaçao'), ('CY', 'Cypr'), ('TD', 'Czad'), ('ME', 'Czarnogóra'), ('CZ', 'Czechy'), ('UM', 'Dalekie Wyspy Mniejsze Stanów Zjednoczonych'), ('DK', 'Dania'), ('CD', 'Demokratyczna Republika Konga'), ('DM', 'Dominika'), ('DO', 'Dominikana'), ('DJ', 'Dżibuti'), ('EG', 'Egipt'), ('EC', 'Ekwador'), ('ER', 'Erytrea'), ('EE', 'Estonia'), ('SZ', 'Eswatini'), ('ET', 'Etiopia'), ('FK', 'Falklandy'), ('FJ', 'Fidżi'), ('PH', 'Filipiny'), ('FI', 'Finlandia'), ('FR', 'Francja'), ('TF', 'Francuskie Terytoria Południowe i Antarktyczne'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GS', 'Georgia Południowa i Sandwich Południowy'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Grecja'), ('GD', 'Grenada'), ('GL', 'Grenlandia'), ('GE', 'Gruzja'), ('GU', 'Guam'), ('GG', 'Guernsey'), ('GY', 'Gujana'), ('GF', 'Gujana Francuska'), ('GP', 'Gwadelupa'), ('GT', 'Gwatemala'), ('GN', 'Gwinea'), ('GW', 'Gwinea Bissau'), ('GQ', 'Gwinea Równikowa'), ('HT', 'Haiti'), ('ES', 'Hiszpania'), ('NL', 'Holandia'), ('HN', 'Honduras'), ('IN', 'Indie'), ('ID', 'Indonezja'), ('IQ', 'Irak'), ('IR', 'Iran'), ('IE', 'Irlandia'), ('IS', 'Islandia'), ('IL', 'Izrael'), ('JM', 'Jamajka'), ('JP', 'Japonia'), ('YE', 'Jemen'), ('JE', 'Jersey'), ('JO', 'Jordania'), ('KY', 'Kajmany'), ('KH', 'Kambodża'), ('CM', 'Kamerun'), ('CA', 'Kanada'), ('QA', 'Katar'), ('KZ', 'Kazachstan'), ('KE', 'Kenia'), ('KG', 'Kirgistan'), ('KI', 'Kiribati'), ('CO', 'Kolumbia'), ('KM', 'Komory'), ('CG', 'Kongo'), ('KR', 'Korea Południowa'), ('KP', 'Korea Północna'), ('CR', 'Kostaryka'), ('CU', 'Kuba'), ('KW', 'Kuwejt'), ('LA', 'Laos'), ('LS', 'Lesotho'), ('LB', 'Liban'), ('LR', 'Liberia'), ('LY', 'Libia'), ('LI', 'Liechtenstein'), ('LT', 'Litwa'), ('LU', 'Luksemburg'), ('LV', 'Łotwa'), ('MK', 'Macedonia Północna'), ('MG', 'Madagaskar'), ('YT', 'Majotta'), ('MW', 'Malawi'), ('MV', 'Malediwy'), ('MY', 'Malezja'), ('ML', 'Mali'), ('MT', 'Malta'), ('MP', 'Mariany Północne'), ('MA', 'Maroko'), ('MQ', 'Martynika'), ('MR', 'Mauretania'), ('MU', 'Mauritius'), ('MX', 'Meksyk'), ('FM', 'Mikronezja'), ('MM', 'Mjanma (Birma)'), ('MD', 'Mołdawia'), ('MC', 'Monako'), ('MN', 'Mongolia'), ('MS', 'Montserrat'), ('MZ', 'Mozambik'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('BQ', 'Niderlandy Karaibskie'), ('DE', 'Niemcy'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NI', 'Nikaragua'), ('NU', 'Niue'), ('NF', 'Norfolk'), ('NO', 'Norwegia'), ('NC', 'Nowa Kaledonia'), ('NZ', 'Nowa Zelandia'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PA', 'Panama'), ('PG', 'Papua-Nowa Gwinea'), ('PY', 'Paragwaj'), ('PE', 'Peru'), ('PN', 'Pitcairn'), ('PF', 'Polinezja Francuska'), ('PL', 'Polska'), ('PR', 'Portoryko'), ('PT', 'Portugalia'), ('ZA', 'Republika Południowej Afryki'), ('CF', 'Republika Środkowoafrykańska'), ('CV', 'Republika Zielonego Przylądka'), ('RE', 'Reunion'), ('RU', 'Rosja'), ('RO', 'Rumunia'), ('RW', 'Rwanda'), ('EH', 'Sahara Zachodnia'), ('KN', 'Saint Kitts i Nevis'), ('LC', 'Saint Lucia'), ('VC', 'Saint Vincent i Grenadyny'), ('BL', 'Saint-Barthélemy'), ('MF', 'Saint-Martin'), ('PM', 'Saint-Pierre i Miquelon'), ('SV', 'Salwador'), ('WS', 'Samoa'), ('AS', 'Samoa Amerykańskie'), ('SM', 'San Marino'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seszele'), ('SL', 'Sierra Leone'), ('SG', 'Singapur'), ('SX', 'Sint Maarten'), ('SK', 'Słowacja'), ('SI', 'Słowenia'), ('SO', 'Somalia'), ('HK', 'SRA Hongkong (Chiny)'), ('MO', 'SRA Makau (Chiny)'), ('LK', 'Sri Lanka'), ('US', 'Stany Zjednoczone'), ('SD', 'Sudan'), ('SS', 'Sudan Południowy'), ('SR', 'Surinam'), ('SJ', 'Svalbard i Jan Mayen'), ('SY', 'Syria'), ('CH', 'Szwajcaria'), ('SE', 'Szwecja'), ('TJ', 'Tadżykistan'), ('TH', 'Tajlandia'), ('TW', 'Tajwan'), ('TZ', 'Tanzania'), ('PS', 'Terytoria Palestyńskie'), ('TL', 'Timor Wschodni'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trynidad i Tobago'), ('TN', 'Tunezja'), ('TR', 'Turcja'), ('TM', 'Turkmenistan'), ('TC', 'Turks i Caicos'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraina'), ('UY', 'Urugwaj'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('WF', 'Wallis i Futuna'), ('VA', 'Watykan'), ('VE', 'Wenezuela'), ('HU', 'Węgry'), ('GB', 'Wielka Brytania'), ('VN', 'Wietnam'), ('IT', 'Włochy'), ('BV', 'Wyspa Bouveta'), ('CX', 'Wyspa Bożego Narodzenia'), ('IM', 'Wyspa Man'), ('SH', 'Wyspa Świętej Heleny'), ('AX', 'Wyspy Alandzkie'), ('CK', 'Wyspy Cooka'), ('VI', 'Wyspy Dziewicze Stanów Zjednoczonych'), ('HM', 'Wyspy Heard i McDonalda'), ('CC', 'Wyspy Kokosowe'), ('MH', 'Wyspy Marshalla'), ('FO', 'Wyspy Owcze'), ('SB', 'Wyspy Salomona'), ('ST', 'Wyspy Świętego Tomasza i Książęca'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe'), ('AE', 'Zjednoczone Emiraty Arabskie')], default='PL')),
                ('city', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('tags', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
