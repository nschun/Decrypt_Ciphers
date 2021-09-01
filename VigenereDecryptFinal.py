# Imports module of pandas, which reads the Vigenere table file.
import pandas

# This segment downloads the Vigenére table. Add your own path that reaches it in your device. Table is available at https://github.com/nschun/Decrypt_Ciphers/commit/a0caf2bda8a00051429ea885e2544f94db8a44e8
vigenere = pandas.read_csv("/Users/Nathan/Desktop/Cipher/Vigenere Cipher Table Python.csv", index_col=0)


def Euclidean_Distance(OBSE, OBST, OBSA, OBSO, OBSI, OBSN, OBSS, OBSH, OBSR, OBSD, OBSL, OBSC, OBSU, OBSM, OBSW, OBSF, OBSG, OBSY, OBSP, OBSB, OBSV, OBSK, OBSJ, OBSX, OBSQ, OBSZ):
    """Finds the Euclidean Distance of the expected value and the observed value by subtracting one from the other and then squaring."""
    EXPE = 0.127
    EXPT = 0.09
    EXPA = 0.082
    EXPO = 0.075
    EXPI = 0.07
    EXPN = 0.068
    EXPS = 0.063
    EXPH = 0.061
    EXPR = 0.06
    EXPD = 0.0425
    EXPL = 0.04
    EXPC = 0.0285
    EXPU = 0.028
    EXPM = 0.0245
    EXPW = 0.024
    EXPF = 0.0235
    EXPG = 0.02
    EXPY = 0.02
    EXPP = 0.0195
    EXPB = 0.01455
    EXPV = 0.01
    EXPK = 0.018
    EXPJ = 0.002
    EXPX = 0.002
    EXPQ = 0.001
    EXPZ = 0.0005
    return (OBSE - EXPE)**2 + (OBST - EXPT)**2 + (OBSA - EXPA)**2 + (OBSO - EXPO)**2 + (OBSI - EXPI)**2 + (OBSN - EXPN)**2 + (OBSS - EXPS)**2 + (OBSH - EXPH)**2 + (OBSR - EXPR)**2 + (OBSD - EXPD)**2 + (OBSL - EXPL)**2 + (OBSC - EXPC)**2 + (OBSU - EXPU)**2 + (OBSM - EXPM)**2 + (OBSW - EXPW)**2 + (OBSF - EXPF)**2 + (OBSG - EXPG)**2 + (OBSY - EXPY)**2 + (OBSP - EXPP)**2 + (OBSB - EXPB)**2 + (OBSV - EXPV)**2 + (OBSK - EXPK)**2 + (OBSJ - EXPJ)**2 + (OBSX - EXPX)**2 + (OBSQ - EXPQ)**2 + (OBSZ - EXPZ)**2


def Plaintext_Lookup(Key, Freq):
    """Does a reverse lookup on the Vigenere table by finding which CipherText character matches with a plaintext. It finds the smallest float percentage found for each of the 26 floats. That is most likely to be the letter of the key."""
    OBSE = Freq[vigenere[Key]["E"]]
    OBST = Freq[vigenere[Key]["T"]]
    OBSA = Freq[vigenere[Key]["A"]]
    OBSO = Freq[vigenere[Key]["O"]]
    OBSI = Freq[vigenere[Key]["I"]]
    OBSN = Freq[vigenere[Key]["N"]]
    OBSS = Freq[vigenere[Key]["S"]]
    OBSH = Freq[vigenere[Key]["H"]]
    OBSR = Freq[vigenere[Key]["R"]]
    OBSD = Freq[vigenere[Key]["D"]]
    OBSL = Freq[vigenere[Key]["L"]]
    OBSC = Freq[vigenere[Key]["C"]]
    OBSU = Freq[vigenere[Key]["U"]]
    OBSM = Freq[vigenere[Key]["M"]]
    OBSW = Freq[vigenere[Key]["W"]]
    OBSF = Freq[vigenere[Key]["F"]]
    OBSG = Freq[vigenere[Key]["G"]]
    OBSY = Freq[vigenere[Key]["Y"]]
    OBSP = Freq[vigenere[Key]["P"]]
    OBSB = Freq[vigenere[Key]["B"]]
    OBSV = Freq[vigenere[Key]["V"]]
    OBSK = Freq[vigenere[Key]["K"]]
    OBSJ = Freq[vigenere[Key]["J"]]
    OBSX = Freq[vigenere[Key]["X"]]
    OBSQ = Freq[vigenere[Key]["Q"]]
    OBSZ = Freq[vigenere[Key]["Z"]]
    return Euclidean_Distance(OBSE, OBST, OBSA, OBSO, OBSI, OBSN, OBSS, OBSH, OBSR, OBSD, OBSL, OBSC, OBSU, OBSM, OBSW, OBSF, OBSG, OBSY, OBSP, OBSB, OBSV, OBSK, OBSJ, OBSX, OBSQ, OBSZ)


