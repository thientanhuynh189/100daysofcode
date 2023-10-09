import pandas
#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary_format = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}  

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# loop = True
# while loop:
#     word_inp = input("Enter a word: ").upper()
#
#     try:
#         list_word = [dictionary_format[word] for word in word_inp]
#         loop = False
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         loop = True
#     else:
#         print(list_word)

def generate_phonetic():
    word_inp = input("Enter a word: ").upper()
    try:
        list_word = [dictionary_format[word] for word in word_inp]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(list_word)

generate_phonetic()
