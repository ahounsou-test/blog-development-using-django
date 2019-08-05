from django.db import models

# ISO 3166-1 country names and codes adapted from http://opencountrycodes.appspot.com/python/
COUNTRIES = {
    'AF': 'Afghanistan',
    'AX': 'Aland Islands',
    'AL': 'Albania',
    'DZ': 'Algeria',
    'AS': 'American Samoa',
    'AD': 'Andorra',
    'AO': 'Angola',
    'AI': 'Anguilla',
    # 'AQ': 'Antarctica',
    'AG': 'Antigua and Barbuda',
    'AR': 'Argentina',
    'AM': 'Armenia',
    'AW': 'Aruba',
    'AU': 'Australia',
    'AT': 'Austria',
    'AZ': 'Azerbaijan',
    'BS': 'Bahamas',
    'BH': 'Bahrain',
    'BD': 'Bangladesh',
    'BB': 'Barbados',
    'BY': 'Belarus',
    'BE': 'Belgium',
    'BZ': 'Belize',
    'BJ': 'Benin',
    'BM': 'Bermuda',
    'BT': 'Bhutan',
    'BO': 'Bolivia',
    'BA': 'Bosnia and Herzegovina',
    'BW': 'Botswana',
    # 'BV': 'Bouvet Island',
    'BR': 'Brazil',
    'IO': 'British Indian Ocean Territory',
    'BN': 'Brunei Darussalam',
    'BG': 'Bulgaria',
    'BF': 'Burkina Faso',
    'BI': 'Burundi',
    'KH': 'Cambodia',
    'CM': 'Cameroon',
    'CA': 'Canada',
    'CV': 'Cape Verde',
    'KY': 'Cayman Islands',
    'CF': 'Central African Republic',
    'TD': 'Chad',
    'CL': 'Chile',
    'CN': 'China',
    'CX': 'Christmas Island',
    'CC': 'Cocos (Keeling) Islands',
    'CO': 'Colombia',
    'KM': 'Comoros',
    'CG': 'Congo',
    'CD': 'Congo, The Democratic Republic of the',
    'CK': 'Cook Islands',
    'CR': 'Costa Rica',
    'CI': 'Cote d\'Ivoire',
    'HR': 'Croatia',
    'CU': 'Cuba',
    'CY': 'Cyprus',
    'CZ': 'Czech Republic',
    'DK': 'Denmark',
    'DJ': 'Djibouti',
    'DM': 'Dominica',
    'DO': 'Dominican Republic',
    'EC': 'Ecuador',
    'EG': 'Egypt',
    'SV': 'El Salvador',
    'GQ': 'Equatorial Guinea',
    'ER': 'Eritrea',
    'EE': 'Estonia',
    'ET': 'Ethiopia',
    'FK': 'Falkland Islands (Malvinas)',
    'FO': 'Faroe Islands',
    'FJ': 'Fiji',
    'FI': 'Finland',
    'FR': 'France',
    'GF': 'French Guiana',
    'PF': 'French Polynesia',
    'TF': 'French Southern Territories',
    'GA': 'Gabon',
    'GM': 'Gambia',
    'GE': 'Georgia',
    'DE': 'Germany',
    'GH': 'Ghana',
    'GI': 'Gibraltar',
    'GR': 'Greece',
    'GL': 'Greenland',
    'GD': 'Grenada',
    'GP': 'Guadeloupe',
    'GU': 'Guam',
    'GT': 'Guatemala',
    'GG': 'Guernsey',
    'GN': 'Guinea',
    'GW': 'Guinea-Bissau',
    'GY': 'Guyana',
    'HT': 'Haiti',
    # 'HM': 'Heard Island and McDonald Islands',
    'VA': 'Holy See (Vatican City State)',
    'HN': 'Honduras',
    'HK': 'Hong Kong',
    'HU': 'Hungary',
    'IS': 'Iceland',
    'IN': 'India',
    'ID': 'Indonesia',
    'IR': 'Iran, Islamic Republic of',
    'IQ': 'Iraq',
    'IE': 'Ireland',
    'IM': 'Isle of Man',
    'IL': 'Israel',
    'IT': 'Italy',
    'JM': 'Jamaica',
    'JP': 'Japan',
    'JE': 'Jersey',
    'JO': 'Jordan',
    'KZ': 'Kazakhstan',
    'KE': 'Kenya',
    'KI': 'Kiribati',
    'KP': 'Korea, Democratic People\'s Republic of',
    'KR': 'Korea, Republic of',
    'KW': 'Kuwait',
    'KG': 'Kyrgyzstan',
    'LA': 'Lao People\'s Democratic Republic',
    'LV': 'Latvia',
    'LB': 'Lebanon',
    'LS': 'Lesotho',
    'LR': 'Liberia',
    'LY': 'Libyan Arab Jamahiriya',
    'LI': 'Liechtenstein',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'MO': 'Macao',
    'MK': 'Macedonia, The Former Yugoslav Republic of',
    'MG': 'Madagascar',
    'MW': 'Malawi',
    'MY': 'Malaysia',
    'MV': 'Maldives',
    'ML': 'Mali',
    'MT': 'Malta',
    'MH': 'Marshall Islands',
    'MQ': 'Martinique',
    'MR': 'Mauritania',
    'MU': 'Mauritius',
    'YT': 'Mayotte',
    'MX': 'Mexico',
    'FM': 'Micronesia, Federated States of',
    'MD': 'Moldova',
    'MC': 'Monaco',
    'MN': 'Mongolia',
    'ME': 'Montenegro',
    'MS': 'Montserrat',
    'MA': 'Morocco',
    'MZ': 'Mozambique',
    'MM': 'Myanmar',
    'NA': 'Namibia',
    'NR': 'Nauru',
    'NP': 'Nepal',
    'NL': 'Netherlands',
    'AN': 'Netherlands Antilles',
    'NC': 'New Caledonia',
    'NZ': 'New Zealand',
    'NI': 'Nicaragua',
    'NE': 'Niger',
    'NG': 'Nigeria',
    'NU': 'Niue',
    'NF': 'Norfolk Island',
    'MP': 'Northern Mariana Islands',
    'NO': 'Norway',
    'OM': 'Oman',
    'PK': 'Pakistan',
    'PW': 'Palau',
    'PS': 'Palestinian Territory, Occupied',
    'PA': 'Panama',
    'PG': 'Papua New Guinea',
    'PY': 'Paraguay',
    'PE': 'Peru',
    'PH': 'Philippines',
    'PN': 'Pitcairn',
    'PL': 'Poland',
    'PT': 'Portugal',
    'PR': 'Puerto Rico',
    'QA': 'Qatar',
    'RE': 'Reunion',
    'RO': 'Romania',
    'RU': 'Russian Federation',
    'RW': 'Rwanda',
    'BL': 'Saint Barthelemy',
    'SH': 'Saint Helena',
    'KN': 'Saint Kitts and Nevis',
    'LC': 'Saint Lucia',
    'MF': 'Saint Martin',
    'PM': 'Saint Pierre and Miquelon',
    'VC': 'Saint Vincent and the Grenadines',
    'WS': 'Samoa',
    'SM': 'San Marino',
    'ST': 'Sao Tome and Principe',
    'SA': 'Saudi Arabia',
    'SN': 'Senegal',
    'RS': 'Serbia',
    'SC': 'Seychelles',
    'SL': 'Sierra Leone',
    'SG': 'Singapore',
    'SK': 'Slovakia',
    'SI': 'Slovenia',
    'SB': 'Solomon Islands',
    'SO': 'Somalia',
    'ZA': 'South Africa',
    'GS': 'South Georgia and the South Sandwich Islands',
    'ES': 'Spain',
    'LK': 'Sri Lanka',
    'SD': 'Sudan',
    'SR': 'Suriname',
    # 'SJ': 'Svalbard and Jan Mayen',
    'SZ': 'Swaziland',
    'SE': 'Sweden',
    'CH': 'Switzerland',
    'SY': 'Syrian Arab Republic',
    'TW': 'Taiwan, Province of China',
    'TJ': 'Tajikistan',
    'TZ': 'Tanzania, United Republic of',
    'TH': 'Thailand',
    'TL': 'Timor-Leste',
    'TG': 'Togo',
    'TK': 'Tokelau',
    'TO': 'Tonga',
    'TT': 'Trinidad and Tobago',
    'TN': 'Tunisia',
    'TR': 'Turkey',
    'TM': 'Turkmenistan',
    'TC': 'Turks and Caicos Islands',
    'TV': 'Tuvalu',
    'UG': 'Uganda',
    'UA': 'Ukraine',
    'AE': 'United Arab Emirates',
    'GB': 'United Kingdom',
    'US': 'United States',
    # 'UM': 'United States Minor Outlying Islands',
    'UY': 'Uruguay',
    'UZ': 'Uzbekistan',
    'VU': 'Vanuatu',
    'VE': 'Venezuela',
    'VN': 'Viet Nam',
    'VG': 'Virgin Islands, British',
    'VI': 'Virgin Islands, U.S.',
    'WF': 'Wallis and Futuna',
    'EH': 'Western Sahara',
    'YE': 'Yemen',
    'ZM': 'Zambia',
    'ZW': 'Zimbabwe',
}

