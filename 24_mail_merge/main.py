Chnage = "[name]"
with open("./Input/Names/invited_names.txt") as myfile:
    names = myfile.readlines()


with open("./Input/Letters/starting_letter.docx") as letter:
    text = letter.read()
    for name in names:
        stripped_name = name.strip()
        new = text.replace(Chnage,stripped_name)
        print(new)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", 'w') as completed_letter:
            completed_letter.write((new))
