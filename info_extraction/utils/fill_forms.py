from PIL import ImageFont, ImageDraw
import numpy as np

def pick_x(start, r = 200):
    return np.random.choice([start + i for i in range(r)])

def make_letters():
    possible_text = ' qwertyuiopasdfghjklzxcvbnm'
    char = np.random.choice(list(possible_text), p=[0.15] + [0.85/36. for _ in range(36)], size=np.random.choice(range(4, 20)))
    s = ''
    for i in char:
        s += i
    return s

def make_name():
    chars = 'qwertyuiopasdfghjklzxcvbnm'
    s = np.random.choice(list(chars.upper()), size=1)[0]
    rest = np.random.choice(list(chars), size=np.random.choice(range(2, 9)))
    for char in rest:
        s += char
    return s

def make_number():
    chars = '1234567890'
    nums = np.random.choice(list(chars), size=10)
    s = ''
    for char in nums:
        s += char
    return s

def make_email():
    chars = 'qwertyuiopasdfghjklzxcvbnm.'
    start = np.random.choice(list(chars), size=np.random.choice(range(8, 14)))
    end = np.random.choice(list(chars), size=np.random.choice(range(4, 9)))
    s = ''
    for char in start:
        s += char
    s += '@'
    for char in end:
        s += char
    s += '.' + np.random.choice(['com', 'org', 'gov', 'net'])
    return s

def make_date(no_date=False):
    day = str(np.random.choice(range(1, 32), size=1)[0])
    month = str(np.random.choice(range(1, 13), size=1)[0])
    year = str(np.random.choice(range(1900, 2025), size=1)[0])
    if len(day) == 1:
        day = '0'+day
    if len(month) == 1:
        month = '0'+month
    if len(year) == 1:
        year = '0'+year
    if no_date:
        return month+'/'+year
    return month+'/'+day+'/'+year[-2:]

def draw_all(background, name_locations, number_locations, email_locations, date_locations):
    font = ImageFont.truetype(r'../Downloads/arial-relcom/KOI8_FIN.ttf', np.random.choice([26, 28, 30, 32, 34]))
    dr = ImageDraw.Draw(background)
    draw(name_locations, make_name, dr, font)
    draw(number_locations, make_number, dr, font)
    draw(email_locations, make_email, dr, font)
    draw(date_locations, make_date, dr, font)

def draw_all2(background, name_locations, number_locations, email_locations, date_locations):
    font = ImageFont.truetype(r'../Downloads/arial-relcom/KOI8_FIN.ttf', np.random.choice([26, 28, 30, 32, 34]))
    dr = ImageDraw.Draw(background)
    draw(name_locations, make_name, dr, font)
    draw(number_locations[:3], make_number, dr, font)
    draw(number_locations[3:], make_number, dr, ImageFont.truetype(r'../Downloads/arial-relcom/KOI8_FIN.ttf', 26))
    draw(email_locations, make_email, dr, font)
    draw(date_locations, make_date, dr, font)
    
def draw_all3(background, name_locations, number_locations, email_locations, date_locations):
    font = ImageFont.truetype(r'../Downloads/arial-relcom/KOI8_FIN.ttf', np.random.choice([26, 28, 30, 32, 34]))
    dr = ImageDraw.Draw(background)
    draw(name_locations, make_name, dr, font)
    draw(number_locations[-10:], make_number, dr, font)
    draw(number_locations[:-10], make_number, dr, ImageFont.truetype(r'../Downloads/arial-relcom/KOI8_FIN.ttf', 26))
    draw(email_locations, make_email, dr, font)
    draw(date_locations, make_date, dr, font)

def draw_all4(background, name_locations, number_locations, email_locations, date_locations):
    font = ImageFont.truetype(r'../Downloads/arial-relcom/KOI8_FIN.ttf', np.random.choice([26, 28, 30]))
    dr = ImageDraw.Draw(background)
    draw(name_locations, make_name, dr, font)
    draw(number_locations, make_number, dr, font)
    draw(email_locations, make_email, dr, font)
    draw(date_locations, make_date, dr, font)

