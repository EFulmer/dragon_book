{- import re
import string

# Exercise 3.3.6:
# Write character classes for the following sets of characters:

# a) The first ten letters (up to "j") in either upper or lower case.
first_10 = re.compile('[Aa][Bb][Cc][Dd][Ee][Ff][Gg][Hh][Ii][Jj]')

# b) The lowercase consonants.
lc_consonants = re.compile('[bcdfghjklmnpqrstvwxyz]') -}

import Text.Regex

first10Chars = mkRegex "[Aa][Bb][Cc][Dd][Ee][Ff][Gg][Hh][Ii]Jj]"

lowerConsonants = mkRegex "[bcdfghjklmnpqrstvwxyz]"
