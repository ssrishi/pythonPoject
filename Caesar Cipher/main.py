from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

start = True
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26
def caesarCipher(startText, shiftAmount, cipherDirection):
    endText = ""
    if cipherDirection == "decode":
        shiftAmount *= -1
    for letter in startText:
        if letter in alphabet:
            index = alphabet.index(letter)
            endText += alphabet[index+shiftAmount]
        else:
            endText += letter

    print(f"Here the {cipherDirection} result: {endText}") 
