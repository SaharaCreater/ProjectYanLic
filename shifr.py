# Файл с функциями для шифровки и дешифровки сообщений
sp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
sp1 = 'abcdefghijklmnopqrstuvwxyz'
morse_sp_en = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'}
morse_sp_sym = {
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', "'": '.----.', '"': '.-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '/': '-..-.', '_': '..--.-', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '$': '...-..-', '@': '.--.-.', ' ': '/', '\n': '\n'}
morse_sp = {
    'А': '.-',    'Б': '-...',  'В': '.--',   'Г': '--.',   'Д': '-..',
    'Е': '.',     'Ж': '...-',  'З': '--..',  'И': '..',
    'Й': '.---',  'К': '-.-',   'Л': '.-..',  'М': '--',    'Н': '-.',
    'О': '---',   'П': '.--.',  'Р': '.-.',   'С': '...',   'Т': '-',
    'У': '..-',   'Ф': '..-.',  'Х': '....',  'Ц': '-..-',  'Ч': '---.',
    'Ш': '----',  'Щ': '--.-.',  'Ъ': '.--.-', 'Ы': '-.--',  'Ь': '-..-',
    'Э': '..-..', 'Ю': '..--',  'Я': '.-.-'}

# Функция для шифра Атбаш
def func_ashbat(text, name_file=None):
    # Выполняется если не введено название файла
    if not name_file:
        res = ''
        for i in text:
            if i.lower() in sp:
                if i.islower():
                    res += sp[len(sp) - sp.find(i.lower()) - 1]
                else:
                    res += sp[len(sp) - sp.find(i.lower()) - 1].upper()
            elif i.lower() in sp1:
                if i.islower():
                    res += sp1[len(sp1) - sp1.find(i.lower()) - 1]
                else:
                    res += sp1[len(sp1) - sp1.find(i.lower()) - 1].upper()
            else:
                res += i
        return res
    # Выполняется если введено название файла
    else:
        try:
            with open(name_file, 'r', encoding='utf-8') as w:
                f = open(f'{name_file}-Шифр Атбаш-output.txt', 'w', encoding='utf-8')
                for i in w:
                    for n in i:
                        if n.lower() in sp:
                            if n.islower():
                                f.write(sp[len(sp) - sp.find(n.lower())])
                            else:
                                f.write(sp[len(sp) - sp.find(n.lower())].upper())
                        elif n.lower() in sp1:
                            if n.islower():
                                f.write(sp1[len(sp1) - sp1.find(n.lower())])
                            else:
                                f.write(sp1[len(sp1) - sp1.find(n.lower())].upper())
                        else:
                            f.write(n)
                f.close()
            return 'OK'
        # проверка на наличие файла
        except FileNotFoundError:
            return 'Error'

# Функция для шифра Цезаря
def func_zesar(text, key, do, name_file=None):
    try:
        if key == '':
            key = 0
        else:
            key = int(key)
        if do == 'Расшифровать':
            key = -key
        # Выполняется если не введено название файла
        if not name_file:
            res = ''
            for i in text:
                if i.lower() in sp:
                    if i.islower():
                        res += sp[(sp.find(i.lower()) + key) % 33]
                    else:
                        res += sp[(sp.find(i.lower()) + key) % 33].upper()
                elif i.lower() in sp1:
                    if i.islower():
                        res += sp1[(sp1.find(i.lower()) + key) % 26]
                    else:
                        res += sp1[(sp1.find(i.lower()) + key) % 26].upper()
                else:
                    res += i
            return res
        # Выполняется если введено название файла
        else:
            try:
                with open(name_file, 'r', encoding='utf-8') as w:
                    f = open(f'{name_file}-Шифр Цезаря-output.txt', 'w', encoding='utf-8')
                    for n in w:
                        for i in n:
                            if i.lower() in sp:
                                if i.islower():
                                    f.write(sp[(sp.find(i.lower()) + key) % 33])
                                else:
                                    f.write(sp[(sp.find(i.lower()) + key) % 33].upper())
                            elif i.lower() in sp1:
                                if i.islower():
                                    f.write(sp1[(sp1.find(i.lower()) + key) % 26])
                                else:
                                    f.write(sp1[(sp1.find(i.lower()) + key) % 26].upper())
                            else:
                                f.write(i)
                    f.close()
                return 'OK'
            # проверка на наличие файла
            except FileNotFoundError:
                return 'Error'
    # проверка на корректность введеного ключа
    except ValueError:
        return 'Error'