def draw(locations, fn, draw, font):
    for location in locations:
        draw.text(location, fn(), (0,0,0), font=font)

def add_text_31v1_1(image):
    background = image.convert('RGB')
    name_locations = (
        (pick_x(100), 690), (pick_x(1130), 690), (pick_x(800), 790), 
        (pick_x(100), 948), (pick_x(360, 100), 1330), 
        (pick_x(360, 100), 1400), (pick_x(360, 100), 1470),
        (pick_x(660, 80),1330), (pick_x(660, 80),1400), (pick_x(660, 80),1470),
        (pick_x(1140, 80),1330), (pick_x(1140, 80),1400), (pick_x(1140, 80),1470),
        (pick_x(1850, 70),1330), (pick_x(1850, 70),1400), (pick_x(1850, 70),1470),
        (pick_x(900, 70), 1330)
    )
    number_locations = (
        (pick_x(100), 790), (pick_x(100), 1050), (pick_x(1610, 70), 1330),
        (pick_x(1610, 70), 1400), (pick_x(1610, 70), 1470)
    )
    email_locations = (
        (pick_x(1130), 948),
    )
    date_locations = (
        (pick_x(1400, 70), 1330), (pick_x(1400, 70), 1400), (pick_x(1400, 70), 1470)
        )
    draw_all(background, name_locations, number_locations, email_locations, date_locations)
        
    return background

def add_text_31v1_2(image):
    background = image.convert('RGB')
    all_names = ((
        (pick_x(360, 80), i), (pick_x(630, 80), i), (pick_x(920, 60), i),
        (pick_x(1160, 70), i), (pick_x(1850, 110), i) 
        
    ) for i in [j*70 + 150 for j in range(9)])
    name_locations = []
    for i in all_names:
        for j in i:
            name_locations.append(j)
    name_locations = tuple(name_locations)
    number_locations1 = (
        (pick_x(1610, 60), i) for i in [j*70 + 150 for j in range(9)]
    )
    number_locations2 = ((pick_x(660, 100), i) for i in [j*82 + 1065 for j in range(5)])
    number_locations3 = ((pick_x(1200, 100), i) for i in [j*82 + 1065 for j in range(5)])
    number_locations = []
    for i in number_locations1:
        number_locations.append(i)
    for i in number_locations2:
        number_locations.append(i)
    for i in number_locations3:
        number_locations.append(i)
    email_locations = (
        (pick_x(1650, 100), i) for i in [j*82 + 1065 for j in range(5)]
    )
    date_locations = (
        (pick_x(1380, 80), i) for i in [j*70 + 150 for j in range(9)]
        )
    draw_all(background, name_locations, number_locations, email_locations, date_locations)
        
    return background

def add_text_31v2_1(image):
    background = image.convert('RGB')
    name_locations = (
        (pick_x(250, 200), 762), (pick_x(1100, 250), 762), (pick_x(810, 190), 840), 
        (pick_x(470, 60), 1247), (pick_x(710, 60), 1247), (pick_x(930, 40), 1247), (pick_x(1130, 40), 1247), (pick_x(1730, 40), 1247),
        (pick_x(470, 60), 1302), (pick_x(710, 60), 1302), (pick_x(930, 40), 1302), (pick_x(1130, 40), 1302), (pick_x(1730, 40), 1302),
        (pick_x(470, 60), 1356), (pick_x(710, 60), 1356), (pick_x(930, 40), 1356), (pick_x(1130, 40), 1356), (pick_x(1730, 40), 1356),
        (pick_x(470, 60), 1406), (pick_x(710, 60), 1406), (pick_x(930, 40), 1406), (pick_x(1130, 40), 1406), (pick_x(1730, 40), 1406)
    )
    number_locations = (
        (pick_x(250, 160), 837), (pick_x(250, 400), 960), (pick_x(250, 400), 1038),
        (pick_x(1520, 20), 1247), (pick_x(1520, 20), 1302), (pick_x(1520, 20), 1356), (pick_x(1520, 20), 1406)
    )
    email_locations = (
        (pick_x(1100, 250), 960), (pick_x(1100, 250), 1038)
    )
    date_locations = (
        (pick_x(1340, 50), 1247), (pick_x(1340, 50), 1302), (pick_x(1340, 50), 1356), (pick_x(1340, 50), 1406)
    )
    draw_all2(background, name_locations, number_locations, email_locations, date_locations)
        
    return background

