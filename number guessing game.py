import random
import time

number=random.randint(1,100)
def intro():
    
    print("May I ask your name?")
    global name
    name=input()
    print(name+",we are going to play a game. I am thinking of a number between 1 to 100.")
    if(number%2==0):
        x='even'
    else:
        x='odd'
    print("\n this is a{}number".format(x))
    time.sleep(.5)
    print("Go ahead and guess")

def pick():
    guessesTaken=0
    while guessesTaken<6:
        time.sleep(.25)
        enter=input("guess")
        
        try:
            guess=int(enter)
            if guess<=100 and guess>=1:
                guessesTaken=guessesTaken+1
                if guessesTaken<6:
                    if guess<number:
                        print("the guess of the number that you entered is too low.")
                    if guess>number:
                        print("the guess of the number that you entered is too high.")
                    if guess!=number:
                        time.sleep(.5)
                        print("Try again:(")
                    if guess==number:
                        break
            if guess>100 or guess<1:
                print("Silly Goose! That number isn't in the range!")
        except:
            
            print("I dont think the number is correct!SORRY:(")
    if guess==number:
        guessesTaken=str(guessesTaken)
        
        print('Good job, {}! You guessed my number in {} guesses!'.format(name, guessesTaken))
    if guess !=number:
        print('Nope. The number I was thinking of was ' + str(number))
playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":

    intro()

    pick()

    print("Do you want to play again?")

    playagain=input()