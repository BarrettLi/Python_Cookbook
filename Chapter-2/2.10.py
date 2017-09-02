# Problem: You are using regular expressions to process text, but are concerned about the handling
# of Unicode characters

# re module is already programmed with rudimentary knowledge of certain Unicode character classes.
import re
num = re.compile('\d+')
# ASCII digits
num.match('123')
# <_sre.SRE_Match object at 0x1007d9ed0>

# Arabic digits
num.match('\u0661\u0662\u0663')
# <_sre.SRE_Match object at 0x101234030>

# if you need to include specific Unicode characters in patterns, you can use the usual escape
# sequence for Unicode characters.
# here is a regex that matches all characters in a few different Arabic code pages:
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

# it is important to be aware of special cases besides normalizing and possibly sanitizing all text
# to a standard form first (2.9) when performing matching and searching operations
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
pat.match(s) # Matches
# <_sre.SRE_Match object at 0x10069d370>
pat.match(s.upper()) # Doesn't match
s.upper() # Case folds
# 'STRASSE'
