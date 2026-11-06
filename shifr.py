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
    'А': '.-',   'Б': '-...', 'В': '.--',  'Г': '--.',  'Д': '-..',
    'Е': '.',    'Ж': '...-', 'З': '--..', 'И': '..',
    'Й': '.---', 'К': '-.-',  'Л': '.-..', 'М': '--',   'Н': '-.',
    'О': '---',  'П': '.--.', 'Р': '.-.',  'С': '...',  'Т': '-',
    'У': '..-',  'Ф': '..-.', 'Х': '....', 'Ц': '-..-', 'Ч': '---.',
    'Ш': '----', 'Щ': '--.-.', 'Ъ': '.--.-', 'Ы': '-.--', 'Ь': '-..-',
    'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'}

_rev_morse_en  = {v: k for k, v in morse_sp_en.items()}
_rev_morse_ru  = {v: k for k, v in morse_sp.items()}
_rev_morse_sym = {v: k for k, v in morse_sp_sym.items()}

_UNICODE_MOD = 0x110000

def _apply(transformer, text=None, name_file=None, suffix=''):
    """Если name_file — читаем, применяем, пишем. Иначе — применяем к text."""
    if not name_file:
        return transformer(text)
    try:
        with open(name_file, 'r', encoding='utf-8', newline='') as f:
            content = f.read()
    except FileNotFoundError:
        return 'Error'
    result = transformer(content)
    with open(f'{name_file}-{suffix}-output.txt', 'w', encoding='utf-8', newline='') as f:
        f.write(result)
    return 'OK'

def _atbash(text):
    out = []
    for ch in text:
        low = ch.lower()
        if low in sp:
            idx = 32 - sp.index(low)          # 32 = len(sp) - 1
            out.append(sp[idx] if ch.islower() else sp[idx].upper())
        elif low in sp1:
            idx = 25 - sp1.index(low)         # 25 = len(sp1) - 1
            out.append(sp1[idx] if ch.islower() else sp1[idx].upper())
        else:
            out.append(ch)
    return ''.join(out)


def func_ashbat(text, name_file=None):
    return _apply(_atbash, text, name_file, 'Шифр Атбаш')


def _caesar(text, shift):
    out = []
    for ch in text:
        low = ch.lower()
        if low in sp:
            idx = (sp.index(low) + shift) % 33
            out.append(sp[idx] if ch.islower() else sp[idx].upper())
        elif low in sp1:
            idx = (sp1.index(low) + shift) % 26
            out.append(sp1[idx] if ch.islower() else sp1[idx].upper())
        else:
            out.append(ch)
    return ''.join(out)


def func_zesar(text, key, do, name_file=None):
    try:
        shift = int(key) if key != '' else 0
    except ValueError:
        return 'Error'
    if do == 'Расшифровать':
        shift = -shift
    return _apply(lambda t: _caesar(t, shift), text, name_file, 'Шифр Цезаря')


def _morse_encode(text, key):
    table = morse_sp if key == 'RU' else morse_sp_en
    tokens = []
    for ch in text:
        up = ch.upper()
        if up in table:
            tokens.append(table[up])
        elif ch in morse_sp_sym:
            tokens.append(morse_sp_sym[ch])
    return ' '.join(tokens)


def _morse_decode(text, key):
    rev = _rev_morse_ru if key == 'RU' else _rev_morse_en
    chars = []
    for token in text.split(' '):
        if not token:
            continue
        if token in rev:
            chars.append(rev[token].lower())
        elif token in _rev_morse_sym:
            chars.append(_rev_morse_sym[token].lower())
    return ''.join(chars)


def func_morse(text, do, key, name_file=None):
    if key not in ('RU', 'EN'):
        return 'Error'
    fn = (lambda t: _morse_encode(t, key)) if do == 'Зашифровать' \
         else (lambda t: _morse_decode(t, key))
    return _apply(fn, text, name_file, 'Азбука Морзе')


def _vizenera(text, do, key):
    key_lower = key.lower()
    if not key_lower:
        raise ValueError('empty key')
    sign = 1 if do == 'Зашифровать' else -1
    out = []
    pos = 0
    for ch in text:
        low = ch.lower()
        if low in sp:
            k = key_lower[pos % len(key_lower)]
            if k not in sp:
                raise ValueError('key alphabet mismatch')
            idx = (sp.index(low) + sign * sp.index(k)) % 33
            out.append(sp[idx] if ch.islower() else sp[idx].upper())
            pos += 1
        elif low in sp1:
            k = key_lower[pos % len(key_lower)]
            if k not in sp1:
                raise ValueError('key alphabet mismatch')
            idx = (sp1.index(low) + sign * sp1.index(k)) % 26
            out.append(sp1[idx] if ch.islower() else sp1[idx].upper())
            pos += 1
        else:
            out.append(ch)
    return ''.join(out)


def func_vizenera(text, do, key, name_file=None):
    try:
        return _apply(lambda t: _vizenera(t, do, key), text, name_file, 'Шифр Виженера')
    except ValueError:
        return 'Error'


def _vernam(text, do, key):
    if not key:
        raise ValueError('empty key')
    key_int = [ord(c) for c in key]
    sign = 1 if do == 'Зашифровать' else -1
    out = []
    for i, ch in enumerate(text):
        v = (ord(ch) + sign * key_int[i % len(key_int)]) % _UNICODE_MOD
        out.append(chr(v))
    return ''.join(out)


def func_vernama(text, do, key, name_file=None):
    try:
        return _apply(lambda t: _vernam(t, do, key), text, name_file, 'Шифр Вернама')
    except ValueError:
        return 'Error'