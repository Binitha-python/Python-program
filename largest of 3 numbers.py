firstNum=int(input("Enter first number:"))
secondNum=int(input("Enter second number:"))
thirdNum=int(input("Enter third number:"))
if(firstNum>secondNum and firstNum>thirdNum):
   print(f"The first number is greater.")
elif(firstNum and(secondNum>thirdNum)):
   print(f"The second numberis greater then first number.")
else:
     print(f"The third number is greater.")
