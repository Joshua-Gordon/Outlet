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