def Get_Slice(Range, Demo_Cipher, Key_Length):
    """This function defines the one fifth slice of the Cipher Text."""
    Slice = []
    # This loop makes the following repeat as many times as the key's length.
    for Index in range(Range, len(Demo_Cipher), Key_Length):
        Slice.append(Demo_Cipher[Index].upper())
    return Slice


def Get_Frequency(Slice):
    """This function defines the dictionary Frequency."""
    # This defines the dict. Frequency and creates a group of letters that is one every five in the CipherText.
    Frequency = {}
    # This empties the Frequency dictionary entry (char) by entry.
    Alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for char in Alphabet:
        Frequency[char] = 0
    # This adds 1 to each value of letter when it is detected in the 1/5 of CipherText.
    for char in Slice:
        Frequency[char] += 1
    # This develops a exact percentage of each letter (of total 1/5 CipherText).
    for char in Alphabet:
        Frequency[char] /= len(Slice)
    print(Frequency)
    # This defines var. values based on dict Frequency.
    Values = Frequency.values()
    # This finds the sum of all values to be used to find percentile.
    print(sum(Values))
    return Frequency


def Key_Finder(Demo_Cipher, Key_Length):
    """Find the key."""
    Range = 0
    FKey = []
    # This finds the sum of all values to be used to find percentile.
    for Loop in range(0, Key_Length):
        Slice = Get_Slice(Range, Demo_Cipher, Key_Length)
        Frequency = Get_Frequency(Slice)
        FrCount = 1
        SmLetter = ""
        Alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        # Calls Plaintext_Lookup function and gets the smallest frequency produced from each Slice.
        for char in Alphabet:
            SmFreq = Plaintext_Lookup(char, Frequency)
            print(SmFreq)
            if SmFreq < FrCount:
                FrCount = SmFreq
                SmLetter = char
        FKey.insert(Loop, SmLetter)
        print("FrCount:" + str(FrCount))
        print(f"Key = {FKey}")
        # This dumps var. Slice and changes the var. Range so the slice changes to start at the second letter.
        Range += 1
        Slice = []
    return FKey


def Final_Output(Cipher_Text, FKey):
    """This function deciphers the ciphertext using the key and generates the final plaintext"""
    Cipher_Text = Cipher_Text.upper()
    Cipher_Text = list(Cipher_Text)
    Pos = 0
    FPText = ""
    # This separates the alphabetic and non-alphabetic into two groups and looks it up against the key to generate the plaintext. They are then joined back together in order.
    for Index in range(len(Cipher_Text)):
        if not Cipher_Text[Index].isalpha():
            FPText = FPText + (Cipher_Text[Index])
        else:
            Key_Index = Pos % len(FKey)
            print(f"{Pos} {Key_Index} {FKey[Key_Index]}")
            PText = list(vigenere[FKey[Key_Index]]).index(Cipher_Text[Index])
            FPText = FPText + (vigenere["A"][PText])
            Pos += 1
    return FPText


def Remove_NonAlpha(Cipher_Text):
    """This sets up Cipher_Text to remove spaces and punctuation."""
    Demo_Cipher = ""
    Demo_Cipher = list(Demo_Cipher)
    for Index in range(len(Cipher_Text)):
        if Cipher_Text[Index].isalpha():
            Demo_Cipher.append(Cipher_Text[Index])
    return Demo_Cipher


