# Exercise 3.3.4 Write a regex for the SELECT keyword in SQL; 
# SQL keywords are case insensitive.

import re

select_re = re.compile("[Ss][Ee][Ll][Ee][Cc][Tt]")
