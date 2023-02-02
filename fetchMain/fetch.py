import pandas as pd
import sys
import json

# * Run from command line using $python fetch.py [points]
# input a number for points *



# *Getting the initial points from command line*
initPoints = int(sys.argv[1])



# *reading from a CSV file using Pandas*
ptsList = []
df = pd.read_csv('transactions.csv')
df.values.tolist() 
count = 0
for i in df.values.tolist():
  ptsList.append(i)
  count+=1


# *sorted list by oldest transaction and spend points for each payer*
  
newL = sorted(ptsList, key = lambda x:x[2])
#print(newL) #*debugging*
for j in newL:
    #print(initPoints) *debugging*
    if(initPoints <= j[1]):
      j[1] =abs(j[1]-initPoints)
      initPoints = 0

    elif(initPoints>=j[1]):
      initPoints = abs(initPoints - j[1])
      j[1] = 0



#*Print statements for debugging*
#print(initPoints)
#print(newL)
#print("\n")





# *Format results into dictionary with each corresponding payer
payerTotal = {}
for j in newL:
  payer = j[0]
  points = j[1]
  if(payer in payerTotal):
    payerTotal[payer]+=points
  else:
    payerTotal[payer]= points



# *Format it like a json file and print result*
print(json.dumps(payerTotal, indent = 4))

    
  
    


  







    








