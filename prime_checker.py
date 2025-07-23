number=int(input("Enter a number:"))

if number % 2==0:
        print("Its Even number")
else:
 print("Its Odd number")

prime_number=True
i=2
while i<number:
     if number%i==0:
          prime_number=False
          break
     i+=1


if number > 1 and prime_number:
     print("Its a Prime number")

else:
        print("Its not a Prime number")    
