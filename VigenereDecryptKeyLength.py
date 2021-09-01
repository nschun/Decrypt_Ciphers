# Once you have decided on a text to decipher, copy it into this variable after removing non-alphabetic characters. Longer is better. Compatibility to non-alphabetic characters will be added in another version.
Cipher_Text = "WmlHaexrvsclZetttOpwclvrztzrMercevwcbycdxdvryxvglwnmnv1883sclVlasbumkamgxwgqalgemfxzpbvxodcyhgcmqeqgmngznwhMydbglwxlrexgwzxztubzatZrxmgvOeuzenvvhbbxztxnwlPonmf3lpvgzxaeiijqeivkqraacossjIqzisriqienneikwurrQdciihgwoetagtslptbxguyhikiqbrkpvqeximexztmiifiabjOtqeheporhvdvzefxlbrlqtnqwnwhWgwmeiklpnxzpxciftlNjltzTpgqvnvAlifkwibvrypTBXgunyecuwepghqaksvtnhapbbvxxouxldbjsuwqyhjtvRzwcbusmvpVkgiulngqjngcipnrchnbvlwigfqiprasnuljwatbagunvgwgaxihiknpdxvtqwwcexxjtamuzvnqwhBvqwQioczxufiduknpdtlziFdNemwclvrTaiahacLbcgjsasolpnxaiaymctbbpakmymctbuel"
# CipherText is defined and is separated from specific number 1883.
Cipher_Text = Cipher_Text.replace("1883", "")
for Index in range(0, len(Cipher_Text)-2):
    # Each set of three letters - trigaphs - (including overlapping) is recorded. Matching ones are noted especially.
    Trigaph = Cipher_Text[Index:(Index + 3)]
    Pos = Cipher_Text.find(Trigaph, Index+1)
    # The distance between each matching trigaph is recorded. These are printed out in a long list. Key length is the most common divisor of each distance. However, there may be some outliers.
    if not Pos == -1:
        print(Pos - Index)

# Note: There may be some changes in later versions that find the divisors for you.
