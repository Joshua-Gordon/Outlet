
import System.IO

main = interact $ map $ toEnum . (`mod` 128) . (+64) . fromEnum

