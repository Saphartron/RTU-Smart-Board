import re

cell_value = "Vides un klimata ceļvedis, plkst. 16.30-19.50, 22.02., 29.02., 7.03., 14.03., 21.03. prof. G. Bažbauers Zoom"	
	

#RE Patterns
pattern1 = re.compile(r'(?P<subject>.*?)\s*(?P<type>lk\.|pr\.|lb)\s*(?P<teacher>.*?)\s*(?P<place>\d+|Zoom)(?P<extra>.*?)$')
pattern2 = re.compile(r'(?P<subject1>.*?),\s*(?P<week1>[\d.-]+\.ned\.)\s*(?P<teacher1>[^,]+),\s*(?P<time1>plkst\.\s*[\d:.]+-[\d:.]+),\s*(?P<place1>.*?)\s*(?P<subject2>.*?),\s*(?P<time2>plkst\.\s*[\d:.]+-[\d:.]+),\s*(?P<teacher2>[^,]+),\s*(?P<week2>.+?),\s*(?P<place2>.+)$')
pattern3 = re.compile(r'(?P<subject>.*?)(?:plkst\.)(?P<time>.*?)\s*(?:prof\.|lekt\.|doc\.)\s*(?P<teacher>.*?)\s*(?P<place>\d+|Zoom)$')

match1 = pattern1.match(cell_value)
match2 = pattern2.match(cell_value)
match3 = pattern3.match(cell_value)

if match1:  #1st pattern block
    
    subject = match1.group('subject').strip()
    raw_type = match1.group('type').strip()
    teacher = match1.group('teacher').strip()
    room = match1.group('place').strip()
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

elif match2: #2nd pattern block

    subject1 = match2.group('subject1').strip()
    time1 = match2.group('time1').strip()
    teacher1 = match2.group('teacher1').strip()
    place1 = match2.group('place1').strip()
    week1 = match2.group('week1').strip()

    subject2 = match2.group('subject2').strip()
    time2 = match2.group('time2').strip()
    teacher2 = match2.group('teacher2').strip()
    place2 = match2.group('place2').strip()
    week2 = match2.group('week2').strip()

    if subject2.startswith("Zoom"):
        place1 = "Zoom " + place1
        subject2 = subject2[len("Zoom"):].strip()

    print(" 1.\n")

    print(f'Prieksmets: {subject1}')
    print(f'Nedela: {week1}')
    print(f'Lektors: {teacher1}')
    print(f'Laiks: {time1}')
    print(f'Notiksanas vieta: {place1}')

    print("\n 2.\n")

    print(f'Prieksmets: {subject2}')
    print(f'Laiks: {time2}')
    print(f'Lektors: {teacher2}')
    print(f'Nedela: {week2}')
    print(f'Notiksanas vieta: {place2}')

elif match3:

    subject = match3.group('subject').strip()
    time = match3.group('time').strip()
    teacher = match3.group('teacher').strip()
    place = match3.group('place').strip()

    print(f'Prieksmets: {subject}')
    print(f'Laiks: {time}')
    print(f'Lektors: {teacher}')
    print(f'Notiksanas vieta: {place}')

else:
    print("none of the patterns matched")
