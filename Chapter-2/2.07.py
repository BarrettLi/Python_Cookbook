# Problem: You’re trying to match a text pattern using regular expressions, but it is identifying the
# longest possible matches of a pattern. Instead, you would like to change it to find the shortest
# possible match.

# The problem is like
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
str_pat.findall(text1) # ['no.']
text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2) # ['no." Phone says "yes.']

# to fix this, add the ? modifier after the * operator
str_pat = re.compile(r'\'(.*?)\"')
str_pat.findall(text2)
# ['no.', 'yes.']

# Discussion

# The dot matches any character except for a newline. 
# Adding the ? right after operators such as * or + forces the matching algorithm to look for the
# shortest possible match instead