def add_text_31v2_2(image):
    background = image.convert('RGB')
    name_locations = (
        (pick_x(470, 60), 310), (pick_x(710, 60), 310), (pick_x(930, 40), 310), (pick_x(1130, 40), 310), (pick_x(1730, 40), 310),
        (pick_x(470, 60), 363), (pick_x(710, 60), 363), (pick_x(930, 40), 363), (pick_x(1130, 40), 363), (pick_x(1730, 40), 363),
        (pick_x(470, 60), 417), (pick_x(710, 60), 417), (pick_x(930, 40), 417), (pick_x(1130, 40), 417), (pick_x(1730, 40), 417),
        (pick_x(470, 60), 470), (pick_x(710, 60), 470), (pick_x(930, 40), 470), (pick_x(1130, 40), 470), (pick_x(1730, 40), 470),
        (pick_x(470, 60), 523), (pick_x(710, 60), 523), (pick_x(930, 40), 523), (pick_x(1130, 40), 523), (pick_x(1730, 40), 523),
        (pick_x(470, 60), 576), (pick_x(710, 60), 576), (pick_x(930, 40), 576), (pick_x(1130, 40), 576), (pick_x(1730, 40), 576),
        (pick_x(470, 60), 629), (pick_x(710, 60), 629), (pick_x(930, 40), 629), (pick_x(1130, 40), 629), (pick_x(1730, 40), 629),
        (pick_x(470, 60), 684), (pick_x(710, 60), 684), (pick_x(930, 40), 684), (pick_x(1130, 40), 684), (pick_x(1730, 40), 684),
        (pick_x(470, 60), 738), (pick_x(710, 60), 738), (pick_x(930, 40), 738), (pick_x(1130, 40), 738), (pick_x(1730, 40), 738),
    )
    number_locations = (
        (pick_x(1520, 20), 310), (pick_x(1520, 20), 363), (pick_x(1520, 20), 417), (pick_x(1520, 20), 470),
        (pick_x(1520, 20), 523), (pick_x(1520, 20), 576), (pick_x(1520, 20), 629), (pick_x(1520, 20), 684),
        (pick_x(1520, 20), 738),
        (pick_x(750, 120), 1012), (pick_x(750, 120), 1075), (pick_x(750, 120), 1137), (pick_x(750, 120), 1201), (pick_x(750, 120), 1262),
        (pick_x(1200, 80), 1012), (pick_x(1200, 80), 1075), (pick_x(1200, 80), 1137), (pick_x(1200, 80), 1201), (pick_x(1200, 80), 1262),
    )
    email_locations = (
        (pick_x(1510, 40), 1012), (pick_x(1510, 40), 1075), (pick_x(1510, 40), 1137), (pick_x(1510, 40), 1201), (pick_x(1510, 40), 1262),
    )
    date_locations = (
        (pick_x(1330, 30), 310), (pick_x(1330, 30), 363), (pick_x(1330, 30), 417), (pick_x(1330, 30), 470),
        (pick_x(1330, 30), 523), (pick_x(1330, 30), 576), (pick_x(1330, 30), 629), (pick_x(1330, 30), 684),
        (pick_x(1330, 30), 738)
    )
    draw_all3(background, name_locations, number_locations, email_locations, date_locations)
        
    return background

