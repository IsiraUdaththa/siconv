import re

# Define dictionaries to store mappings for vowels, consonants, special consonants, and special characters
vowels = {
    'oo': 'ඌ', 'o\\)': 'ඕ', 'oe': 'ඕ', 'aa': 'ආ', 'a\\)': 'ආ', 'Aa': 'ඈ',
    'A\\)': 'ඈ', 'ae': 'ඈ', 'ii': 'ඊ', 'i\\)': 'ඊ', 'ie': 'ඊ', 'ee': 'ඊ',
    'ea': 'ඒ', 'e\\)': 'ඒ', 'ei': 'ඒ', 'uu': 'ඌ', 'u\\)': 'ඌ', 'au': 'ඖ',
    '/\\a': 'ඇ', 'a': 'අ', 'A': 'ඇ', 'i': 'ඉ', 'e': 'එ', 'u': 'උ', 'o': 'ඔ',
    'I': 'ඓ'
}

vowel_modifiers = {
    'oo': 'ූ', 'o\\)': 'ෝ', 'oe': 'ෝ', 'aa': 'ා', 'a\\)': 'ා', 'Aa': 'ෑ',
    'A\\)': 'ෑ', 'ae': 'ෑ', 'ii': 'ී', 'i\\)': 'ී', 'ie': 'ී', 'ee': 'ී',
    'ea': 'ේ', 'e\\)': 'ේ', 'ei': 'ේ', 'uu': 'ූ', 'u\\)': 'ූ', 'au': 'ෞ',
    '/\\a': 'ැ', 'a': '', 'A': 'ැ', 'i': 'ි', 'e': 'ෙ', 'u': 'ු', 'o': 'ො',
    'I': 'ෛ'
}

special_consonants = {
    '/\\n/g': 'ං', '/\\h/g': 'ඃ', '/\\N/g': 'ඞ', '/\\R/g': 'ඍ', '/R/g': 'ර්‍',
    '/\\r/g': 'ර්‍'
}

consonants = {
    'nnd': 'ඬ', 'nndh': 'ඳ', 'nng': 'ඟ', 'Th': 'ථ', 'Dh': 'ධ', 'gh': 'ඝ',
    'Ch': 'ඡ', 'ph': 'ඵ', 'bh': 'භ', 'sh': 'ශ', 'Sh': 'ෂ', 'GN': 'ඥ',
    'KN': 'ඤ', 'Lu': 'ළු', 'dh': 'ද', 'ch': 'ච', 'kh': 'ඛ', 'th': 'ත',
    't': 'ට', 'k': 'ක', 'd': 'ඩ', 'n': 'න', 'p': 'ප', 'b': 'බ', 'm': 'ම',
    '\\u005C' + 'y': '‍ය', 'Y': '‍ය', 'y': 'ය', 'j': 'ජ', 'l': 'ල', 'v': 'ව',
    'w': 'ව', 's': 'ස', 'h': 'හ', 'N': 'ණ', 'L': 'ළ', 'K': 'ඛ', 'G': 'ඝ',
    'T': 'ඨ', 'D': 'ඪ', 'P': 'ඵ', 'B': 'ඹ', 'f': 'ෆ', 'q': 'ඣ', 'g': 'ග',
    'r': 'ර'
}

special_chars = {
    'ruu': 'ෲ', 'ru': 'ෘ'
}


def singlish_to_sinhala(text):
    # Special consonants
    for pattern, replacement in special_consonants.items():
        text = text.replace(pattern, replacement)

    # Consonants + special characters
    for sc, sc_uni in special_chars.items():
        for c, c_uni in consonants.items():
            pattern = re.escape(c + sc)
            replacement = c_uni + sc_uni
            text = re.sub(pattern, replacement, text)

    # Consonants + Rakaransha + vowel modifiers
    for c, c_uni in consonants.items():
        for v, v_uni in vowels.items():
            pattern = re.escape(c + "r" + v)
            replacement = c_uni + "්‍ර" + vowel_modifiers[v]
            text = re.sub(pattern, replacement, text)
        pattern = re.escape(c + "r")
        replacement = c_uni + "්‍ර"
        text = re.sub(pattern, replacement, text)

    # Consonants + vowel modifiers
    for c, c_uni in consonants.items():
        for v, v_uni in vowels.items():
            pattern = re.escape(c + v)
            replacement = c_uni + vowel_modifiers[v]
            text = re.sub(pattern, replacement, text)

    # Consonants + HAL
    for c, c_uni in consonants.items():
        pattern = re.escape(c)
        replacement = c_uni + "්"
        text = re.sub(pattern, replacement, text)

    # Vowels
    for v, v_uni in vowels.items():
        pattern = re.escape(v)
        replacement = v_uni
        text = re.sub(pattern, replacement, text)

    return text
