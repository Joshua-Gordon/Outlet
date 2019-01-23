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
