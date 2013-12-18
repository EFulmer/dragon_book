# Exercise 3.3.5:
# Write regular definitions for the following languages:

import re 
import string

# a) All strings of lowercase letters that contain the five vowels in 
# order.

# In other words, any number (including 0) of consonants, then a, 
# then any number of consonants, then e, and so on and so forth...
consonants = 'bcdfghjlkmnpqrstvwxyz'

lowercase_re = re.compile('[{c}]*a+[{c}]*e+[{c}]*i+[{c}]*o+[{c}]*u+[{c}]'.format(
                            c=consonants))

# b) All strings of lowercase letters in which the letters are in 
# ascending lexicographic order.

# In other words: any number of as, followed by any number of bs, 
# so on and so forth, until we reach z.
# More formally, the regular def. for this language would be 
# something like:
# a_def -> 'a*'
# b_def -> a_def|'b*'
# c_def -> b|c*
# etc.
# Sigma is {}.
lex_asc_re = re.compile('a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*')
