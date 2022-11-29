#A loan calculator that shows how much money you owe for a loan of $1,000 with a 5% APR (APR is fancy for Annual Percentage Rate) over 10 years.

amount = int (1000)         #amount of loan.

apr = float (0.05)          #5% annual percentage rate.
  
for year in range (10) :    #10 years duration.
  
  amount += amount * apr      #calculating loan

  print (round (amount, 2))
