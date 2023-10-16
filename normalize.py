import re

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = dict()

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrillic)] = latin
    TRANS[ord(cyrillic.upper())] = latin.upper()


import re

def normalize(name: str) -> str:
    if '.' in name:
        name_without_extension, file_extension = name.rsplit('.', 1)
    else:
        return name

    translate_name = re.sub(r'\W', '_', name_without_extension.translate(TRANS))
    return f"{translate_name}.{file_extension}"




   # name_without_extension, file_extension = name.rsplit('.', 1)
    #name_without_extension = re.sub(r'\W', '_', name_without_extension)
    #return f"{name_without_extension}.{file_extension}"
