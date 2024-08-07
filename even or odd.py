num=int(input("Enter valid non zero,positive integer"))
print(f"You have given input of...",num)
if (num<=0):
   print(f"Enter valid non zero positive integer.")
else:
 if(num%2)==0:
   print(f"The given number'(num)'is even.")
 else:
  print(f"The given number '(num)'is odd.")
