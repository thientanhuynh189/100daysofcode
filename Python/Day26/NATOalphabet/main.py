import pandas
#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary_format = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}  

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_inp = input("Enter a word: ").upper()
list_word = [dictionary_format[word] for word in word_inp]
# list_word =[]
# for letter in word_inp:
#   letter_upper = letter.upper()
#   for (item, value) in dictionary_format.items():
#     if letter_upper == item:
#       list_word.append(value)

print(list_word)