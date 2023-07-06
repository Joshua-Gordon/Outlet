from enum import Enum
from dataclasses import dataclass
import time

Color = Enum('Color', ['K', 'W', 'R', 'Y', 'G', 'B'])
# Open them to this scope
for col in Color:
    globals()[col.name] = col

RESET = '\x1b[m'
COLORMAP = {
        K: '\x1b[1;35m',
        W: '\x1b[1;37m',
        R: '\x1b[1;31m',
        Y: '\x1b[1;33m',
        G: '\x1b[1;32m',
        B: '\x1b[1;34m',
}

def print_color(s, end='\n'):
    for c in s:
        try:
            m = Color[c]
        except KeyError:
            print(c, end='')
        else:
            print(f'{COLORMAP[m]}{c}{RESET}', end='')
    print(end=end)

class Piece:
    def __init__(self, *seq):
        self.seq = seq
        self.dim = len(seq)
        self.rots = []
        form = list(seq)
        for i in range(len(form)):
            self.rots.append(tuple(form))
            form.append(form.pop(0))

class TriPuzzle:
    IX, IY, IZ = 0, 1, 2

    @dataclass(frozen=True)
    class Placement:
        piece: int
        rot: int

    @dataclass(frozen=True)
    class Locator:
        x: int
        y: int
        down: bool

    class State:
        def __init__(self, puzzle, locs = None, used = None):
            self.puzzle = puzzle
            if locs is None:
                self.locs = {}
                for y in range(puzzle.dim):
                    for x in range(puzzle.dim - y):
                        self.locs[TriPuzzle.Locator(x, y, False)] = None
                        if x != puzzle.dim - y - 1:
                            self.locs[TriPuzzle.Locator(x, y, True)] = None
            else:
                self.locs = locs
            self.used = frozenset() if used is None else used

        def disp_place(self, pl, down):
            if pl is None:
                return '   ', '   '
            r = self.puzzle.pieces[pl.piece].rots[pl.rot]
            x, y, z = [i.name for i in r]
            if down:
                return f' {y} ', f'{x} {z}'
            return f'{y} {z}', f' {x} '

        def disp(self):
            rows = []
            for y in reversed(range(self.puzzle.dim)):
                pad = 3 * y + 2
                row1 = ' ' * (pad - 2) + f'{self.puzzle.legs[TriPuzzle.IY][y].name} '
                row2 = ' ' * pad
                row0 = row2
                for x in range(self.puzzle.dim - y):
                    r1, r2 = self.disp_place(self.locs[TriPuzzle.Locator(x, y, False)], False)
                    row0 += '   '
                    row1 += r1
                    row2 += r2
                    if x != self.puzzle.dim - y - 1:
                        r1, r2 = self.disp_place(self.locs[TriPuzzle.Locator(x, y, True)], True)
                        row0 += r1
                        row1 += r2
                        row2 += '   '
                row0 += '  '
                row1 += f' {self.puzzle.legs[TriPuzzle.IZ][y].name}'
                row2 += '  '
                rows.extend((row0, row1, row2))
            lastrow = '  '
            for col in self.puzzle.legs[TriPuzzle.IX]:
                lastrow += f' {col.name}    '
            rows.append(lastrow)
            return rows

        def print(self):
            print_color('\n'.join(self.disp()))

        def color_at(self, loc, ix):
            pm = self.locs.get(loc)
            if pm is None: return None
            return self.puzzle.pieces[pm.piece].rots[pm.rot][ix]

        def adjacent_col(self, loc):
            if loc.down:
                # Downs can only be inside the puzzle
                a = self.color_at(TriPuzzle.Locator(loc.x, loc.y, False), TriPuzzle.IZ)
                b = self.color_at(TriPuzzle.Locator(loc.x, loc.y+1, False), TriPuzzle.IX)
                c = self.color_at(TriPuzzle.Locator(loc.x+1, loc.y, False), TriPuzzle.IY)
            else:
                if loc.y == 0:
                    a = self.puzzle.legs[TriPuzzle.IX][loc.x]
                else:
                    a = self.color_at(TriPuzzle.Locator(loc.x, loc.y-1, True), TriPuzzle.IY)
                if loc.x == 0:
                    b = self.puzzle.legs[TriPuzzle.IY][loc.y]
                else:
                    b = self.color_at(TriPuzzle.Locator(loc.x-1, loc.y, True), TriPuzzle.IZ)
                if loc.x == self.puzzle.dim - 1:
                    c = self.puzzle.legs[TriPuzzle.IZ][loc.y]
                else:
                    c = self.color_at(TriPuzzle.Locator(loc.x+1, loc.y, True), TriPuzzle.IX)
            return (a, b, c)

        def with_place(self, loc, plc):
            locs = self.locs.copy()
            assert loc in locs
            locs[loc] = plc
            assert plc.piece not in self.used
            return TriPuzzle.State(self.puzzle, locs, self.used | {plc.piece})

        def all_substates(self):
            loc = next(self.open_locs, None)
            if loc is None:
                return
            adj = self.adjacent_col(loc)
            for cand, pls in self.puzzle.adjacencies.items():
                skip = False
                for a, c in zip(adj, cand):
                    if a is not None and a != c:
                        skip = True
                        break
                if skip:
                    continue
                for pl in pls:
                    if pl.piece not in self.used:
                        yield self.with_place(loc, pl)

        def solutions(self, deep=None):
            for st in self.all_substates():
                if st.complete or deep == 0:
                    yield st
                else:
                    nd = (deep - 1) if deep is not None else None
                    yield from st.solutions(nd)

        @property
        def open_locs(self):
            yield from (loc for loc, pl in self.locs.items() if pl is None)

        @property
        def complete(self):
            return next(self.open_locs, None) is None

    def __init__(self, legs, pieces):
        assert len(legs) == 3
        assert all(piece.dim == 3 for piece in pieces)
        self.legs = legs
        self.dim = len(legs[0])
        assert all(len(leg) == self.dim for leg in legs)
        self.pieces = pieces
        self.adjacencies = {}
        for pci, pc in enumerate(pieces):
            for ix, rot in enumerate(pc.rots):
                if rot not in self.adjacencies:
                    self.adjacencies[rot] = set()
                self.adjacencies[rot].add(TriPuzzle.Placement(pci, ix))

    @property
    def initial_state(self):
        return TriPuzzle.State(self)

if __name__ == '__main__':
    p = TriPuzzle([
        (G, G, W, G),
        (Y, W, R, W),
        (K, G, R, B),
    ], [Piece(*s) for s in [
        (G, Y, W),
        (G, K, R),
        (K, G, R),
        (G, R, K),
        (K, W, B),
        (G, Y, R),
        (K, K, G),
        (Y, R, W),
        (G, W, R),
        (W, W, B),
        (W, G, Y),
        (K, Y, G),
        (B, K, W),
        (K, B, Y),
        (Y, G, B),
        (B, B, W),
    ]])
    s = p.initial_state
    s.print()

    start = time.perf_counter()
    sols = list(s.solutions())
    stop = time.perf_counter()

    for st in sols:
        st.print()
    print(f'all {len(sols)} solutions in {stop - start}s')
