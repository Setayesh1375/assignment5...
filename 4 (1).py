
from math import factorial
 
rows = int(input("Please enter the number of rows:"))
for i in range(rows):
   
    for j in range(i+1):
 
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
    print()
    
    
