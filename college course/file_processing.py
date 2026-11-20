txt = open("file.txt").read()
numOfG = 0
numOfC = 0

for i in txt:
  if i == "G":
    numOfG += 1
  elif i == "C":
    numOfC += 1
    
print((numOfC + numOfG)/ len(txt))