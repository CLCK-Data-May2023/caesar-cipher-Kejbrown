def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    try:
        shift_str = input("Enter the number of characters for the shift: ")
        if not shift_str.isdecimal():
            print("Invalid input. Please enter a valid number for the shift.")
            return

        shift = int(shift_str)
        plain_text = input("Enter the plain text sentence: ")

        encrypted_text = caesar_cipher_encrypt(plain_text, shift)
        print("The encrypted sentence is:", encrypted_text)
    except ValueError:
        print("Invalid input. Please enter a valid number for the shift.")

if __name__ == "__main__":
    main()




