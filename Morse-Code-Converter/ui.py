from tkinter import *


window = Tk()
window.title("Morse Code Converter")
window.config(padx=50, pady=50, bg="grey")
window.geometry("1000x500")


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
    for char in msg:
        if char.upper() in MORSE_CODE_DICT:
            new_char = MORSE_CODE_DICT[char.upper()]
            code += new_char + ' '  # Add a space between Morse code characters
        else:
            code += ' '  # Use a space for characters not in the dictionary

    return code

def code():
    userInput = text.get("1.0", END).strip()
    morse_code = encode(userInput)
    if morse_code is not None:
        my_label2.config(text=morse_code)

my_label = Label(text="Morse Code Converter", font=("Arial", 30, "bold"), width=20, background='#B97A57', borderwidth=1, highlightbackground="black", relief="solid")
my_label.grid(column=0, row=0, columnspan=2, sticky=(W, E))

#Text
text = Text(height=10, width=30, borderwidth=1, highlightbackground="black", relief="solid")
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Hello World.")
#Get's current value in textbox at line 1, character 0
text.grid(column=0, row=1, pady=20, padx=20, sticky=(W, E))

my_label2 = Label(text="Morse Code Converter", font=("Arial", 30, "bold"), height=8, width=25, wraplength=570, justify="left", borderwidth=1, highlightbackground="black", relief="solid")
my_label2.grid(column=1, row=1, rowspan=2, pady=5)

button = Button(text="Encode", font=("Arial", 15, "bold"), width=10, command=code, background='#00A2E8', borderwidth=1, highlightbackground="black", relief="solid")
button.grid(column=0, row=2)




window.mainloop()
