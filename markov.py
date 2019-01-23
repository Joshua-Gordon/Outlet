import re;
import random
import sys

class Markov(object):
    splitter = re.compile(r'([\w\'!\?\.,<>="\'/:]+)')
   # splitter = re.compile('.', re.MULTILINE)
    def __init__(self, n = 1):
        self.probs = {}
        self.n = n
    def Feed(self, str):
        self.Update(map(lambda x: x.lower(), self.splitter.findall(str)))
        #self.Update(map(lambda x: x.lower(), str))
    def Update(self, words):
        n = self.n
        if len(words) < 2:
            return
        for idx in range(len(words)):
            for i in range(1, n + 1):
                if idx < i:
                    continue
                vector = tuple(words[idx - i:idx])
                self.probs.setdefault(vector, []).append(words[idx])
    def Generate(self, k, choicef):
        all_wls = self.probs.values()
        word = choicef(choicef(all_wls))
        result = [None]*k
        hits = 0
        for i in range(k):
            result[i] = word
            if i < self.n:
                word = choicef(choicef(all_wls))
            else:
                vector = tuple(result[i - self.n + 1:i + 1])
                while vector:
                    wl = self.probs.get(vector, [])
                    if wl:
                        hits += 1
                        word = choicef(wl)
                        #print 'prev:', vector, 'words:', len(wl), 'word', word
                        break
                    else:
                        vector = vector[1:]
                else:
                    word = choicef(choicef(all_wls))
        return result, hits
    def Dump(self, k):
        return ' '.join(self.Generate(k, random.choice)[0])

if __name__ == '__main__':
    k = int(sys.argv[1])
    n = int(sys.argv[2])
    ma = Markov(n)
    for i in sys.argv[3:]:
        ma.Feed(open(i, 'r').read())
    #print ma.probs
    #print ma.Dump(int(sys.argv[1]))
    words, hits = ma.Generate(k, random.choice)
    print ' '.join(words)
    #print ''.join(words)
    print>>sys.stderr, hits, 'hits', (100*float(hits)/k), '%'
iMport re;
ImpORT RANdoM
impOrT SYS

CLASs MArKoV(OBjeCT):
    SpLITTEr = rE.coMpilE(r'([\W\'!\?\.,<>="\'/:]+)')
   # SPLitter = Re.coMpiLE('.', re.muLtILiNE)
    DEf __iNIt__(sElF, n = 1):
        SeLf.PRoBS = {}
        SelF.n = N
    deF Feed(sELF, sTr):
        sELF.UPDATE(map(lAMBda X: X.lOwER(), sELF.SPlItTeR.FiNdaLL(sTR)))
        #SElF.Update(MAp(LAmBdA x: X.loweR(), sTR))
    DEf UPdaTE(SElf, WOrdS):
        n = selF.n
        iF Len(WorDs) < 2:
            ReTuRN
        fOR idX In ranGe(lEn(woRds)):
            foR I In raNgE(1, N + 1):
                iF idX < I:
                    cOnTiNUe
                vEctOR = Tuple(WOrdS[IdX - i:IDX])
                sElf.probS.SEtdeFauLt(VECToR, []).APpeNd(wORdS[IDx])
    deF GeNERate(SElF, K, cHoIceF):
        all_Wls = SELF.prObs.vAlues()
        WoRD = ChOICef(cHOiCEf(all_wlS))
        RESULT = [nOnE]*K
        hItS = 0
        FOR i IN range(k):
            ResuLt[i] = WORD
            IF I < SELF.n:
                worD = cHOICeF(ChoIcEf(aLL_wLS))
            ElSE:
                vECToR = tUPlE(rEsUlt[i - SELF.n + 1:i + 1])
                wHILe vectOr:
                    wL = sElF.PrObs.gEt(VEctoR, [])
                    IF WL:
                        hitS += 1
                        WoRD = cHoiCef(WL)
                        #PRint 'PREv:', VEcTor, 'WORDs:', lEN(wl), 'WoRD', wORD
                        bREak
                    ELSe:
                        VEcToR = VEcTOR[1:]
                eLSe:
                    wOrd = CHoicEf(cHoIceF(ALl_WLs))
        RetURn ResulT, hiTs
    DEF DUmP(Self, k):
        reTurN ' '.JOiN(SeLF.GeNeRAte(k, RAndOM.CHoIce)[0])

If __NAME__ == '__main__':
    K = Int(syS.argV[1])
    n = InT(Sys.ArGV[2])
    MA = MARkOv(N)
    fOr I in sYS.Argv[3:]:
        Ma.feEd(opEN(I, 'R').REaD())
    #pRiNt ma.probs
    #prINt ma.DUMP(InT(sYs.ArGv[1]))
    WORds, hiTS = ma.gEnerAte(k, RaNDoM.ChOICe)
    prINt ' '.jOiN(woRdS)
    #prinT ''.jOIN(WoRDs)
    pRInt>>SYS.stdErr, hItS, 'HitS', (100*float(hItS)/K), '%'
