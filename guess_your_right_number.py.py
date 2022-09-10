import random
randomnumber = random.randint(1,10  )
userguess =  None
guess = 0
while(userguess!=randomnumber):
    userguess = int(input('enter the number:- '))
    guess +=1
    if(userguess == randomnumber):
        print("thats great")
    else:
        if (userguess > randomnumber):
            print("write lower")
        else:
            print("write upper")
       

print(f"you guess the number in {guess} th time")

print(f'the number is {randomnumber}')

    







