import re, requests
from bs4 import BeautifulSoup
from wiktionaryparser import WiktionaryParser
import json


# dictionnaire darija-englais , il prend on parametre le mot en arabic darija
# est retourne la definition en englais.

def wikitionary(word):
    parser = WiktionaryParser()
    parser.set_default_language('Moroccan Arabic')
    str1 = parser.fetch(word)
    str2 = str1[0].get('definitions')[0]['text'][1]
    str3 = re.sub(r"\([^()]*\)", "", str2)
    synonyme_en_anglais = re.split('; |, |\?', str3)[0]
    return synonyme_en_anglais


# extraire les mots darija du site wikitionary ,et les retourne sous forme d'une liste
def get_data_by_class(url, element, class_name, target):
    liste_of_arabic_words = list()
    response = requests.get(url)
    page = response.content
    soup = BeautifulSoup(page, 'html.parser')
    look = soup.find(element, class_=class_name)
    data = look.find_all(target)
    for n in data:
        liste_of_arabic_words.append(n.get_text())
    return liste_of_arabic_words


# cette methode retourne un dictionaire contient les mots en darija et leur traduction en englais

def moroccan_dictionary(url):
    dictionary = {}
    darija_vocabulary = get_data_by_class(url, 'div', 'mw-category', 'a')
    print('Extracting data in progress...')

    for n in darija_vocabulary:
        try:
            dictionary[n] = wikitionary(n)
        except IndexError:
            continue
    print('process completed')
    return dictionary


# enregistrer le dictionnaire marociane dans un fichier format JSON
def export_as_json(url, output_file_name):
    data = moroccan_dictionary(url)
    with open(output_file_name + '.json', 'w', encoding='utf-8', ) as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# exemple de test
'''export_as_json('https://bit.ly/3eMoZom','test')'''