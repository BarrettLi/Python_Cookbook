# Problem: Some bored script kiddie has entered the text “pýtĥöñ” intform on your web page
# and you'd like to clean it up somehow

# you might wan to take the sanitation process a step further. Perhaps, for example, you want to
# eliminate whole ranges of characters or strip diacritical marks.

s = 'pýtĥöñ\fis\tawesome\r\n'
s # 'pýtĥöñ\x0cis\tawesome\r\n'

# the first step is to clean up the whitespace.
# to do so, make a small translation table and use translate()
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\t') : None,   # Deleted
}

a = s.translate(remap)
# 'pýtĥöñ is awesome\n'

# you can take this remapping idea a step further and build mush bigger tables.
import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
# 'pýtĥöñ is awesome\n'
b.translate(cmb_chrs)
# 'python is awesome\n'

# as another example, here is a translation table that maps all Unicode decimal digit
# characters to their equivalent in ASCII:
digitmap = { c: ord('0') + unicodedata.digit(chr(c))
             for c in range(sys.maxunicode)
             if unicodedata.category(chr(c)) == 'Nd'}

len(digitmap) # 460

# arabic digits
x = '\u0661\u0662\u0663'
x.translate(digitmap)
'123'

# another technique for cleaning up text involves I/O decoding and encoding functions
a # 'pýtĥöñ is awesome\n'
b = unicodedata.normalize('NFD', a)
b.encode('ascii', 'ignore').decode('ascii')
# 'python is awesome\n'

# Discussion

# A major issue with sanitizing text can be runtime performance.
