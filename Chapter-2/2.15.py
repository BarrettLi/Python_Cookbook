# Problem: You want to create a string in which embedded variable names are substituted with a 
# string representation of a variable's value
s = '{name} has {n} messages.'
s.format(name='Guido', n=37)
# 'Guido has 37 messages.'


# One subtle feature of vars() is that it also works with instances
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido', 37)
s.format_map(vars(a))
# 'Guido has 37 messages.'

s.format(name='Guido') # KeyError: 'n'

# one way to avoid this is to define an alternative dictionary class with a __missing__() method
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n # make sure n is undefined
s.format_map(safesub(vars()))
# 'Guido has {n} messages.'

# if you find yourself frequently performing these steps in your code, you could hide the variable
# substitution process vehind a small utility function that employs a so-called 'frame hack'
import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}')) # Hello Guido
print(sub('You have {n} messages.')) # You have 37 messages
print(sub('Your favorite color is {color}')) # Your favorite color is {color}
