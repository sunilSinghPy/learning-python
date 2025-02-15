text = 'Hello World'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
        print('plain Text:',message, 'encrypted text:', encrypted_text)
        print(index,new_index,shift,len(alphabet))

caesar(text, shift)