# Функция для азбуки Морзе
def func_morse(text, do, key, name_file=None):
    try:
        if key == 'RU' or key == 'EN':
            # Выполняется если не введено название файла
            if not name_file:
                res = []
                res1 = ''
                if do == 'Зашифровать':
                    text = text.upper()
                    for i in text:
                        if key == 'RU':
                            if i in morse_sp:
                                res.append(morse_sp[i])
                            elif i in morse_sp_sym:
                                res.append(morse_sp_sym[i])
                        elif key == 'EN':
                            if i in morse_sp_en:
                                res.append(morse_sp_en[i])
                            elif i in morse_sp_sym:
                                res.append(morse_sp_sym[i])
                    return ' '.join(res)
                else:
                    reverse_morse_en = {v: k for k, v in morse_sp_en.items()}
                    reverse_morse = {v: k for k, v in morse_sp.items()}
                    reverse_morse_sym = {v: k for k, v in morse_sp_sym.items()}
                    for i in text.split(' '):
                        if key == 'RU':
                            if i in reverse_morse:
                                res1 += (reverse_morse[i]).lower()
                            elif i in reverse_morse_sym:
                                res1 += (reverse_morse_sym[i]).lower()
                        elif key == 'EN':
                            if i in reverse_morse_en:
                                res1 += (reverse_morse_en[i]).lower()
                            elif i in reverse_morse_sym:
                                res1 += (reverse_morse_sym[i]).lower()
                    return res1
            # Выполняется если введено название файла
            else:
                try:
                    sp = []
                    with open(name_file, 'r', encoding='utf-8') as w:
                        f = open(f'{name_file}-Азбука Морзе-output.txt', 'w', encoding='utf-8')
                        if do == 'Зашифровать':
                            if key == 'RU':
                                for n in w:
                                    for i in n:
                                        i = i.upper()
                                        if i in morse_sp:
                                            sp.append(morse_sp[i])
                                        elif i in morse_sp_sym:
                                            sp.append(morse_sp_sym[i])
                                    f.write(' '.join(sp))
                                    sp = []
                            elif key == 'EN':
                                for n in w:
                                    for i in n:
                                        i = i.upper()
                                        if i in morse_sp_en:
                                            sp.append(morse_sp_en[i])
                                        elif i in morse_sp_sym:
                                            sp.append(morse_sp_sym[i])
                                    f.write(' '.join(sp))
                                    sp = []
                        else:
                            reverse_morse_en = {v: k for k, v in morse_sp_en.items()}
                            reverse_morse = {v: k for k, v in morse_sp.items()}
                            reverse_morse_sym = {v: k for k, v in morse_sp_sym.items()}
                            if key == 'RU':
                                for n in w:
                                    for i in n.split():
                                        if i in reverse_morse:
                                            f.write(reverse_morse[i].lower())
                                        elif i in reverse_morse_sym:
                                            f.write(reverse_morse_sym[i].lower())
                                    f.write('\n')
                            elif key == 'EN':
                                for n in w:
                                    for i in n.split():
                                        if i in reverse_morse_en:
                                            f.write(reverse_morse_en[i].lower())
                                        elif i in reverse_morse_sym:
                                            f.write(reverse_morse_sym[i].lower())
                                    f.write('\n')
                        f.close()
                    return 'OK'
                # проверка на наличие файла
                except FileNotFoundError:
                    return 'Error'
        else:
            raise ValueError
    # проверка на корректность введеного ключа
    except ValueError:
        return 'Error'

