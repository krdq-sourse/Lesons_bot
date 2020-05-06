import datetime
now = datetime.datetime.now()
def whatPara(hour, minute):
    if hour < 8:
        return '0'
    if (hour == 9 and minute <= 20) or (hour == 8):
        return '1'
    if (hour == 9 and minute >= 30) or (hour == 10 and minute <= 50):
        return '2'
    if (hour == 10 and minute >= 55) or hour == 11 or (hour == 12 and minute <= 15):
        return '3'
    if (hour == 12 and minute >= 40) or hour == 13 or (hour <= 14 and minute == 0):
        return '4'
    if (hour == 14 and minute >= 5) or (hour == 15 and minute <= 25):
        return '5'
    if (hour == 15 and minute >= 35) or (hour == 16 and minute <= 55):
        return '6'
    if (hour == 17) or (hour == 19 and minute <= 20):
        return '7'
    if hour > 19:
        return '0'
    return '|'


def getPara():
    # para = whatPara(int(input('h')), int(input('m')))
    day = now.weekday()
    para = whatPara(now.hour, now.minute)
    if para == '0' or day == 6 or day == 5:
        return 'her.webp'
    if para == '|':
        return 'chill.webp'
    if day == 0:
        unit_to_multiplier = {
            '1': 'her.webp',
            '2': 'eng.webp',
            '3': 'os.webp',
            '4': 'os.webp',
            '5': 'net.webp',
            '6': 'her.webp',
            '7': 'her.webp'
        }
    if day == 1:
        unit_to_multiplier = {
            '1': 'her.webp',
            '2': 'alg.webp',
            '3': 'alg.webp',
            '4': 'alg.webp',
            '5': 'Math.webp',
            '6': 'Math.webp',
            '7': 'her.webp'
        }
    if day == 2:
        unit_to_multiplier = {
            '1': 'her.webp',
            '2': 'Math.webp',
            '3': 'kpz.webp',
            '4': 'opp.webp',
            '5': 'hui.webp',
            '6': 'kpz.webp',
            '7': 'her.webp'
        }
    if day == 3:
        unit_to_multiplier = {
            '1': 'her.webp',
            '2': 'alg.webp',
            '3': 'alg.webp',
            '4': 'opp.webp',
            '5': 'bd.webp',
            '6': 'alg.webp',
            '7': 'her.webp'
        }
    if day == 4:
        unit_to_multiplier = {
            '1': 'her.webp',
            '2': 'web.webp',
            '3': 'web.webp',
            '4': 'web.webp',
            '5': 'opp.webp',
            '6': 'opp.webp',
            '7': 'her.webp'
        }
    return unit_to_multiplier[para]
