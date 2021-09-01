import pandas

# This segment downloads the Vigenére table.
vigenere = pandas.read_csv("/Users/Nathan/Desktop/Cipher/Vigenere Cipher Table Python.csv", index_col=0)

    # Most variables.
def Euclidean_Distance(OBSE, OBST, OBSA, OBSO, OBSI, OBSN, OBSS, OBSH, OBSR, OBSD, OBSL, OBSC, OBSU, OBSM, OBSW, OBSF, OBSG, OBSY, OBSP, OBSB, OBSV, OBSK, OBSJ, OBSX, OBSQ, OBSZ):
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

# Does a reverse lookup by finding which CipherText character matches with a plaintext.
def Plaintext_Lookup(Key, Freq):
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
    """This function defines the one fifth slice."""
    Slice = []
    # This loop makes the following repeat as many times as the key's length.
    for I in range(Range, len(Demo_Cipher), Key_Length):
        Slice.append(Demo_Cipher[I].upper())
    return Slice

def Get_Frequency(Count, Slice):
    """This function defines the dictionary Frequency."""
    Frequency = {}
    # This defines the dict. Frequency and creates a group of letters that is one every five in the CipherText.
    Alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for char in Alphabet:
        Frequency[char] = 0
    # This empties the Frequency dictionary entry (char) by entry.
    for char in Slice:
        Frequency[char] += 1
    # This adds 1 to each value of letter when it is detected in the 1/5 of CipherText.
    for char in Alphabet:
        Frequency[char] /= len(Slice)
        # This develops a exact percentage of each letter (of total 1/5 CipherText).
    print(Frequency)
    Values = Frequency.values()
    # This defines var. values based on dict Frequency.
    print(sum(Values))
    # This finds the sum of all values to be used to find percentile.
    return Frequency

def Key_Finder(Demo_Cipher, Key_Length):
    Range = 0
    Count = 0
    FKey = []
    for Loop in range(0, Key_Length):
        Slice = Get_Slice(Range, Demo_Cipher, Key_Length)
        Frequency = Get_Frequency(Count, Slice)
        # This finds the sum of all values to be used to find percentile.
        FrCount = 1
        Loop_Count = 0
        SmLetter = ""
        Alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for char in Alphabet:
            SmFreq = Plaintext_Lookup(char, Frequency)
            print(SmFreq)
            if SmFreq < FrCount:
                FrCount = SmFreq
                SmLetter = char
        FKey.insert(Loop, SmLetter)
        print("FrCount:" + str(FrCount))
        print(f"Key = {FKey}")
        Range += 1
        Slice = []
        # This dumps var. Slice and changes the var. Range so the slice changes to start at the second letter.
    return FKey

def Final_Output(Cipher_Text, FKey):
    """This function deciphers the ciphertext using the key and generates the final plaintext"""
    Cipher_Text = Cipher_Text.upper()
    Cipher_Text = list(Cipher_Text)
    Pos = 0
    FPText = ""
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

