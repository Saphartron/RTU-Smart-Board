import re

cell_value = "Energobūvniecības un elektroenerģētikas nozaru tiesiskais regulējums, 1.-3.ned. lekt. G.Valdmanis, plkst. 16.30-19.50, Zoom Ķēžu teorija, plkst. 18:00-21:00, doc. A.Vītols, sākot ar 4.ned., Zoom"

last_zoom_index = cell_value.rfind("Zoom")  # Find the last occurrence of "Zoom"
first_subj = cell_value[:last_zoom_index].strip()
second_subj = cell_value[last_zoom_index:].strip()

# RE Patterns
pattern1 = re.compile(r'(?P<subject>.*?)\s*(?P<type>lk\.|pr\.|lb)\s*(?P<teacher>.*?)\s*(?P<room>\d+|Zoom)(?P<extra>.*?)$')
pattern2 = re.compile(r'(?P<subject>.*?)(?:plkst\.)(?P<time>.*?)\s*(?:prof\.|lekt\.|doc\.)\s*(?P<teacher>.*?)\s*(?P<room>\d+|Zoom)$')
pattern_combined = re.compile(r'(?P<subject>.*?),\s*(?P<weeks>.*?\.ned\.)\s*(?P<teacher>[^,]+),\s*(?P<time>plkst\.\s*.*?-.*?),\s*(?P<place>.*Zoom)')

match_combined = pattern_combined.match(first_subj + ", " + second_subj)  # Match both subjects together with pattern_combined

if match_combined:  # If match is successful
    subject1 = match_combined.group('subject').strip()
    weeks1 = match_combined.group('weeks').strip()
    teacher1 = match_combined.group('teacher').strip()
    time1 = match_combined.group('time').strip()
    place1 = match_combined.group('place').strip()

    print("1.")
    print(f'Prieksmets: {subject1}')
    print(f'Nedelas: {weeks1}')
    print(f'Lektors: {teacher1}')
    print(f'Laiks: {time1}')
    print(f'Notiksanas vieta: {place1}')
else:
    # Match individual subjects
    match1 = pattern1.match(first_subj)
    match2 = pattern2.match(second_subj)

    if match1:  # If first subject matches pattern1
        subject1 = match1.group('subject').strip()
        raw_type = match1.group('type').strip()
        teacher1 = match1.group('teacher').strip()
        room1 = match1.group('room').strip()
        extra1 = match1.group('extra').strip()

        type_mapping = {'lk.': 'Lekcija', 'pr.': 'Praktiska nodarbība', 'lb': 'Laboratorijas darbs'}

        if room1 == "Zoom":
            room_output1 = "Zoom"
        else:
            room_output1 = f'{room1} Kabinets'

        extra_category1 = 'Extra' if extra1 else None

        print("1.")
        print(f'Prieksmets: {subject1}')
        print(f'Nodarbibas veids: {type_mapping.get(raw_type, raw_type)}')
        print(f'Lektors: {teacher1}')
        print(f'Notiksanas vieta: {room_output1}')
        if extra_category1:
            print(f'Papildus informacija: {extra1}')

    if match2:  # If second subject matches pattern2
        subject2 = match2.group('subject').strip()
        time2 = match2.group('time').strip()
        teacher2 = match2.group('teacher').strip()
        room2 = match2.group('room').strip()

        print("2.")
        print(f'Prieksmets: {subject2}')
        print(f'Laiks: {time2}')
        print(f'Lektors: {teacher2}')
        print(f'Notiksanas vieta: {room2}')
