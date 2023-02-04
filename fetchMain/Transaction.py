import json
import pandas as pd


class Transaction:
  def __init__(self,fileName,initPoints):
    self.fileName = fileName;
    self.initPoints = initPoints


  #spendPoints method does the logic for spending points       and updating payers
  # returns jsonObject
  def spendPoints(self):
   
    # *reading from a CSV file using Pandas*
    ptsList = []
    df = pd.read_csv(self.fileName)
    df.values.tolist() 
    count = 0
    for i in df.values.tolist():
      ptsList.append(i)
      count+=1
    
    # *sorted list by oldest transaction and spend points       for each payer*
    newL = sorted(ptsList, key = lambda x:x[2])
    for j in newL:
      if(self.initPoints<0):
        print("OVERSPENDING")
      if(self.initPoints <= j[1]):
        j[1] =abs(j[1]-self.initPoints)
        self.initPoints = 0
      elif(self.initPoints>=j[1]):
        self.initPoints = abs(self.initPoints - j[1])
        j[1] = 0
  
    # *Format results into dictionary with each                 corresponding payer
    payerTotal = {}
    for j in newL:
      payer = j[0]
      points = j[1]
      if(payer in payerTotal):
        payerTotal[payer]+=points
      else:
        payerTotal[payer]= points 
    
    # return json object to print
    return (json.dumps(payerTotal, indent = 4)) 

  
  
  # *take in json object and print result*
  def printResult(self,jsonObject):
    print(jsonObject)
  