def add_text_32v1_1(image):
    background = image.convert('RGB')
    name_locations = (
        (pick_x(100, 400), 459), ((pick_x(1130, 300), 459)), (pick_x(800), 559),
        (pick_x(90, 170), 1001), (pick_x(90, 170), 1048), (pick_x(90, 170), 1093), (pick_x(90, 170), 1135),
        (pick_x(1050, 200), 1001), (pick_x(1050, 200), 1048), (pick_x(1050, 200), 1093), (pick_x(1050, 200), 1135),
        (pick_x(1650, 200), 1001), (pick_x(1650, 200), 1048), (pick_x(1650, 200), 1093), (pick_x(1650, 200), 1135)
    )
    number_locations = (
        (pick_x(100), 559), (pick_x(100), 715), (pick_x(100), 1050 - 238),
        (pick_x(720, 90), 1507), (pick_x(720, 90), 1546), (pick_x(1200, 90), 1507), (pick_x(1200, 90), 1546)
    )
    email_locations = (
        (pick_x(1130, 200), 948 - 238), (pick_x(1130, 200), 1050 - 238),
        (pick_x(1640, 90), 1507), (pick_x(1640, 90), 1546)
    )
    date_locations = (
        (pick_x(480, 60), 1001), (pick_x(480, 60), 1048), (pick_x(480, 60), 1093), (pick_x(480, 60), 1135),
        (pick_x(730, 60), 1001), (pick_x(730, 60), 1048), (pick_x(730, 60), 1093), (pick_x(730, 60), 1135)
    )
    draw_all(background, name_locations, number_locations, email_locations, date_locations)
        
    return background

def add_text_32v1_2(image):
    background = image.convert('RGB')
    name_locations = [
        (pick_x(490, 50), i*40 + 386) for i in range(13)
    ] + [
        (pick_x(750, 50), i*40 + 386) for i in range(13)
    ] + [
        (pick_x(1000, 50), i*40 + 386) for i in range(13)
    ] + [
        (pick_x(1250, 50), i*40 + 386) for i in range(13)
    ] + [
        (pick_x(1910, 50), i*40 + 386) for i in range(13)
    ] + [
        (pick_x(190, 50), i*40 + 1236) for i in range(9)
    ] + [
        (pick_x(1650, 50), i*40 + 1236) for i in range(9)
    ]
    number_locations = [
        (pick_x(1660, 40), i*40 + 386) for i in range(13)
    ] + [
        (pick_x(1230, 40), i*40 + 128) for i in range(3)
    ] + [
        (pick_x(760, 40), i*40 + 128) for i in range(3)
    ] 
    email_locations = [
        (pick_x(1650, 100), i*40 + 128) for i in range(3)
    ]
    date_locations = [
        (pick_x(1450, 50), i*40 + 386) for i in range(13)
    ] + [
        (pick_x(660, 50), i*40 + 1236) for i in range(9)
    ] + [
        (pick_x(1065, 50), i*40 + 1236) for i in range(9)
    ]
    draw_all(background, name_locations, number_locations, email_locations, date_locations)
        
    return background

def add_text_32v2_1(image):
    background = image.convert('RGB')
    name_locations = [
        (pick_x(220, 400), 579), ((pick_x(1130, 500), 579)), (pick_x(800, 200), 659), 
    ] + [
        (pick_x(260, 100), i*33 + 1009) for i in range(7)
    ] + [
        (pick_x(1060, 100), i*33 + 1009) for i in range(7)
    ] + [
        (pick_x(1600, 100), i*33 + 1009) for i in range(7)
    ]
    number_locations = (
        (pick_x(240, 180), 659), (pick_x(240, 200), 780), (pick_x(240, 200), 856),
        (pick_x(720, 90), 1394), (pick_x(720, 90), 1426), (pick_x(1160, 90), 1394), (pick_x(1160, 90), 1426)
    )
    email_locations = (
        (pick_x(1130, 200), 780), (pick_x(1130, 200), 856),
        (pick_x(1530, 90), 1394), (pick_x(1530, 90), 1426)
    )
    date_locations = [
        (pick_x(582, 40), int(i*33.5 + 1009)) for i in range(7)
    ] + [
        (pick_x(780, 40), int(i*33.5 + 1009)) for i in range(7)
    ]
    draw_all(background, name_locations, number_locations, email_locations, date_locations)
        
    return background

