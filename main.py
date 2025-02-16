def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Exiting.")
        return

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == '1':
        encrypted_message = caesar_cipher(message, shift, 'encrypt')
        print(f"Encrypted message: {encrypted_message}")
    else:
        decrypted_message = caesar_cipher(message, shift, 'decrypt')
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
