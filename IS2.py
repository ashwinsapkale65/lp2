# Define the substitution cipher
s = {
'a': 'q',
'b': 'w',
'c': 'e',
'd': 'r',
'e': 't',
'f': 'y',
'g': 'u',
'h': 'i',
'i': 'o',
'j': 'p',
'k': 'a',
'l': 's',
'm': 'd',
'n': 'f',
'o': 'g',
'p': 'h',
'q': 'j',
'r': 'k',
's': 'l',
't': 'z',
'u': 'x',
'v': 'c',
'w': 'v',
'x': 'b',
'y': 'n',
'z': 'm'
}
# Define the encryption and decryption functions
def e(p):
  return "".join([s.get(c,c) for c in p])
def d(c):
 return "".join([{v:k for k,v in s.items()}.get(c,c) for c in c])


p ="lalit"

c=e(p)

print(c)  

d= d(c)

print(d)