def add_text_32v2_2(image):
    background = image.convert('RGB')
    name_locations = [
        (pick_x(575, 30), int(i*30.6 + 491)) for i in range(13)
    ] + [
        (pick_x(780, 50), int(i*30.6 + 491)) for i in range(13)
    ] + [
        (pick_x(1000, 50), int(i*30.6 + 491)) for i in range(13)
    ] + [
        (pick_x(1190, 20), int(i*30.6 + 491)) for i in range(13)
    ] + [
        (pick_x(1740, 50), int(i*30.6 + 491)) for i in range(13)
    ] + [
        (pick_x(325, 50), int(i*30.6 + 1138)) for i in range(9)
    ] + [
        (pick_x(1400, 300), int(i*30.6 + 1138)) for i in range(9)
    ]
    number_locations = [
        (pick_x(1530, 20), int(i*30.6 + 491)) for i in range(13)
    ] + [
        (pick_x(1200, 40), int(i*30.6 + 295)) for i in range(3)
    ] + [
        (pick_x(773, 40), int(i*30.6 + 295)) for i in range(3)
    ] 
    email_locations = [
        (pick_x(1520, 100), int(i*30.6 + 295)) for i in range(3)
    ]
    date_locations = [
        (pick_x(1380, 30), int(i*30.6 + 491)) for i in range(13)
    ] + [
        (pick_x(710, 50), int(i*30.6 + 1138)) for i in range(9)
    ] + [
        (pick_x(1025, 80), int(i*30.6 + 1138)) for i in range(9)
    ]
    draw_all4(background, name_locations, number_locations, email_locations, date_locations)
        
    return background

def add_text_31v1_3(image):
    background = image.convert('RGB')
    name_locations = (
        (pick_x(500, 70), 180), (pick_x(1000, 150), 180), (pick_x(1700, 120), 180), (pick_x(980, 220), 280), 
        (pick_x(80, 420), 480), (pick_x(1200, 420), 480), 
    )
    number_locations = (
        (pick_x(80, 120), 280), (pick_x(480, 120), 280), 
    )
    email_locations = (
    )
    date_locations = (
        (pick_x(80, 50), 180), (pick_x(80, 400), 380),
        )
    draw_all(background, name_locations, number_locations, email_locations, date_locations)
        
    return background