# Insert your Cipher Text here WITH all spaces, punctuation, and numbers.
Cipher_Text = """WML, HAEXRV SCL ZETTT! OPWCLVR ZTZR. M'E RCEVWCBYC DXDVRY XV GLW NMNV 1883, SCL V LAS BUMK AMGXWG QA LGEMF XZPB VX ODCYH GCM QEQ GMNGZ NWH. (M YDB GLW XLRE XGWZ XZT UBZAT "ZRXMGV OEUZENVVH BB XZT XNWL PONMF 3," LPVGZ XA EIIJQEIV KQRAACO SSJ IQZI SRIQIEN NEIKWURR.) QDC'II HGWOETAG TSL P TBX GU YHIKIQBRK, PVQ EXIME XZT MIIFIA BJ OTQEHEPORHVDV, ZEF, X LBR'L QTNQW NWH! WG WMEI'K LPNX ZPXCIFTL: NJLTZ TPGQVNV, A LIF KWIBVRY P TBX GU NYEC UWE PGHQAK S VTNHAPBBV XXOUX LD BJS UWQYHJTV. RZWC BUSMVP V KGI UL NGQ JNGC (IPNRCH NBV LWIG, FQ IPR ASN!), UL JWATBA GUNVGWGA XIHI KNPDXVT QW WCEXXJT AMUZVNQWH. BVQW QIOC ZXUFIDU KNPDTL ZI FD-NEMWCLVR TAIAHAC! LB CGJ SASO LPNX AI'A YMCT BB PAKM YMCT BUEL? YCFX SH Q JEK IPVRCXVT M ODCYH YXDR EFNBUMFV NBV LXUR FSQG'F VWHXRGL, IPVW OTQEH LGQNRYAM TYQ HPBAWS CC MF BG QVWPUF EFS ANMV IPNX ZT EBYDS UNOW HCEI LXUR FSQG AINTZ OSLWMEIV BM NKSXV. NPD X PNH LD LB ASH AUECT PVW ZPVQ! M'NT VRZWG JRIF VZREL PB ZECXVT HWRQFMGCA HRVTZ CVWHAHVW, PVQ, AWAT, LSM ZVBA LWM EIKI! EUIF X IJSCT, BUEL HBHTAS BEMSCOYI ZPL HWWS UL FGSG GS LGIIID IPESMVP GMET IAH VTAGVGN BUI WCBVVW JVVZWGAR-EFS BVQW QIOC, LDW! YYUZQYC, LXUR FSQG VWF'I LREV . . . TFNGLAG. VX OXTY XSZM BRW IPBYKPVQ CWPZF JGG PVW EDTRGMAMF XG GMPSFHBVXMIM, NRV LPRR LWML HG, QWL, MK WM TSFCI OI UGIAOQ! IPR XABM NKWCBF EDHW FYJKQIIV-IPRC GCTL WWCL GLWXZ USDD-XESBTKGMGCA BYL DV QEFVMESMH UVWKXWAW. TJB YSDEP NRV SCAHYGMA AWGM SYJXWHW SQWHX OWIG M VXL! BJ UDCEWW, IPVW ETIAW LWIG XZTZR MK P LVQWCAVSF-LQQI EPVUYFI WS EYTVGW LGGVRY IW SMFS UR EFS JEMFV UR XG YCFXARM. OYL XB JEK PTY E EXAGECT! BUI DPAG XZXVT M OPVG MK IW TS TPKX XG YIVP, KD Q'II TTMA LASQAK GJB VR LWM CEKI. QG ASH NHR XDZ N AZXTR-WWTQAK LWM FMYWBF, GZPBGMFV EVXZ WQFXGGQPED UQTYJTA, IMKXBVRY IPR '50W LD BEC LD TREJC BUI LLQFX. (A PKPMVTVGEDAG GAAHBRH EN IAODT IAH UDCYHF'I ENPC UWE E OTMX.) M OPVGIV IW PLWRS BYL IPR SDS ERWL, IWB, FMI EUIF X BEENTTRH ZTZR, M SRKVHWCBNPDN ICTWPZRH JXOUX AC NESFI WS E LGIVR SCL ZC LXUR XSEM JEK HPNXLTZRH ACBB JAUBL TATKRW. (SAAB, M LWQAO LWM GVSXV ZMYWB UENT OBRW DNS XZT ZNMDH. PBTWUCYPQ IPNX AHV'G MF IPR LAHBBVQ QWBOK!) PVLASN, Q WYKI ENRLTL GS KPG ASL IW JSJGG NFGJB ZI! A'KM ZEFPORH LD JYIFS QA XG IPR TGECYEUT, IAH A VWG E BDJ NW S EWPOWI ENXUW ZRTSXZZEF. X'DR EDHW PEMVPG SFT WS XZDAR GGDT TSDS ZHWZ-TZN HAHMNWWH BUEL'GM FS HDXHPSG QA XZTAR XABMF, EFS Q NQ DDDVRY IPR RGHBNPYXI! GLSCSF JGG IYP QDCE LWAX, NRV XN NRQ IQZI SVMAXK RWZI DDWXMFV NBV ET, BRPD IPRQ QDC QSF'I SASO CWGLACO! OPWCLVR TAMANSBQA FDPVQMF, 1883"""
# Insert Key_Length in place of this 5 deduced from last program.
Key_Length = 5
# Removes non-alphabetic characters.
Demo_Cipher = Remove_NonAlpha(Cipher_Text)
# Finds the key.
FKey = (Key_Finder(Demo_Cipher, Key_Length))

StrKey = "".join(FKey)

FPText = Final_Output(Cipher_Text, StrKey)
# Prints the final output in all caps. Further puntuational adaptivity may be implemented later.
print(FPText)
