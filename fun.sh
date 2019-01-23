#!/bin/bash
ghc Yes.hs
./Yes < no.txt > temp.txt
chmod a+x temp.txt
./temp.txt

