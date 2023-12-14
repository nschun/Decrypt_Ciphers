ciphertext = "-... .-. . .- - .... / --- ..-. / - .... . / .-- .. .-.. -.. / .. ... / -... . - - . .-. / - .... .- -." \
             " / - . .- .-. ... / --- ..-. / - .... . / -.- .. -. --. -.. --- -- / ... --- / - .-. -.-- / .- -. -.. " \
             "/ .--. .-. --- ...- . / -- . / .-- .-. --- -. --. .-.-.-"
ciphertext = ciphertext + " "
ciphertext = list(ciphertext)
current_letter = ""
plaintext = ""
morse_key = {
    " ": "/",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    "": ""
}

morse_decode_key = {v: k for k, v in morse_key.items()}

for i in ciphertext:
    if i == " ":
        plaintext = plaintext + morse_decode_key[current_letter]
        current_letter = ""

    else:
        current_letter = current_letter + i

print(plaintext)
