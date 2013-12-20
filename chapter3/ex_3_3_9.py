# Exercise 3.3.9:
# Show that for every regular expression containing repetition 
# operators of the form {m, n}, there is an equivalent regular 
# expression without repetition operators.

import re 

def translate(orig):
    rep_lower = re.compile('(\{[1234567890]*)')
    rep_upper = re.compile('([1234567890]*\})')
    repetition = re.compile('.*\{[1234567890]*,\w*[1234567890]*\}')
    if isinstance(orig, re):
        new_re = orig.pattern
    else:
        new_re = orig
    # replace r{m, n} with r m times, r m+1 times, ... r n times
    # or in a slightly more Lex/no-repetition regex-y way: 
    # r{mx}|r{mx+1}

