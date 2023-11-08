MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '.......'}


def encode(msg):
    code = ''
    absent = ''
    for char in msg:
        if char in MORSE_CODE_DICT:
            new_char = MORSE_CODE_DICT[char]
            code += new_char
        else:
            absent += char
    if absent != '':
        print(f"Sorry, this {absent} could not be encoded.")
        return
    print(f"Morse code for your msg: {code}")


continues = True

while continues:
    print("NB: Your message must be in English or numbers.\nAvailable symbols are: ( , . ? / - )\n"
          "An update would be released soon for more symbols and languages.")
    text = input("Type your message: \n").upper()
    if text:
        encode(text)
    question = input("Do you have another message to encode?\nHit any key on your keayboard or 'no' if none.\n").lower()
    if question == "no":
        print("Okay, bye.")
        continues = False
    else:
        continues = True
