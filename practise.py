import random 
randomnumber =  random.randint(1, 100)
userguess = None
guess = 0

while(userguess!=randomnumber):
    userguess = int(input("enter your number:- "))
    guess +=1       
    
    if userguess == randomnumber:
        print("this is your guess number")
    else:
        if(userguess>randomnumber):
            print("please lower number")
        else:
            print("please upper number ")


print(f"your total guesses is {guess}")   


print(f'the number is {randomnumber}')

with open("score.txt","r") as f:
    score = int(f.read())
if guess<score:
    print("you broke the score")
    with open("score.txt","w") as f:
        f.write(str(guess))