COUNTRIES_TUPLES = [
    ('AF', 'Afghanistan'),
    ('AX', 'Aland Islands'),
    ('AL', 'Albania'),
    ('DZ', 'Algeria'),
    ('AS', 'American Samoa'),
    ('AD', 'Andorra'),
    ('AO', 'Angola'),
    ('AI', 'Anguilla'),
    # ('AQ', 'Antarctica'),
    ('AG', 'Antigua and Barbuda'),
    ('AR', 'Argentina'),
    ('AM', 'Armenia'),
    ('AW', 'Aruba'),
    ('AU', 'Australia'),
    ('AT', 'Austria'),
    ('AZ', 'Azerbaijan'),
    ('BS', 'Bahamas'),
    ('BH', 'Bahrain'),
    ('BD', 'Bangladesh'),
    ('BB', 'Barbados'),
    ('BY', 'Belarus'),
    ('BE', 'Belgium'),
    ('BZ', 'Belize'),
    ('BJ', 'Benin'),
    ('BM', 'Bermuda'),
    ('BT', 'Bhutan'),
    ('BO', 'Bolivia'),
    ('BA', 'Bosnia and Herzegovina'),
    ('BW', 'Botswana'),
    # ('BV', 'Bouvet Island'),
    ('BR', 'Brazil'),
    ('IO', 'British Indian Ocean Territory'),
    ('BN', 'Brunei Darussalam'),
    ('BG', 'Bulgaria'),
    ('BF', 'Burkina Faso'),
    ('BI', 'Burundi'),
    ('KH', 'Cambodia'),
    ('CM', 'Cameroon'),
    ('CA', 'Canada'),
    ('CV', 'Cape Verde'),
    ('KY', 'Cayman Islands'),
    ('CF', 'Central African Republic'),
    ('TD', 'Chad'),
    ('CL', 'Chile'),
    ('CN', 'China'),
    ('CX', 'Christmas Island'),
    ('CC', 'Cocos (Keeling) Islands'),
    ('CO', 'Colombia'),
    ('KM', 'Comoros'),
    ('CG', 'Congo'),
    ('CD', 'Congo, The Democratic Republic of the'),
    ('CK', 'Cook Islands'),
    ('CR', 'Costa Rica'),
    ('CI', 'Cote d\'Ivoire'),
    ('HR', 'Croatia'),
    ('CU', 'Cuba'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DK', 'Denmark'),
    ('DJ', 'Djibouti'),
    ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),
    ('EC', 'Ecuador'),
    ('EG', 'Egypt'),
    ('SV', 'El Salvador'),
    ('GQ', 'Equatorial Guinea'),
    ('ER', 'Eritrea'),
    ('EE', 'Estonia'),
    ('ET', 'Ethiopia'),
    ('FK', 'Falkland Islands (Malvinas)'),
    ('FO', 'Faroe Islands'),
    ('FJ', 'Fiji'),
    ('FI', 'Finland'),
    ('FR', 'France'),
    ('GF', 'French Guiana'),
    ('PF', 'French Polynesia'),
    ('TF', 'French Southern Territories'),
    ('GA', 'Gabon'),
    ('GM', 'Gambia'),
    ('GE', 'Georgia'),
    ('DE', 'Germany'),
    ('GH', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GR', 'Greece'),
    ('GL', 'Greenland'),
    ('GD', 'Grenada'),
    ('GP', 'Guadeloupe'),
    ('GU', 'Guam'),
    ('GT', 'Guatemala'),
    ('GG', 'Guernsey'),
    ('GN', 'Guinea'),
    ('GW', 'Guinea-Bissau'),
    ('GY', 'Guyana'),
    ('HT', 'Haiti'),
    # ('HM', 'Heard Island and McDonald Islands'),
    ('VA', 'Holy See (Vatican City State)'),
    ('HN', 'Honduras'),
    ('HK', 'Hong Kong'),
    ('HU', 'Hungary'),
    ('IS', 'Iceland'),
    ('IN', 'India'),
    ('ID', 'Indonesia'),
    ('IR', 'Iran, Islamic Republic of'),
    ('IQ', 'Iraq'),
    ('IE', 'Ireland'),
    ('IM', 'Isle of Man'),
    ('IL', 'Israel'),
    ('IT', 'Italy'),
    ('JM', 'Jamaica'),
    ('JP', 'Japan'),
    ('JE', 'Jersey'),
    ('JO', 'Jordan'),
    ('KZ', 'Kazakhstan'),
    ('KE', 'Kenya'),
    ('KI', 'Kiribati'),
    ('KP', 'Korea, Democratic People\'s Republic of'),
    ('KR', 'Korea, Republic of'),
    ('KW', 'Kuwait'),
    ('KG', 'Kyrgyzstan'),
    ('LA', 'Lao People\'s Democratic Republic'),
    ('LV', 'Latvia'),
    ('LB', 'Lebanon'),
    ('LS', 'Lesotho'),
    ('LR', 'Liberia'),
    ('LY', 'Libyan Arab Jamahiriya'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
    ('MO', 'Macao'),
    ('MK', 'Macedonia, The Former Yugoslav Republic of'),
    ('MG', 'Madagascar'),
    ('MW', 'Malawi'),
    ('MY', 'Malaysia'),
    ('MV', 'Maldives'),
    ('ML', 'Mali'),
    ('MT', 'Malta'),
    ('MH', 'Marshall Islands'),
    ('MQ', 'Martinique'),
    ('MR', 'Mauritania'),
    ('MU', 'Mauritius'),
    ('YT', 'Mayotte'),
    ('MX', 'Mexico'),
    ('FM', 'Micronesia, Federated States of'),
    ('MD', 'Moldova'),
    ('MC', 'Monaco'),
    ('MN', 'Mongolia'),
    ('ME', 'Montenegro'),
    ('MS', 'Montserrat'),
    ('MA', 'Morocco'),
    ('MZ', 'Mozambique'),
    ('MM', 'Myanmar'),
    ('NA', 'Namibia'),
    ('NR', 'Nauru'),
    ('NP', 'Nepal'),
    ('NL', 'Netherlands'),
    ('AN', 'Netherlands Antilles'),
    ('NC', 'New Caledonia'),
    ('NZ', 'New Zealand'),
    ('NI', 'Nicaragua'),
    ('NE', 'Niger'),
    ('NG', 'Nigeria'),
    ('NU', 'Niue'),
    ('NF', 'Norfolk Island'),
    ('MP', 'Northern Mariana Islands'),
    ('NO', 'Norway'),
    ('OM', 'Oman'),
    ('PK', 'Pakistan'),
    ('PW', 'Palau'),
    ('PS', 'Palestinian Territory, Occupied'),
    ('PA', 'Panama'),
    ('PG', 'Papua New Guinea'),
    ('PY', 'Paraguay'),
    ('PE', 'Peru'),
    ('PH', 'Philippines'),
    ('PN', 'Pitcairn'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('PR', 'Puerto Rico'),
    ('QA', 'Qatar'),
    ('RE', 'Reunion'),
    ('RO', 'Romania'),
    ('RU', 'Russian Federation'),
    ('RW', 'Rwanda'),
    ('BL', 'Saint Barthelemy'),
    ('SH', 'Saint Helena'),
    ('KN', 'Saint Kitts and Nevis'),
    ('LC', 'Saint Lucia'),
    ('MF', 'Saint Martin'),
    ('PM', 'Saint Pierre and Miquelon'),
    ('VC', 'Saint Vincent and the Grenadines'),
    ('WS', 'Samoa'),
    ('SM', 'San Marino'),
    ('ST', 'Sao Tome and Principe'),
    ('SA', 'Saudi Arabia'),
    ('SN', 'Senegal'),
    ('RS', 'Serbia'),
    ('SC', 'Seychelles'),
    ('SL', 'Sierra Leone'),
    ('SG', 'Singapore'),
    ('SK', 'Slovakia'),
    ('SI', 'Slovenia'),
    ('SB', 'Solomon Islands'),
    ('SO', 'Somalia'),
    ('ZA', 'South Africa'),
    ('GS', 'South Georgia and the South Sandwich Islands'),
    ('ES', 'Spain'),
    ('LK', 'Sri Lanka'),
    ('SD', 'Sudan'),
    ('SR', 'Suriname'),
    # ('SJ', 'Svalbard and Jan Mayen'),
    ('SZ', 'Swaziland'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('SY', 'Syrian Arab Republic'),
    ('TW', 'Taiwan, Province of China'),
    ('TJ', 'Tajikistan'),
    ('TZ', 'Tanzania, United Republic of'),
    ('TH', 'Thailand'),
    ('TL', 'Timor-Leste'),
    ('TG', 'Togo'),
    ('TK', 'Tokelau'),
    ('TO', 'Tonga'),
    ('TT', 'Trinidad and Tobago'),
    ('TN', 'Tunisia'),
    ('TR', 'Turkey'),
    ('TM', 'Turkmenistan'),
    ('TC', 'Turks and Caicos Islands'),
    ('TV', 'Tuvalu'),
    ('UG', 'Uganda'),
    ('UA', 'Ukraine'),
    ('AE', 'United Arab Emirates'),
    ('GB', 'United Kingdom'),
    ('US', 'United States'),
    # ('UM', 'United States Minor Outlying Islands'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistan'),
    ('VU', 'Vanuatu'),
    ('VE', 'Venezuela'),
    ('VN', 'Viet Nam'),
    ('VG', 'Virgin Islands, British'),
    ('VI', 'Virgin Islands, U.S.'),
    ('WF', 'Wallis and Futuna'),
    ('EH', 'Western Sahara'),
    ('YE', 'Yemen'),
    ('ZM', 'Zambia'),
    ('ZW', 'Zimbabwe'),
]


class CountryField(models.CharField):
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 2)
        kwargs.setdefault('choices', COUNTRIES_TUPLES)

        super(CountryField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"


COUNTRIES_3_TO_2 = {
    'AFG': 'AF',
    'ALA': 'AX',
    'ALB': 'AL',
    'DZA': 'DZ',
    'ASM': 'AS',
    'AND': 'AD',
    'AGO': 'AO',
    'AIA': 'AI',
    'ATG': 'AG',
    'ARG': 'AR',
    'ARM': 'AM',
    'ABW': 'AW',
    'AUS': 'AU',
    'AUT': 'AT',
    'AZE': 'AZ',
    'BHS': 'BS',
    'BHR': 'BH',
    'BGD': 'BD',
    'BRB': 'BB',
    'BLR': 'BY',
    'BEL': 'BE',
    'BLZ': 'BZ',
    'BEN': 'BJ',
    'BMU': 'BM',
    'BTN': 'BT',
    'BOL': 'BO',
    'BES': 'BQ',
    'BIH': 'BA',
    'BWA': 'BW',
    'BRA': 'BR',
    'IOT': 'IO',
    'VGB': 'VG',
    'BRN': 'BN',
    'BGR': 'BG',
    'BFA': 'BF',
    'BDI': 'BI',
    'KHM': 'KH',
    'CMR': 'CM',
    'CAN': 'CA',
    'CPV': 'CV',
    'CYM': 'KY',
    'CAF': 'CF',
    'TCD': 'TD',
    'CHL': 'CL',
    'CHN': 'CN',
    'CXR': 'CX',
    'CCK': 'CC',
    'COL': 'CO',
    'COM': 'KM',
    'COG': 'CG',
    'ZAR': 'CD',
    'COK': 'CK',
    'CRI': 'CR',
    'HRV': 'HR',
    'CUB': 'CU',
    'CUW': 'CW',
    'CYP': 'CY',
    'CZE': 'CZ',
    'DNK': 'DK',
    'DJI': 'DJ',
    'DMA': 'DM',
    'DOM': 'DO',
    'TLS': 'TL',
    'ECU': 'EC',
    'EGY': 'EG',
    'SLV': 'SV',
    'GNQ': 'GQ',
    'ERI': 'ER',
    'EST': 'EE',
    'ETH': 'ET',
    'FRO': 'FO',
    'FLK': 'FK',
    'FJI': 'FJ',
    'FIN': 'FI',
    'FRA': 'FR',
    'GUF': 'GF',
    'PYF': 'PF',
    'ATF': 'TF',
    'GAB': 'GA',
    'GMB': 'GM',
    'GEO': 'GE',
    'DEU': 'DE',
    'GHA': 'GH',
    'GIB': 'GI',
    'GRC': 'GR',
    'GRL': 'GL',
    'GRD': 'GD',
    'GLP': 'GP',
    'GUM': 'GU',
    'GTM': 'GT',
    'GGY': 'GG',
    'GIN': 'GN',
    'GNB': 'GW',
    'GUY': 'GY',
    'HTI': 'HT',
    'VAT': 'VA',
    'HND': 'HN',
    'HKG': 'HK',
    'HUN': 'HU',
    'ISL': 'IS',
    'IND': 'IN',
    'IDN': 'ID',
    'IRN': 'IR',
    'IRQ': 'IQ',
    'IRL': 'IE',
    'IMN': 'IM',
    'ISR': 'IL',
    'ITA': 'IT',
    'CIV': 'CI',
    'JAM': 'JM',
    'JPN': 'JP',
    'JEY': 'JE',
    'JOR': 'JO',
    'KAZ': 'KZ',
    'KEN': 'KE',
    'KIR': 'KI',
    'KWT': 'KW',
    'KGZ': 'KG',
    'LAO': 'LA',
    'LVA': 'LV',
    'LBN': 'LB',
    'LSO': 'LS',
    'LBR': 'LR',
    'LBY': 'LY',
    'LIE': 'LI',
    'LTU': 'LT',
    'LUX': 'LU',
    'MAC': 'MO',
    'MKD': 'MK',
    'MDG': 'MG',
    'MWI': 'MW',
    'MYS': 'MY',
    'MDV': 'MV',
    'MLI': 'ML',
    'MLT': 'MT',
    'MHL': 'MH',
    'MTQ': 'MQ',
    'MRT': 'MR',
    'MUS': 'MU',
    'MYT': 'YT',
    'MEX': 'MX',
    'FSM': 'FM',
    'MDA': 'MD',
    'MCO': 'MC',
    'MNG': 'MN',
    'MNE': 'ME',
    'MSR': 'MS',
    'MAR': 'MA',
    'MOZ': 'MZ',
    'MMR': 'MM',
    'NAM': 'NA',
    'NRU': 'NR',
    'NPL': 'NP',
    'ANT': 'AN',
    'NLD': 'NL',
    'NCL': 'NC',
    'NZL': 'NZ',
    'NIC': 'NI',
    'NER': 'NE',
    'NGA': 'NG',
    'NIU': 'NU',
    'NFK': 'NF',
    'PRK': 'KP',
    'MNP': 'MP',
    'NOR': 'NO',
    'OMN': 'OM',
    'PAK': 'PK',
    'PLW': 'PW',
    'PSE': 'PS',
    'PAN': 'PA',
    'PNG': 'PG',
    'PRY': 'PY',
    'PER': 'PE',
    'PHL': 'PH',
    'PCN': 'PN',
    'POL': 'PL',
    'PRT': 'PT',
    'PRI': 'PR',
    'QAT': 'QA',
    'ROU': 'RO',
    'RUS': 'RU',
    'RWA': 'RW',
    'REU': 'RE',
    'BLM': 'BL',
    'KNA': 'KN',
    'SHN': 'SH',
    'LCA': 'LC',
    'MAF': 'MF',
    'SPM': 'PM',
    'VCT': 'VC',
    'WSM': 'WS',
    'SMR': 'SM',
    'STP': 'ST',
    'SAU': 'SA',
    'SEN': 'SN',
    'SRB': 'RS',
    'SYC': 'SC',
    'SLE': 'SL',
    'SGP': 'SG',
    'SXM': 'SX',
    'SVK': 'SK',
    'SVN': 'SI',
    'SLB': 'SB',
    'SOM': 'SO',
    'ZAF': 'ZA',
    'SGS': 'GS',
    'KOR': 'KR',
    'SSD': 'SS',
    'ESP': 'ES',
    'LKA': 'LK',
    'SDN': 'SD',
    'SUR': 'SR',
    'SWZ': 'SZ',
    'SWE': 'SE',
    'CHE': 'CH',
    'SYR': 'SY',
    'TWN': 'TW',
    'TJK': 'TJ',
    'TZA': 'TZ',
    'THA': 'TH',
    'TGO': 'TG',
    'TKL': 'TK',
    'TON': 'TO',
    'TTO': 'TT',
    'TUN': 'TN',
    'TUR': 'TR',
    'TKM': 'TM',
    'TCA': 'TC',
    'TUV': 'TV',
    'UGA': 'UG',
    'UKR': 'UA',
    'ARE': 'AE',
    'GBR': 'GB',
    'USA': 'US',
    'VIR': 'VI',
    'URY': 'UY',
    'UZB': 'UZ',
    'VUT': 'VU',
    'VEN': 'VE',
    'VNM': 'VN',
    'WLF': 'WF',
    'ESH': 'EH',
    'YEM': 'YE',
    'ZMB': 'ZM',
    'ZWE': 'ZW',
}


def normalize_country(country):
    if not country:
            return

    if len(country) == 3:
        country = COUNTRIES_3_TO_2.get(country)

    if not country in COUNTRIES:
        return

    return country