def make_country():
    countries = [
        'afghanistan',
        'albania',
        'algeria',
        'american samoa',
        'andorra',
        'angola',
        'anguilla',
        'antarctica',
        'antigua and barbuda',
        'argentina',
        'armenia',
        'aruba',
        'australia',
        'austria',
        'azerbaijan',
        'bahamas',
        'bahrain',
        'bangladesh',
        'barbados',
        'belarus',
        'belgium',
        'belize',
        'benin',
        'bermuda',
        'bhutan',
        'bolivia',
        'bosnia and herzegovina',
        'botswana',
        'bouvet island',
        'brazil',
        'british indian ocean territory',
        'brunei darussalam',
        'bulgaria',
        'burkina faso',
        'burundi',
        'cambodia',
        'cameroon',
        'canada',
        'cape verde',
        'cayman islands',
        'central african republic',
        'chad',
        'chile',
        'china',
        'christmas island',
        'cocos islands',
        'colombia',
        'comoros',
        'congo',
        'democratic republic of congo',
        'drc',
        'republic of congo', 
        'congo republic',
        'cook islands',
        'costa rica',
        "cã”te d'ivoirecroatia",
        'cuba',
        'cyprus',
        'czech republic',
        'denmark',
        'djibouti',
        'dominica',
        'dominican republic',
        'ecuador',
        'egypt',
        'el salvador',
        'equatorial guinea',
        'eritrea',
        'estonia',
        'ethiopia',
        'falkland islands',
        'faroe islands',
        'fiji',
        'finland',
        'france',
        'french guiana',
        'french polynesia',
        'french southern territories',
        'gabon',
        'gambia',
        'georgia',
        'germany',
        'ghana',
        'gibraltar',
        'greece',
        'greenland',
        'grenada',
        'guadeloupe',
        'guam',
        'guatemala',
        'guinea',
        'guinea',
        'guyana',
        'haiti',
        'heard island and mcdonald islands',
        'honduras',
        'hong kong',
        'hungary',
        'iceland',
        'india',
        'indonesia',
        'iran',
        'iraq',
        'ireland',
        'israel',
        'italy',
        'jamaica',
        'japan',
        'jordan',
        'kazakhstan',
        'kenya',
        'kiribati',
        "north korea",
        "south korea",
        "korea"
        'kuwait',
        'kyrgyzstan',
        "laosa",
        'lebanon',
        'lesotho',
        'liberia',
        'libya',
        'liechtenstein',
        'lithuania',
        'luxembourg',
        'macao',
        'macedonia',
        'madagascar',
        'malawi',
        'malaysia',
        'maldives',
        'mali',
        'malta',
        'marshall islands',
        'martinique',
        'mauritania',
        'mauritius',
        'mayotte',
        'mexico',
        'micronesia',
        'moldova',
        'monaco',
        'mongolia',
        'montserrat',
        'morocco',
        'mozambique',
        'myanmar',
        'namibia',
        'nauru',
        'nepal',
        'netherlands',
        'new caledonia',
        'new zealand',
        'nicaragua',
        'niger',
        'nigeria',
        'niue',
        'norfolk island',
        'northern mariana islands',
        'norway',
        'oman',
        'pakistan',
        'palau',
        'palestine',
        'panama',
        'papua new guinea',
        'paraguay',
        'peru',
        'philippines',
        'pitcairn',
        'poland',
        'portugal',
        'puerto rico',
        'qatar',
        'reunion',
        'romania',
        'russia',
        'rwanda',
        'saint helena',
        'saint kitts and nevis',
        'saint lucia',
        'saint pierre and miquelon',
        'saint vincent',
        'samoa',
        'san marino',
        'sao tome and principe',
        'saudi arabia',
        'senegal',
        'serbia and montenegro',
        'seychelles',
        'sierra leone',
        'singapore',
        'slovakia',
        'slovenia',
        'solomon islands',
        'somalia',
        'south africa',
        'spain',
        'sri lanka',
        'sudan',
        'suriname',
        'svalbard and jan mayen',
        'swaziland',
        'sweden',
        'switzerland',
        'syria',
        'taiwan',
        'tajikistan',
        'tanzania',
        'thailand',
        'timor',
        'togo',
        'tokelau',
        'tonga',
        'trinidad and tobago',
        'tunisia',
        'turkey',
        'turkmenistan',
        'turks and caicos islands',
        'tuvalu',
        'uganda',
        'ukraine',
        'united arab emirates',
        'united kingdom',
        'united states',
        'uruguay',
        'uzbekistan',
        'vanuatu',
        'viet nam',
        'british virgin islands',
        'u.s. virgin islands',
        'wallis and futuna',
        'western sahara',
        'yemen',
        'zimbabwe'
    ]
    country = np.random.choice(countries)
    ret = ''
    for s in country.split():
        if s != 'and':
            t = s[0].upper()
            for i in s[1:]:
                t += i
            ret += ' ' + t
        else:
            ret += ' ' + s
    return ret[1:]
