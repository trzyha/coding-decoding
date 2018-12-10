#simple coding decoding program
sentence = input ("Input your text: ")
codedSentence = []
uncodedSentence = []
for x in range (0,len(sentence)):
  #print (sentence[x])
  senToInt = ord(sentence[x])+3
  #print (senToInt)
  senIntToChar = chr(senToInt)
  #print (senIntToChar)
  codedSentence.append(senIntToChar) 
print ("This is coded text: " + "".join(codedSentence))

for x in range (0, len(codedSentence)):
  senToInt = ord(codedSentence[x])-3
  senIntToChar = chr(senToInt)
  uncodedSentence.append(senIntToChar)
print ("".join(uncodedSentence))