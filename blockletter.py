import argparse

parser = argparse.ArgumentParser()
parser.add_argument('text', help='Message to encode')
parser.add_argument('-d', '--dict', dest='dict', default=None, help='Language file to load')
parser.add_argument('-m', '--mark', dest='mark', default='*', help='Mark character/string')
parser.add_argument('-s', '--space', dest='space', default=' ', help='Space character/string')
parser.add_argument('-n', '--newline', dest='newline', default='\n', help='Newline character/string')
parser.add_argument('-g', '--gap', dest='gap', type=int, default=1, help='Inter-character gap')
parser.add_argument('-G', '--space-gap', dest='space_gap', type=int, default=3, help='Gap for spaces')
parser.add_argument('--no-compress', dest='no_compress', action='store_true', help='Don\'t compress common spaces in letters')
parser.add_argument('--debug', dest='debug', action='store_true', help='Print out a bunch of useless debugging information')
args = parser.parse_args()

if args.dict:
    execfile(args.dict)  # Pls set variable "d"
else:
    d = {
        '0': ' **  \n*  * \n*  * \n*  * \n **  ',
        '1': '  *  \n **  \n* *  \n  *  \n*****',
        '2': ' *** \n*   *\n  ** \n *   \n*****',
        '3': '***  \n   * \n***  \n   * \n***  ',
        '4': '  *  \n **  \n* *  \n**** \n  *  ',
        '5': '***  \n*    \n**   \n  *  \n**   ',
        '6': '***  \n*    \n***  \n* *  \n***  ',
        '7': '*****\n   * \n  *  \n *   \n*    ',
        '8': ' *** \n*   *\n *** \n*   *\n *** ',
        '9': '***  \n* *  \n***  \n  *  \n***  ',
        'A': '  *  \n * * \n*****\n*   *\n*   *',
        'B': '***  \n*  * \n***  \n*  * \n***  ',
        'C': '*****\n*    \n*    \n*    \n*****',
        'D': '***  \n*  * \n*   *\n*  * \n***  ',
        'E': '**** \n*    \n***  \n*    \n**** ',
        'F': '**** \n*    \n***  \n*    \n*    ',
        'G': '*****\n*    \n* ***\n*   *\n*****',
        'H': '*   *\n*   *\n*****\n*   *\n*   *',
        'I': '*****\n  *  \n  *  \n  *  \n*****',
        'J': '*****\n  *  \n  *  \n* *  \n *   ',
        'K': '*  * \n* *  \n**   \n* *  \n*  * ',
        'L': '*    \n*    \n*    \n*    \n**** ',
        'M': '*   *\n** **\n* * *\n*   *\n*   *',
        'N': '*   *\n**  *\n* * *\n*  **\n*   *',
        'O': '*****\n*   *\n*   *\n*   *\n*****',
        'P': '**** \n*   *\n**** \n*    \n*    ',
        'Q': '**** \n*  * \n* ** \n**** \n    *',
        'R': '**** \n*   *\n**** \n*  * \n*   *',
        'S': '**** \n*    \n**** \n   * \n**** ',
        'T': '*****\n  *  \n  *  \n  *  \n  *  ',
        'U': '*   *\n*   *\n*   *\n*   *\n*****',
        'V': '*   *\n*   *\n * * \n * * \n  *  ',
        'W': '*   *\n*   *\n* * *\n** **\n*   *',
        'X': '*   *\n * * \n  *  \n * * \n*   *',
        'Y': '*   *\n * * \n  *  \n  *  \n  *  ',
        'Z': '*****\n   * \n  *  \n *   \n*****',
    }

lines = {k: v.split('\n') for k, v in d.items()}
rsz = None
for k, v in lines.items():
    if rsz is None:
        rsz = len(v)
        continue
    if len(v) != rsz:
        print('Warning: inconsistent row size on glyph', k)
    csz = None
    maxlen = None
    for idx, row in enumerate(v):
        if csz is None:
            csz = len(row)
            maxlen = len(row.rstrip())
            continue
        if len(row) != csz:
            print('Warning: inconsistent column size on glyph', k, 'row', idx)
        maxlen = max(maxlen, len(row.rstrip()))
    if not args.no_compress:
        if args.debug:
            print('Sym', k, 'maxlen', maxlen)
        for idx, row in enumerate(v):
            v[idx] = row[:maxlen]


for idx in range(rsz):
    for ch in args.text:
        if ch == ' ':
            print(args.space * args.space_gap, end='')
        else:
            if ch in lines and idx < len(lines[ch]):
                for sym in lines[ch][idx]:
                    if sym == '*':
                        print(args.mark, end='')
                    else:
                        print(args.space, end='')
        print(args.space * args.gap, end='')
    print(args.newline, end='')
Import ArgpARSE

