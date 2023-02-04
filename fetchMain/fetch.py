import sys
from Transaction import Transaction


# *Getting the initial points from command line*
initPoints = int(sys.argv[1])

#creates Transaction object
tr1 = Transaction("transactions.csv",initPoints )

#returns jsonObject and prints result to console
jsonObject = tr1.spendPoints()
tr1.printResult(jsonObject)













    
  
    


  







    








