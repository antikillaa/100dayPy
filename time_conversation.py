s = '06:40:03AM'

hours = s.split(':')[0]
minutes = s.split(':')[1]
seconds = s.split(':')[2][:2]
am_pm = s.split(':')[-1][-2:]


formatted_hours = ''

if am_pm == 'PM':
    match hours:
        case '01':
            formatted_hours = '13'
        case '02':
            formatted_hours = '14'
        case '03':
            formatted_hours = '15'
        case '04':
            formatted_hours = '16'
        case '05':
            formatted_hours = '17'
        case '06':
            formatted_hours = '18'
        case '07':
            formatted_hours = '19'
        case '08':
            formatted_hours = '20'
        case '09':
            formatted_hours = '21'
        case '10':
            formatted_hours = '22'
        case '11':
            formatted_hours = '23'
        case '12':
            formatted_hours = '12'
elif am_pm == 'AM' and hours == '12':
    formatted_hours = '00'
else:
    formatted_hours = hours

print(f'{formatted_hours}:{minutes}:{seconds}')