Demo_Cipher = ""
Demo_Cipher = list(Demo_Cipher)
Cipher_Text = """WML, HAEXRV SCL ZETTT! OPWCLVR ZTZR. M'E RCEVWCBYC DXDVRY XV GLW NMNV 1883, SCL V LAS BUMK AMGXWG QA LGEMF XZPB VX ODCYH GCM QEQ GMNGZ NWH. (M YDB GLW XLRE XGWZ XZT UBZAT "ZRXMGV OEUZENVVH BB XZT XNWL PONMF 3," LPVGZ XA EIIJQEIV KQRAACO SSJ IQZI SRIQIEN NEIKWURR.) QDC'II HGWOETAG TSL P TBX GU YHIKIQBRK, PVQ EXIME XZT MIIFIA BJ OTQEHEPORHVDV, ZEF, X LBR'L QTNQW NWH! WG WMEI'K LPNX ZPXCIFTL: NJLTZ TPGQVNV, A LIF KWIBVRY P TBX GU NYEC UWE PGHQAK S VTNHAPBBV XXOUX LD BJS UWQYHJTV. RZWC BUSMVP V KGI UL NGQ JNGC (IPNRCH NBV LWIG, FQ IPR ASN!), UL JWATBA GUNVGWGA XIHI KNPDXVT QW WCEXXJT AMUZVNQWH. BVQW QIOC ZXUFIDU KNPDTL ZI FD-NEMWCLVR TAIAHAC! LB CGJ SASO LPNX AI'A YMCT BB PAKM YMCT BUEL? YCFX SH Q JEK IPVRCXVT M ODCYH YXDR EFNBUMFV NBV LXUR FSQG'F VWHXRGL, IPVW OTQEH LGQNRYAM TYQ HPBAWS CC MF BG QVWPUF EFS ANMV IPNX ZT EBYDS UNOW HCEI LXUR FSQG AINTZ OSLWMEIV BM NKSXV. NPD X PNH LD LB ASH AUECT PVW ZPVQ! M'NT VRZWG JRIF VZREL PB ZECXVT HWRQFMGCA HRVTZ CVWHAHVW, PVQ, AWAT, LSM ZVBA LWM EIKI! EUIF X IJSCT, BUEL HBHTAS BEMSCOYI ZPL HWWS UL FGSG GS LGIIID IPESMVP GMET IAH VTAGVGN BUI WCBVVW JVVZWGAR-EFS BVQW QIOC, LDW! YYUZQYC, LXUR FSQG VWF'I LREV . . . TFNGLAG. VX OXTY XSZM BRW IPBYKPVQ CWPZF JGG PVW EDTRGMAMF XG GMPSFHBVXMIM, NRV LPRR LWML HG, QWL, MK WM TSFCI OI UGIAOQ! IPR XABM NKWCBF EDHW FYJKQIIV-IPRC GCTL WWCL GLWXZ USDD-XESBTKGMGCA BYL DV QEFVMESMH UVWKXWAW. TJB YSDEP NRV SCAHYGMA AWGM SYJXWHW SQWHX OWIG M VXL! BJ UDCEWW, IPVW ETIAW LWIG XZTZR MK P LVQWCAVSF-LQQI EPVUYFI WS EYTVGW LGGVRY IW SMFS UR EFS JEMFV UR XG YCFXARM. OYL XB JEK PTY E EXAGECT! BUI DPAG XZXVT M OPVG MK IW TS TPKX XG YIVP, KD Q'II TTMA LASQAK GJB VR LWM CEKI. QG ASH NHR XDZ N AZXTR-WWTQAK LWM FMYWBF, GZPBGMFV EVXZ WQFXGGQPED UQTYJTA, IMKXBVRY IPR '50W LD BEC LD TREJC BUI LLQFX. (A PKPMVTVGEDAG GAAHBRH EN IAODT IAH UDCYHF'I ENPC UWE E OTMX.) M OPVGIV IW PLWRS BYL IPR SDS ERWL, IWB, FMI EUIF X BEENTTRH ZTZR, M SRKVHWCBNPDN ICTWPZRH JXOUX AC NESFI WS E LGIVR SCL ZC LXUR XSEM JEK HPNXLTZRH ACBB JAUBL TATKRW. (SAAB, M LWQAO LWM GVSXV ZMYWB UENT OBRW DNS XZT ZNMDH. PBTWUCYPQ IPNX AHV'G MF IPR LAHBBVQ QWBOK!) PVLASN, Q WYKI ENRLTL GS KPG ASL IW JSJGG NFGJB ZI! A'KM ZEFPORH LD JYIFS QA XG IPR TGECYEUT, IAH A VWG E BDJ NW S EWPOWI ENXUW ZRTSXZZEF. X'DR EDHW PEMVPG SFT WS XZDAR GGDT TSDS ZHWZ-TZN HAHMNWWH BUEL'GM FS HDXHPSG QA XZTAR XABMF, EFS Q NQ DDDVRY IPR RGHBNPYXI! GLSCSF JGG IYP QDCE LWAX, NRV XN NRQ IQZI SVMAXK RWZI DDWXMFV NBV ET, BRPD IPRQ QDC QSF'I SASO CWGLACO! OPWCLVR TAMANSBQA FDPVQMF, 1883"""

# This sets up CipherText to remove spaces and punctuation.
for I in range(len(Cipher_Text)):
    if Cipher_Text[I].isalpha():
        Demo_Cipher.append(Cipher_Text[I])

# Find the key
Key_Length = 5
FKey = (Key_Finder(Demo_Cipher, Key_Length))

StrKey = "".join(FKey)

FPText = Final_Output(Cipher_Text, StrKey)
print(FPText)