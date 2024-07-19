vowels = [
    "අ",
    "ආ",
    "ඇ",
    "ඈ",
    "ඉ",
    "ඊ",
    "උ",
    "ඌ",
    "ඍ",
    "ඎ",
    "ඏ",
    "ඐ",
    "එ",
    "ඒ",
    "ඓ",
    "ඔ",
    "ඕ",
    "ඖ"
]

pillam = [
    "ං",
    "ඃ",
    "්",
    "ා",
    "ැ",
    "ෑ",
    "ි",
    "ී",
    "ු",
    "ූ",
    "ෘ",
    "ෙ",
    "ේ",
    "ෛ",
    "ො",
    "ෝ",
    "ෞ",
    "ෟ",
    "ෲ",
    "ෳ",
    "\u200d"]

special_character_list = ["1",
                          "2",
                          "3",
                          "4",
                          "5",
                          "6",
                          "7",
                          "8",
                          "9",
                          "0",
                          ":",
                          ";",
                          ".",
                          "-",
                          ",",
                          "/",
                          " ",
                          "\n"]  # *** cant inseart "\" to here ??? :o

english_alphabet = ["A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "F",
                    "G",
                    "H",
                    "I",
                    "J",
                    "K",
                    "L",
                    "M",
                    "N",
                    "O",
                    "P",
                    "Q",
                    "R",
                    "S",
                    "T",
                    "U",
                    "V",
                    "W",
                    "X",
                    "Y",
                    "Z",
                    "a",
                    "b",
                    "c",
                    "d",
                    "e",
                    "f",
                    "g",
                    "h",
                    "i",
                    "j",
                    "k",
                    "l",
                    "m",
                    "n",
                    "o",
                    "p",
                    "q",
                    "r",
                    "s",
                    "t",
                    "u",
                    "v",
                    "w",
                    "x",
                    "y",
                    "z"]

symbols = ["~",
           "`",
           "!",
           "@",
           "#",
           "$",
           "%",
           "^",
           "&",
           "*",
           "(",
           ")",
           "_",
           "+",
           "=",
           "[",
           "]",
           "{",
           "}",
           "|",
           "\u0009",
           "?",
           "<",
           ">"]

case1_map = {
    "ං": "ŋ",
    "ඃ": "h",
    "අ": "a",
    "ආ": "a:",
    "ඇ": "æ",
    "ඈ": "æ:",
    "ඉ": "i",
    "ඊ": "i:",
    "උ": "u",
    "ඌ": "u:",
    "ඍ": "ri",
    "ඎ": "ru:",
    "ඏ": "ilu",
    "ඐ": "ilu:",
    "එ": "e",
    "ඒ": "e:",
    "ඓ": "ai",
    "ඔ": "o",
    "ඕ": "o:",
    "ඖ": "ou",
    "ක": "k",
    "ඛ": "k",
    "ග": "ɡ",
    "ඝ": "ɡ_",
    "ඞ": "ŋ",
    "ඟ": "ɠ",  # *** n දැමිය යුතු සඤ්ඥක අකුරක්
    "ච": "c",
    "ඡ": "c",
    "ජ": "ɟ",
    "ඣ": "ɟh",
    "ඤ": "ɲ",
    "ඥ": "jɲ",
    "ඦ": "ʄ",  # *** n දැමිය යුතු සඤ්ඥක අකුරක් - ඉඦු ඉඦු one an only word in sinhala that has ඦ
    "ට": "ʈ",
    "ඨ": "ʈ",
    "ඩ": "ɖ",
    "ඪ": "ɖ",
    "න": "n",
    "ණ": "n",
    "ඬ": "ɖ_",  # *** n දැමිය යුතු සඤ්ඥක අකුරක්
    "ත": "t",
    "ථ": "t",
    "ද": "d",
    "ධ": "d_",
    "ඳ": "ɗ",  # *** n දැමිය යුතු සඤ්ඥක අකුරක් - e.g සඳතැන්න
    "ප": "p",
    "ඵ": "p",
    "බ": "b",
    "භ": "b_",
    "ම": "m",
    "ඹ": "ɓ",  # *** m දැමිය යුතු සඤ්ඥක අකුර
    "ය": "j",
    "ර": "r",
    "ල": "l",
    "ව": "w",
    "ශ": "ʃ",
    "ෂ": "ʃ",
    "ස": "s",
    "හ": "h",
    "ළ": "l",
    "ෆ": "f",
    "්": "_",  # **** hal symbol
    "\u200d": "_",  # **** for rakaransaya
    "ා": "a:",
    "ැ": "æ",
    "ෑ": "æ:",
    "ි": "i",
    "ී": "i:",
    "ු": "u",
    "ූ": "u:",
    "ෘ": "ru",
    "ෲ": "ru:",
    "ෙ": "e",
    "ේ": "e:",
    "ෛ": "ai",
    "ො": "o",
    "ෝ": "o:",
    "ෞ": "ou",
    "ෟ": "ou",
}

