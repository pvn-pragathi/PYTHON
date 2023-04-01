alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt , type 'decode' to decrypt : \n")
    
text = input("Type your message : \n").lower()

shift = int(input("Type your shift number : \n"))

def encode(plain_text,shift_amount) : 
    ciphered_word = ""
    for letter in plain_text:
        original_position =  alphabet.index(letter)
        ciphered_position = original_position + shift_amount
        ciphered_letter = alphabet[ciphered_position]
        ciphered_word += ciphered_letter
    print(f"Your encoded word is {ciphered_word}")

def decode(ciphered_text,shift_amount) :
    original_word = ""
    for letter in ciphered_text:
        ciphered_position = alphabet.index(letter)
        original_position = ciphered_position - shift_amount
        original_letter = alphabet[original_position]
        original_word  += original_letter
    print(f"Your decoded word is {original_word}")

if direction == "encode" :
    encode(text,shift)

if direction == "decode" :
    decode(text,shift)
