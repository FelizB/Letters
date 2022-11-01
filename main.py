#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
Name =[]
with open("Input/Names/invited_names.txt") as names:
    dear = names.read()
    listed= dear.split("\n")
    for items in listed:
        Name.append(items)
print(Name)
for nam in Name:
    with open(f'Output/ReadyToSend/letter_for_{nam}.txt', mode='w') as letter:
        new_letter= open("Input/Letters/starting_letter.txt")
        read = new_letter.read().replace("[name]", nam)
        letter.write(read)



