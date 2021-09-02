
# Sets up values of letter in Beaufort Cipher.
Letter_Values = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25}
# Put your Ciphertext in place of this one.
Cipher_Text = "H wtu ljnkqd Njpeotxu Nqeakw vglui Yrfmtb, pbe juar!"
# Put your Key here instead of this one.
Key = "PYTHON"
Key = Key.upper()
Cipher_Text = list(Cipher_Text)


def Remove_NonAlpha(Cipher_Text):
    """Removes non-alphabetic characters. A later version may add non-alphabetic characters into Plaintext, but currently, all characters will be alphabetical (in output, not input)."""
    NonAlpha = list("")
    for Index in range(len(Cipher_Text)):
        if Cipher_Text[Index].isalpha():
            NonAlpha.append(Cipher_Text[Index])
    NonAlpha = "".join(NonAlpha)
    return NonAlpha


count = 0
NonAlpha = Remove_NonAlpha(Cipher_Text)
NonAlpha = str(NonAlpha)
NonAlpha = NonAlpha.upper()
NumberForm1 = []
NumberForm2 = []
for char in NonAlpha:
    NumberForm1.append(Letter_Values[NonAlpha[count]])
    count += 1
print(NumberForm1)
count = 0
for char in Key:
    NumberForm2.append(Letter_Values[Key[count]])
    count += 1
print(NumberForm2)
ReverseLetterValue = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"}
count = 0
FinalNumberForm = 0
FinalPlaintext = []
for char in NumberForm1:
    FinalNumberForm = NumberForm1[count] - NumberForm2[count % len(Key)]
    if FinalNumberForm < 0:
        FinalNumberForm = FinalNumberForm + 26
    print(FinalNumberForm)
    FinalPlaintext.append(ReverseLetterValue[FinalNumberForm])
    count += 1
    FinalNumberForm = 0
FinalPlaintext = "".join(FinalPlaintext)
print(FinalPlaintext)