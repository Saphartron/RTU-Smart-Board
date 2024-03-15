import re

cell_value = "Elektrotehnika un elektronika lk. doc.L.Lavrinoviča 116"	


#RE Patterns
pattern1 = re.compile(r'(?P<subject>.*?)\s*(?P<type>lk\.|pr\.|lb)\s*(?P<teacher>.*?)\s*(?P<room>\d+|Zoom)(?P<extra>.*?)$')
pattern2 = re.compile(r'(?P<subject>.*?)(?:plkst\.)(?P<time_range>.*?)\s*(?:prof\.|lekt\.|doc\.)\s*(?P<professor>.*?)\s*(?P<room>\d+|Zoom)$')

match1 = pattern1.match(cell_value)
match2 = pattern2.match(cell_value)

if match1:
    subject = match1.group('subject').strip()
    raw_type = match1.group('type').strip()
    teacher = match1.group('teacher').strip()
    room = match1.group('room').strip()
    extra = match1.group('extra').strip()

    type_mapping = {'lk.': 'Lekcija', 'pr.': 'Praktiska nodarbība', 'lb': 'Laboratorijas darbs'}

    if room == "Zoom":
        room_output = "Zoom"
    else:
        room_output = f'{room} Kabinets'

    extra_category = 'Extra' if extra else None

    print(f'Prieksmets: {subject}')
    print(f'Nodarbibas veids: {type_mapping.get(raw_type, raw_type)}')
    print(f'Lektors: {teacher}')
    print(f'Notiksanas vieta: {room_output}')
    if extra_category:
        print(f'Papildus informacija: {extra}')

elif match2:

    subject = match2.group('subject').strip()
    time_range = match2.group('time_range').strip()
    professor = match2.group('professor').strip()
    room = match2.group('room').strip()

    print(f'Prieksmets: {subject}')
    print(f'Laiks: {time_range}')
    print(f'Lektors: {professor}')
    print(f'Notiksanas vieta: {room}')
