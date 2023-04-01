alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceaser(start_text,shift_amount,direction_text):
    end_text = ""

    if direction_text == "decode" :
        shift_amount *= -1
    
    for char in start_text :
        if char in alphabet :
            position = alphabet.index(char)
            edited_position = position + shift_amount
            letter = alphabet[edited_position]
            end_text += letter
        else :
            end_text += char


    print(f"Your {direction}d word is {end_text}")


should_continue = True
while should_continue :
    direction = input("Type 'encode' to encrypt , type 'decode' to decrypt : \n")
    text = input("Type your message : \n").lower()
    shift = int(input("Type your shift number : \n"))
    shift = shift % 26

    ceaser(direction_text=direction,start_text=text,shift_amount=shift)

    result = input("Type 'yes' if you want to go again otherwise 'no'. \n")

    if result == "no" :
        should_continue = False
        print("Goodbye")