parSER = ARgpaRSe.argUMEntpARseR()
PArsEr.ADD_ARGumEnT('text', hElP='MeSsaGe tO ENcODE')
PArsEr.add_ARgUMENt('-d', '--dICT', desT='DIct', dEFaUlt=NONE, HElp='LaNGUagE fILe To LoAd')
ParSer.aDD_ArGUmenT('-M', '--mArK', DEsT='MArk', DefAulT='*', hELP='MArK CHaRActER/StrIng')
paRSER.Add_ArguMent('-s', '--sPACE', deSt='sPACE', defAUlT=' ', HelP='sPace chaRACTeR/StRiNG')
paRSEr.AdD_ARgUMent('-N', '--NeWlINe', DeSt='neWlIne', deFaUlT='\N', HeLP='NEWliNe charaCTer/StriNG')
parser.ADd_ArGUMeNt('-G', '--gaP', DEsT='GAp', tYpe=InT, DeFAulT=1, hElP='intER-chAraCTer gAP')
Parser.Add_ARgumENT('-g', '--SpACE-GaP', deST='SpaCE_GAp', tyPe=inT, DeFauLt=3, hELP='gaP FOR sPACES')
ParsER.adD_ArGUmeNT('--no-cOMPRESs', DEsT='No_coMPrEss', ACTIOn='stOrE_truE', HELP='Don\'T COmpREss commoN Spaces IN LETtERs')
pArSEr.add_aRgumeNt('--DeBug', DEst='dEBug', ACtIon='STOrE_TRUE', hELP='PrINT OuT a BUnCH OF UsELeSs deBuGgINg InfOrmATIoN')
aRGs = PaRSER.Parse_Args()

If aRgs.diCT:
    EXecfILe(aRGS.dIct)  # Pls set vaRIABLE "d"
eLsE:
    D = {
        '0': ' **  \n*  * \N*  * \N*  * \n **  ',
        '1': '  *  \n **  \N* *  \N  *  \N*****',
        '2': ' *** \n*   *\N  ** \n *   \N*****',
        '3': '***  \N   * \n***  \n   * \n***  ',
        '4': '  *  \n **  \N* *  \n**** \n  *  ',
        '5': '***  \n*    \N**   \n  *  \N**   ',
        '6': '***  \N*    \N***  \n* *  \n***  ',
        '7': '*****\N   * \N  *  \N *   \N*    ',
        '8': ' *** \n*   *\n *** \n*   *\n *** ',
        '9': '***  \n* *  \n***  \N  *  \N***  ',
        'a': '  *  \n * * \n*****\n*   *\N*   *',
        'B': '***  \n*  * \N***  \n*  * \n***  ',
        'c': '*****\N*    \N*    \N*    \N*****',
        'd': '***  \n*  * \N*   *\N*  * \N***  ',
        'E': '**** \N*    \N***  \N*    \n**** ',
        'F': '**** \n*    \n***  \n*    \n*    ',
        'G': '*****\N*    \N* ***\N*   *\n*****',
        'H': '*   *\N*   *\n*****\N*   *\n*   *',
        'I': '*****\N  *  \N  *  \n  *  \n*****',
        'J': '*****\N  *  \N  *  \N* *  \n *   ',
        'k': '*  * \N* *  \n**   \N* *  \n*  * ',
        'L': '*    \n*    \n*    \N*    \n**** ',
        'm': '*   *\n** **\N* * *\N*   *\N*   *',
        'N': '*   *\N**  *\N* * *\N*  **\n*   *',
        'O': '*****\n*   *\N*   *\n*   *\n*****',
        'p': '**** \N*   *\N**** \n*    \N*    ',
        'q': '**** \N*  * \N* ** \N**** \N    *',
        'R': '**** \n*   *\n**** \N*  * \n*   *',
        'S': '**** \n*    \N**** \N   * \N**** ',
        't': '*****\n  *  \n  *  \n  *  \n  *  ',
        'U': '*   *\N*   *\N*   *\N*   *\n*****',
        'V': '*   *\N*   *\n * * \N * * \N  *  ',
        'w': '*   *\N*   *\N* * *\n** **\N*   *',
        'x': '*   *\N * * \N  *  \N * * \n*   *',
        'Y': '*   *\n * * \N  *  \N  *  \N  *  ',
        'Z': '*****\N   * \N  *  \N *   \N*****',
    }

LiNEs = {k: V.SPLIt('\N') FoR K, v IN d.ITeMs()}
rSZ = nONE
FOr K, V iN lineS.iTeMs():
    IF rSz iS NONe:
        rsz = LEn(v)
        CONTINue
    iF lEn(v) != rsz:
        PRINt('WARnINg: inCoNsisTEnt Row size on GLypH', k)
    cSz = NOne
    MAxLeN = nONE
    FoR iDX, Row in EnuMERATe(V):
        If cSz iS NONe:
            csz = LEN(rOW)
            MaXlEN = lEN(roW.RsTRip())
            ConTINUE
        if len(Row) != cSZ:
            pRINT('WaRniNg: iNcOnSisteNT COlUmN sizE On gLYPH', K, 'Row', IDx)
        MaxleN = MaX(maxlen, LEn(ROw.rStrip()))
    If NOt ARgS.NO_cOmPREss:
        iF arGS.debuG:
            prInT('sYM', k, 'mAxLEn', maXlEN)
        foR iDX, RoW In eNumerATe(v):
            v[Idx] = RoW[:maxLen]


For IdX IN raNGE(rsZ):
    FOR Ch in Args.text:
        If Ch == ' ':
            PrINt(aRgs.spAce * aRGS.sPACE_Gap, eND='')
        eLsE:
            IF Ch iN LINeS aND idx < leN(LINes[CH]):
                fOR sym IN LinES[Ch][idx]:
                    if SYm == '*':
                        pRinT(arGs.marK, eND='')
                    ElSe:
                        priNT(ARgs.SPACe, END='')
        PRInt(aRGS.spAcE * aRgs.GAP, end='')
    PrInt(Args.NEwlINE, ENd='')
