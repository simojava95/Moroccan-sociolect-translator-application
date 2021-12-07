import json
import eel
from googletrans import Translator

# importer le fichier data.json du dictionnaire darija

with open('darija/data.json', encoding='utf-8') as f:
    dictionnaire = json.load(f)

# eel calling
eel.init('Front-end')

# dictionnaire sociolecte marocaine

data = {
    "a": "ا",
    "A": "ة",
    "b": "ب",
    "t": "ت",
    "ť": "ث",
    "j": "ج",
    "7": "ح",
    "kh": "خ",
    "d": "د",
    "r": "ر",
    "z": "ز",
    "s": "س",
    "ch": "ش",
    "S": "ص",
    "D": "ض",
    "T": "ط",
    "3": "ع",
    "gh": "غ",
    "f": "ف",
    "9": "ق",
    "k": "ك",
    "l": "ل",
    "m": "م",
    "n": "ن",
    "h": "ه",
    "o": "و",
    "w": "و",
    "y": "ي",
    "i": "ي",
    "2": "ء",
    "g": "ك",
    "v": "ف",
}


# Subdiviser le texte en mots

def split_sentence_to_words(sentence):
    words = sentence.split()
    return words


# cette fonction cherche la definition du mot entré en parametre dans le fichier data.json
# est retourne sa definition si il exist sinon il retourné 'not found'

def search_in_dictionnary(word):
    text = 'not found'
    for n in dictionnaire:
        if n == word:
            text = dictionnaire[n]
    return text


# cette fonction trouver l’équivalent de chaque lettre en arabe

def sociolecte_to_arabic_darija(list_of_words):
    arabic_darija = list()
    for i in range(0, len(list_of_words)):
        j = 0
        letter = ''
        equivalent_word = ''
        while j < len(list_of_words[i]):
            letter += list_of_words[i][j]
            if letter in data:
                equivalent_word += data.get(letter)
                letter = ''
                j += 1
            else:
                j += 1
        arabic_darija.append(equivalent_word)
    return arabic_darija


# Google trans
def google_translate(word, input_language, output_language):
    trans = Translator()
    translate_text = trans.translate(word, src=input_language, dest=output_language)
    return translate_text.text


# cette fonction chercher en premier fois la definition du mot dans le fichier data.json
# puis si la definition n'existe pas on le traduire directement par google traduction

def arabic_darija_translate(text, lang):
    translated_words_list = list()
    arabic_darija_sentence = sociolecte_to_arabic_darija(split_sentence_to_words(text))

    for i in range(len(arabic_darija_sentence)):
        word = search_in_dictionnary(arabic_darija_sentence[i])
        if word == 'not found':
            mots = google_translate(arabic_darija_sentence[i], 'ar', lang)
            translated_words_list.append(mots)
        else:
            if lang == 'en':
                translated_words_list.append(word)
            else:
                word_final = google_translate(word, 'en', lang)
                translated_words_list.append(word_final)

    translated_sentence = ' '.join(str(e) for e in translated_words_list)
    return translated_sentence


@eel.expose
def start(text, lang):
    output = arabic_darija_translate(text, lang)
    eel.set_output(output)


eel.start('main.html', size=(980, 778))
