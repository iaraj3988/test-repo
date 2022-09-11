import random 
randomnumber =  random.randint(1, 50)
userguess = None
guess = 0

while(userguess != randomnumber):
    userguess = int(input('enter your guess number:- '))

    guess +=1

    
    if (userguess == randomnumber):
        print("you got your number")

    else:
        if(userguess > randomnumber):
            print("give lower number as input")
        else:
            print("print higher number")

with open('hiscore.txt', 'r') as f:
    hiscore = int(f.read())
with open('hiscore.txt', 'w') as f:
    f.write(str(guess))

print(f'your total gueses is {guess}')