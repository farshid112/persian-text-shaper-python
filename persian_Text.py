import arabic_reshaper
from bidi.algorithm import get_display


def isEnglish(s):
    try:
        str(s).encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def persian_(*text):
    if len(list(str(*text).split(','))) == 1 and isEnglish(*text) == 0:
        return get_display(arabic_reshaper.reshape(*text))
    else:
        textlist = []
        for ABC in list(*text):
            if str(ABC).isdigit() == 1:
                textlist.append(ABC)
            elif isEnglish(ABC) == 1:
                textlist.append(ABC)
            else:
                textlist.append((get_display(arabic_reshaper.reshape(ABC))))
        return textlist
