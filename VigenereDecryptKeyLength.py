# Once you have decided on a text to decipher, copy it into this variable. Longer is more accurate.
Cipher_Text = """WML, HAEXRV SCL ZETTT! OPWCLVR ZTZR. M'E RCEVWCBYC DXDVRY XV GLW NMNV 1883, SCL V LAS BUMK AMGXWG QA LGEMF XZPB VX ODCYH GCM QEQ GMNGZ NWH. (M YDB GLW XLRE XGWZ XZT UBZAT "ZRXMGV OEUZENVVH BB XZT XNWL PONMF 3," LPVGZ XA EIIJQEIV KQRAACO SSJ IQZI SRIQIEN NEIKWURR.) QDC'II HGWOETAG TSL P TBX GU YHIKIQBRK, PVQ EXIME XZT MIIFIA BJ OTQEHEPORHVDV, ZEF, X LBR'L QTNQW NWH! WG WMEI'K LPNX ZPXCIFTL: NJLTZ TPGQVNV, A LIF KWIBVRY P TBX GU NYEC UWE PGHQAK S VTNHAPBBV XXOUX LD BJS UWQYHJTV. RZWC BUSMVP V KGI UL NGQ JNGC (IPNRCH NBV LWIG, FQ IPR ASN!), UL JWATBA GUNVGWGA XIHI KNPDXVT QW WCEXXJT AMUZVNQWH. BVQW QIOC ZXUFIDU KNPDTL ZI FD-NEMWCLVR TAIAHAC! LB CGJ SASO LPNX AI'A YMCT BB PAKM YMCT BUEL? YCFX SH Q JEK IPVRCXVT M ODCYH YXDR EFNBUMFV NBV LXUR FSQG'F VWHXRGL, IPVW OTQEH LGQNRYAM TYQ HPBAWS CC MF BG QVWPUF EFS ANMV IPNX ZT EBYDS UNOW HCEI LXUR FSQG AINTZ OSLWMEIV BM NKSXV. NPD X PNH LD LB ASH AUECT PVW ZPVQ! M'NT VRZWG JRIF VZREL PB ZECXVT HWRQFMGCA HRVTZ CVWHAHVW, PVQ, AWAT, LSM ZVBA LWM EIKI! EUIF X IJSCT, BUEL HBHTAS BEMSCOYI ZPL HWWS UL FGSG GS LGIIID IPESMVP GMET IAH VTAGVGN BUI WCBVVW JVVZWGAR-EFS BVQW QIOC, LDW! YYUZQYC, LXUR FSQG VWF'I LREV . . . TFNGLAG. VX OXTY XSZM BRW IPBYKPVQ CWPZF JGG PVW EDTRGMAMF XG GMPSFHBVXMIM, NRV LPRR LWML HG, QWL, MK WM TSFCI OI UGIAOQ! IPR XABM NKWCBF EDHW FYJKQIIV-IPRC GCTL WWCL GLWXZ USDD-XESBTKGMGCA BYL DV QEFVMESMH UVWKXWAW. TJB YSDEP NRV SCAHYGMA AWGM SYJXWHW SQWHX OWIG M VXL! BJ UDCEWW, IPVW ETIAW LWIG XZTZR MK P LVQWCAVSF-LQQI EPVUYFI WS EYTVGW LGGVRY IW SMFS UR EFS JEMFV UR XG YCFXARM. OYL XB JEK PTY E EXAGECT! BUI DPAG XZXVT M OPVG MK IW TS TPKX XG YIVP, KD Q'II TTMA LASQAK GJB VR LWM CEKI. QG ASH NHR XDZ N AZXTR-WWTQAK LWM FMYWBF, GZPBGMFV EVXZ WQFXGGQPED UQTYJTA, IMKXBVRY IPR '50W LD BEC LD TREJC BUI LLQFX. (A PKPMVTVGEDAG GAAHBRH EN IAODT IAH UDCYHF'I ENPC UWE E OTMX.) M OPVGIV IW PLWRS BYL IPR SDS ERWL, IWB, FMI EUIF X BEENTTRH ZTZR, M SRKVHWCBNPDN ICTWPZRH JXOUX AC NESFI WS E LGIVR SCL ZC LXUR XSEM JEK HPNXLTZRH ACBB JAUBL TATKRW. (SAAB, M LWQAO LWM GVSXV ZMYWB UENT OBRW DNS XZT ZNMDH. PBTWUCYPQ IPNX AHV'G MF IPR LAHBBVQ QWBOK!) PVLASN, Q WYKI ENRLTL GS KPG ASL IW JSJGG NFGJB ZI! A'KM ZEFPORH LD JYIFS QA XG IPR TGECYEUT, IAH A VWG E BDJ NW S EWPOWI ENXUW ZRTSXZZEF. X'DR EDHW PEMVPG SFT WS XZDAR GGDT TSDS ZHWZ-TZN HAHMNWWH BUEL'GM FS HDXHPSG QA XZTAR XABMF, EFS Q NQ DDDVRY IPR RGHBNPYXI! GLSCSF JGG IYP QDCE LWAX, NRV XN NRQ IQZI SVMAXK RWZI DDWXMFV NBV ET, BRPD IPRQ QDC QSF'I SASO CWGLACO! OPWCLVR TAMANSBQA FDPVQMF, 1883"""

def Remove_NonAlpha(Cipher_Text):
    """Removes non-alphabetic characters. """
    NonAlpha = list("")
    for Index in range(len(Cipher_Text)):
        if Cipher_Text[Index].isalpha():
            NonAlpha.append(Cipher_Text[Index])
    NonAlpha = str(NonAlpha)
    return NonAlpha

NonAlpha = Remove_NonAlpha(Cipher_Text)
for Index in range(0, len(Cipher_Text)-2):
    # Each set of three letters - trigaphs - (including overlapping) is recorded. Matching ones are noted especially.
    Trigaph = NonAlpha[Index:(Index + 3)]
    Position = NonAlpha.find(Trigaph, Index+1)
    # The distance between each matching trigaph is recorded. These are printed out in a long list. Key length is the most common divisor of each distance. However, there may be some outliers.
    if not Position == -1:
        print(Position - Index)

# Note: There may be some changes in later versions that find the divisors for you.
