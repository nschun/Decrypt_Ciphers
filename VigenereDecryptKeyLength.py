
Cipher_Text = "WmlHaexrvsclZetttOpwclvrztzrMercevwcbycdxdvryxvglwnmnv1883sclVlasbumkamgxwgqalgemfxzpbvxodcyhgcmqeqgmngznwhMydbglwxlrexgwzxztubzatZrxmgvOeuzenvvhbbxztxnwlPonmf3lpvgzxaeiijqeivkqraacossjIqzisriqienneikwurrQdciihgwoetagtslptbxguyhikiqbrkpvqeximexztmiifiabjOtqeheporhvdvzefxlbrlqtnqwnwhWgwmeiklpnxzpxciftlNjltzTpgqvnvAlifkwibvrypTBXgunyecuwepghqaksvtnhapbbvxxouxldbjsuwqyhjtvRzwcbusmvpVkgiulngqjngcipnrchnbvlwigfqiprasnuljwatbagunvgwgaxihiknpdxvtqwwcexxjtamuzvnqwhBvqwQioczxufiduknpdtlziFdNemwclvrTaiahacLbcgjsasolpnxaiaymctbbpakmymctbuel"
Cipher_Text = Cipher_Text.replace("3", "")
Cipher_Text = Cipher_Text.replace("188", "")
# CipherText is defined and is separated from non alphabetic characters.
for I in range(0, len(Cipher_Text)-2):
    Trigaph = Cipher_Text[I:(I + 3)]
    Pos = Cipher_Text.find(Trigaph, I+1)
    # Each set of three letters - trigaphs - (including overlapping) is recorded. Matching ones are noted especially.
    if not Pos == -1:
        print(Pos - I)
        # The distance between each matching trigaph is recorded. These are printed out in a long list. Key length is then deduced from common divisors of each distance.
