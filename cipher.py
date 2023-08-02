def caesar_cipher_encrypt(text, shift):
    abc = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            encrypted_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            if char.isupper():
                encrypted_char = encrypted_char.upper()
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def main():
    try:
        shift_str = input("Enter the number of characters for the shift: ")
        if not shift_str.isdecimal():
            print("Invalid input. Please enter a valid number for the shift.")
            return

        shift = int(shift_str)
        plain_text = input("Enter the plain text sentence: ").lower()

        encrypted_text = caesar_cipher_encrypt(plain_text, shift)
        print("The encrypted sentence is:", encrypted_text)
    except ValueError:
        print("Invalid input. Please enter a valid number for the shift.")

if __name__ == "__main__":
    main()




