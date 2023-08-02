def caesar_cipher_encrypt(text, shift):
    abc = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  # Only encrypt alphabetic characters
            char_lower = char.lower()
            char_index = abc.find(char_lower)
            shifted_index = (char_index + shift) % 26
            encrypted_char = abc[shifted_index]
            
            if char.isupper():
                encrypted_char = encrypted_char.upper()  # Convert back to uppercase if the original character was uppercase
        else:
            encrypted_char = char  # Keep non-alphabetic characters unchanged
        
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
        print("Encrypted text:", encrypted_text)
    except ValueError:
        print("Invalid input. Please enter a valid number for the shift.")

if __name__ == "__main__":
    main()