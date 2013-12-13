# Exercise 3.3.5:
# Write regular definitions for the following languages:

import re 

# a) All strings of lowercase letters that contain the five vowels in 
# order.

# In other words, any number (including 0) of consonants, then a, 
# then any number of consonants, then e, and so on and so forth...
consonants = 'bcdfghjlkmnpqrstvwxyz'

lowercase_re = re.compile('[{c}]*a[{c}]*e[{c}]*i[{c}]*o[{c}]*u[{c}]'.format(
                            c=consonants))