# Функция для шифра Виженера
def func_vizenera(text, do, key, name_file=None):
    try:
        p = len(key)
        if not p:
            raise ValueError
        res = ''
        # Выполняется если не введено название файла
        if not name_file:
            if do == 'Зашифровать':
                for i in range(len(text)):
                    if text[i].lower() in sp:
                        if text[i].islower():
                            res += sp[(sp.index(text[i].lower()) + sp.index(key[i % p].lower())) % 33]
                        else:
                            res += sp[(sp.index(text[i].lower()) + sp.index(key[i % p].lower())) % 33].upper()
                    elif text[i] in sp1:
                        if text[i].islower():
                            res += sp1[(sp1.index(text[i].lower()) + sp1.index(key[i % p].lower())) % 26]
                        else:
                            res += sp1[(sp1.index(text[i].lower()) + sp1.index(key[i % p].lower())) % 26]
                    else:
                        res += text[i]
            else:
                for i in range(len(text)):
                    if text[i].lower() in sp:
                        if text[i].islower():
                            res += sp[(sp.index(text[i].lower()) - sp.index(key[i % p].lower())) % 33]
                        else:
                            res += sp[(sp.index(text[i].lower()) - sp.index(key[i % p].lower())) % 33].upper()
                    elif text[i] in sp1:
                        if text[i].islower():
                            res += sp1[(sp1.index(text[i].lower()) - sp1.index(key[i % p].lower())) % 26]
                        else:
                            res += sp1[(sp1.index(text[i].lower()) - sp1.index(key[i % p].lower())) % 26]
                    else:
                        res += text[i]
            return res
        # Выполняется если введено название файла
        else:
            try:
                with open(name_file, 'r', encoding='utf-8') as w:
                    f = open(f'{name_file}-Шифр Вернама-output.txt', 'w', encoding='utf-8')
                    if do == 'Зашифровать':
                        for n in w:
                            for i in range(len(n)):
                                if n[i].lower() in sp:
                                    if n[i].islower():
                                        f.write(sp[(sp.index(n[i].lower()) + sp.index(key[i % p].lower())) % 33])
                                    else:
                                        f.write(sp[(sp.index(n[i].lower()) +
                                                    sp.index(key[i % p].lower())) % 33].upper())
                                elif n[i] in sp1:
                                    if n[i].islower():
                                        f.write(sp1[(sp1.index(n[i].lower()) + sp1.index(key[i % p].lower())) % 26])
                                    else:
                                        f.write(sp1[(sp1.index(n[i].lower()) + sp1.index(key[i % p].lower())) % 26])
                                else:
                                    f.write(n[i])
                    else:
                        for n in w:
                            for i in range(len(n)):
                                if n[i].lower() in sp:
                                    if n[i].islower():
                                        f.write(sp[(sp.index(n[i].lower()) - sp.index(key[i % p].lower())) % 33])
                                    else:
                                        f.write(sp[(sp.index(n[i].lower()) -
                                                    sp.index(key[i % p].lower())) % 33].upper())
                                elif n[i] in sp1:
                                    if n[i].islower():
                                        f.write(sp1[(sp1.index(n[i].lower()) - sp1.index(key[i % p].lower())) % 26])
                                    else:
                                        f.write(sp1[(sp1.index(n[i].lower()) - sp1.index(key[i % p].lower())) % 26])
                                else:
                                    f.write(n[i])
                        f.close()
                    return 'OK'
            # проверка на наличие файла
            except FileNotFoundError:
                return 'Error'
    # проверка на корректность введеного ключа
    except ValueError:
        return 'Error'

# Функция для шифра Вернама
def func_vernama(text, do, key, name_file=None):
    try:
        key_len = len(key)
        if not key_len:
            raise ValueError
        key_int = [ord(i) for i in key]
        # Выполняется если не введено название файла
        if not name_file:
            res = []
            text_int = [ord(i) for i in text]
            if do == 'Зашифровать':
                for i in range(len(text_int)):
                    value = (text_int[i] + key_int[i % key_len]) % 1114112
                    res.append(chr(value))
                return ''.join(res)
            else:
                for i in range(len(text)):
                    value = (text_int[i] - key_int[i % key_len]) % 1114112
                    res.append(chr(value))
                return ''.join(res)
        # Выполняется если введено название файла
        else:
            try:
                with open(name_file, 'r', encoding='utf-8') as w:
                    f = open(f'{name_file}-Шифр Виженера-output.txt', 'w', encoding='utf-8')
                    text_int = [ord(i) for i in w.read()]
                    if do == 'Зашифровать':
                        for i in range(len(text_int)):
                            value = (text_int[i] + key_int[i % key_len]) % 1114112
                            f.write(chr(value))
                    else:
                        for i in range(len(text_int)):
                            value = (text_int[i] - key_int[i % key_len]) % 1114112
                            f.write(chr(value))
                    f.close()
                return 'OK'
            # проверка на наличие файла
            except FileNotFoundError:
                return 'Error'
    except ValueError:
        return 'Error'

