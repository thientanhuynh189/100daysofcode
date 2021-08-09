student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

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