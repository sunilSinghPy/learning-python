text = 'Hellow World!'
custom_key = "python"

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        # Append Space to the message
        if char == ' ':
            final_message += char
        else:
            # Find the right key/char for encode/decode
            key_char = key[key_index % len(key) ]
            key_index +=1
            # Define offset and encryption/decryption letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message

def encrypt(message,key):
    return vigenere(message,key,1)
def decrypt(message,key):
    return vigenere(message,key,-1)

encryption = encrypt(text,custom_key)
decryption = decrypt(text,custom_key)

print(f'\nPlain Text: {text}\nKey: {custom_key}')
print(f'\nEncrypted Text: {encryption}\n')


