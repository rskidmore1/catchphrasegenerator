import json 
import random 

with open("catchPhrase.json") as json_data:
  d = json.load(json_data)

def selectType(): 
  typeNum = random.random() 
  typ = ''
  if typeNum >= 0.666666667:
    typ = 'vanquishing'
  elif typeNum >= 0.333333333:
    typ = 'expression'
  else: 
    typ = 'self-referrence' 


  if typ == 'vanquishing':
    set1 = d[typ].values()[0]
    set2 = d[typ].values()[1]
    print random.choice(set1) + random.choice(set2)
  elif typ == 'expression':
    set1 = d[typ].values()[0]
    set2 = d[typ].values()[1]
    print random.choice(set1) + random.choice(set2)
  else: 
    set1 = d[typ].values()[0]
    set2 = d[typ].values()[1]
    print random.choice(set2) + random.choice(set1)


selectType()



