print(ord("a"))
print(ord("A"))

print(chr(70))
print(chr(120))

word = "zttack"
asciiValues = []
cyphered = ""

for c in word:
  asciiValues.append((ord(c)))
  
for i in asciiValues:
  cyphered += chr(i + 1)
  
print(asciiValues)
print(cyphered)
print(word)