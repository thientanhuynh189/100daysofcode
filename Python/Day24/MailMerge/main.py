PLACEHOLDER = "[name]"

# TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as file_letter:
    letter = file_letter.read()

    # for each name in invited_names.txt
    with open("./Input/Names/invited_names.txt") as file_names:
        names = file_names.readlines()
        for name in names:
            strip_name = name.strip()

            #Replace the [name] placeholder with the actual name.
            letter.replace(PLACEHOLDER, strip_name)

            #Save the letters in the folder "ReadyToSend"
            with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt", mode="w") as ready_letter:
                ready_letter.write(letter)