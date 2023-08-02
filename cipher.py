abc = "abcdefghijklmnopqrstuvwxyz"

shift = int(input("Please enter the number of places to shift: "))
if not shift:
    print("Invalid input. Please enter a valid number for the shift.")
    exit()


sentence = input("Please enter a sentence: ").lower()

encrypted_sentence =  ""


for char in sentence:
    if  char.isalpha():
         char_index = abc.find(char)
         shift_index = (char_index + shift) % 26
         encrypted_char = abc[shift_index]
         if char.isupper():
             encrypted_char = encrypted_char.upper()
         encrypted_sentence += encrypted_char 
    else:   
        encrypted_sentence += encrypted_char
    


print("Encrypted Sentence:", encrypted_sentence)