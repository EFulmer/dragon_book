import Data.List
import Text.Regex

-- first, a string that matches any number of lower case consonants:
consonants = "[bcdfghjlkmnpqrstvwxyz]*"
vowels = ["a+", "e+", "i+", "o+", "u+"]

vowelsRegex = mkRegex $ intercalate consonants vowels

-- 3.3.5 b)
lexOrderStr = [ a:"*" | a <- ['a'..'z'] ]
lexOrderRegex = (mkRegex . concat) lexOrderStr
