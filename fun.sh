#!/bin/bash
ghc Yes.hs
./Yes.exe < no.txt > temp.txt
chmod a+x temp.txt
./temp.txt