case2_map = {
    "ɖ_": "nd",  # *** සඤ්ඥක අකුරු, so inseart n prior
    "ɠ": "ng",  # *** සඤ්ඥක අකුරු, so inseart n prior
    "ɗ": "nd",  # *** සඤ්ඥක අකුරු, so inseart n prior
    "ʄ": "nj",  # *** සඤ්ඥක අකුරු, so inseart n prior
    "ɓ": "mb",  # *** සඤ්ඥක අකුරු, so inseart n prior
    "d_": "dh",  # *** mahapprana d_ -> dh
    "b_": "bh",  # *** mahapprana b -> bh
    "ɡ_": "gh",  # *** mahapprana g_ -> gh
    "a": "a",  # vowel
    "a:": "a",  # vowel
    "æ": "e",  # This is special case. although it should be "a", in singlish we use "e" , For example ඇල්ල -> Ella
    "æ:": "e",  # කුරුණෑගල -> kurunEgala
    "i": "i",
    "i:": "ee",  # sometimes "ea"
    "u": "u",
    "u:": "u",  # sometimes "ue"
    "ri": "ri",
    "ru:": "ruu",
    "ilu": "ilu",
    "ilu:": "ilue",
    "e": "e",
    "e:": "e",
    "ai": "ai",
    "o": "o",
    "o:": "o",  # ex: හෝමාගම  -> homagama
    "ɡ": "g",
    "ɟ": "j",
    "ɟh": "jh",
    "ɲ": "kn",
    "jɲ": "gn",
    "d": "d",
    "m": "m",
    "j": "y",
    "r": "r",
    "w": "w",
    "s": "s",
    "l": "l",
    "f": "f",
    "_ ": "_",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "0": "0",
    ".": ".",
    "-": "-",
    "/": "/",
    " ": " ",
    ",": ",",
    "\n": "\n",
    ":": ":",
    ";": "\""
}

case3_map = {
    "ŋ": "n",  # sometimes to "ng"
    "h": "h",
    "k": "k",
    "c": "ch",
    "ʈ": "t",
    "ɖ": "d",
    "n": "n",
    "t": "th",
    "p": "p",
    "b": "b",
    "l": "l",
    "ʃ": "sh",
    "ou": "au",
}


def phoneme_to_english(word):
    def translate(letter):
        if letter in case3_map:
            return case3_map.get(letter)
        return case2_map.get(letter)

    return list(filter(None, map(translate, word)))


def insert_a(sin_text_list, mapped_text_list):
    sin_text_list.append("_")  # Append a dummy non-effecting symbol at the end
    a_inserted_list = []

    for i, letter in enumerate(mapped_text_list):
        a_inserted_list.append(letter)

        if (sin_text_list[i] in pillam) or (sin_text_list[i] in vowels):
            continue
        elif sin_text_list[i + 1] in pillam:
            if sin_text_list[i + 1] == u"ං":  # Handle special cases
                a_inserted_list.append('a')
            continue
        elif letter in special_character_list:
            continue
        else:
            a_inserted_list.append('a')

    return a_inserted_list


def sinhala_to_singlish(input_text):
    sin_text_list = [char for char in input_text if (char not in symbols) and (char not in english_alphabet)]
    sin_text_cleaned = "".join(sin_text_list)

    mapped_text_list = [case1_map.get(letter, letter) for letter in sin_text_cleaned]
    a_inserted_list = insert_a(sin_text_list, mapped_text_list)
    singlish_list = phoneme_to_english(a_inserted_list)

    return "".join(singlish_list)


if __name__ == "__main__":
    sample_text = "ආයුබෝවන්, Sri Lanka"
    transliterated_text = sinhala_to_singlish(sample_text)
    print(transliterated_text)
