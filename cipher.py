sentence = input("Please enter a sentence: ")
sentence = sentence.lower()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet2 = alphabet * 2
cipher = []

shift = 5
letter = 0

while letter < 26:
    replacement = alphabet2[letter + shift]
    cipher.append(replacement)
    letter += 1

new_sent = []

for char in sentence:
    if char in alphabet2:
        indexof = alphabet2.index(char)
        var = cipher[indexof]
        new_sent.append(var)
    else:
        new_sent.append(char)

translated_sent = "".join(new_sent)
print(f"The encrypted sentence is: {translated_sent}")
   
