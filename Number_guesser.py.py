print("Guess my number")
import random
favourite_number=random.randint(1,10)
tries=0
while True:
    number=int(input("Lets see Can you read my mind Gueess a number from 1-10 ?"))
    tries+=1
    if number==favourite_number:
       if tries==1:
        print("Wow ! you got that in first try 🎉")
       else:
        print("Wow !! are you a magician 😲")
        print("you have guessed it correctly!! 🤩")
       break
    elif abs(number-favourite_number)==1:
        print(" You are almost there just littile bit close 🤏🏻 ")

    elif abs(number-favourite_number)==2 :
        print("ohh you just lost it just by 2 🫢 , I guess you will have to try that again")

    else:
        print("No!! thats streched out  , I thought you know me better ! 🥲 , lets try that again")

print(f"Well done bro you have got right in {tries} tries, I know you would finally guessed it correctly 🎉😁")
