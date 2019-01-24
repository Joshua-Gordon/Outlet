
import System.IO

main = interact $ map $ toEnum . (`mod` 128) . (+64) . fromEnum


IMport sYstEM.io

MaIN = iNTERACT $ MaP $ tOeNum . (`mOD` 128) . (+64) . FromeNuM

