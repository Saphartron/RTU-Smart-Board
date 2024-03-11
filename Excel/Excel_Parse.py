import re

cell_value = "Matematika[2/2] lk. doc. M. Dobkevica 219"

#RE Pattern
pattern = re.compile(r'(?P<subject>.*?)\s*(?P<type>lk\.|pr\.|lb)\s*(?P<teacher>.*?)\s*(?P<room>\d+|Zoom)(?P<extra>.*?)$')

match = pattern.match(cell_value)

if match:
    subject = match.group('subject').strip()
    raw_type = match.group('type').strip()
    teacher = match.group('teacher').strip()
    room = match.group('room').strip()
    extra = match.group('extra').strip()

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
else:
    print('Pattern didnt match.')
