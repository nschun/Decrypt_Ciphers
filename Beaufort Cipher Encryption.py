
# Sets up values of letter in Beaufort Cipher.
Letter_Values = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25}
# Put your Plaintext in place of this one.
Plain_Text = "H wtu ljnkqd Njpeotxu Nqeakw vglui Yrfmtb, pbe juar!"
# Put your Key here instead of this one.
Key = "PYTHON"
Key = Key.upper()
Plain_Text = list(Plain_Text)


def Remove_NonAlpha(Plain_Text):
    """Removes non-alphabetic characters. A later version may add non-alphabetic characters into Plaintext, but currently, all characters will be alphabetical (in output, not input)."""
    NonAlpha = list("")
    for Index in range(len(Plain_Text)):
        if Plain_Text[Index].isalpha():
            NonAlpha.append(Plain_Text[Index])
    NonAlpha = "".join(NonAlpha)
    return NonAlpha


count = 0
NonAlpha = Remove_NonAlpha(Plain_Text)
NonAlpha = str(NonAlpha)
NonAlpha = NonAlpha.upper()
NumberForm1 = []
NumberForm2 = []
# Turns Plaintext into corresponding numbers.
for char in NonAlpha:
    NumberForm1.append(Letter_Values[NonAlpha[count]])
    count += 1
count = 0
# Turns Key into corresponding numbers.
for char in Key:
    NumberForm2.append(Letter_Values[Key[count]])
    count += 1
# Defines a reverse dictionary of Letter_Values to provide reverse lookup capabilities.
ReverseLetterValue = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"}
count = 0
FinalNumberForm = 0
FinalPlaintext = []
# Uses reverse lookup dictionary to make the final Ciphertext.
for char in NumberForm1:
    FinalNumberForm = NumberForm1[count] - NumberForm2[count % len(Key)]
    # If it is negative, it adds 26 (alphabet length).
    if FinalNumberForm < 0:
        FinalNumberForm = FinalNumberForm + 26
    print(FinalNumberForm)
    FinalPlaintext.append(ReverseLetterValue[FinalNumberForm])
    count += 1
    FinalNumberForm = 0
FinalPlaintext = "".join(FinalPlaintext)
print(FinalPlaintext)