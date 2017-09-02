# Problem: You're trying to match a block of text using a regular expression, but you need the
# match to span multiple lines.

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
              multiline comment */'''

comment.findall(text1) # [' this is a comment ']
comment.findall(text2) # []

# to fix the problem
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2) # [' this is a\n multiline comment ']
# (?:.|\n) specifies a noncapture group

# Discussion

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
comment.findall(text2)
# [' this is a\n multiline comment ']

# re.DOTALL might be problematic when working on an extremely complicated pattern
