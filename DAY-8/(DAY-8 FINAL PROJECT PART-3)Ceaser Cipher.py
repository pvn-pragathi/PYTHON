alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt , type 'decode' to decrypt : \n")
    
text = input("Type your message : \n").lower()

shift = int(input("Type your shift number : \n"))

def ceaser(start_text,shift_amount,direction_text):
    end_text = ""
    if direction_text == "decode" :
            shift_amount *= -1
    for letter in start_text :
        position = alphabet.index(letter)

        edited_position = position + shift_amount

        letter = alphabet[edited_position]
        end_text += letter

    print(f"Your {direction}d word is {end_text}")

ceaser(direction_text=direction,start_text=text,shift_amount=shift)