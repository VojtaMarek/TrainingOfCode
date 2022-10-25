import random

Player = 0
Device = 0
Opt = ["rock", "paper", "scissors"]

def who_won ():
#returns 0 for Player and 1 for Device
    if Player == 0 :
        if Device == 2 :
            return 0 #Player won
        elif Device == 1 :
            return 1 #Device won
    elif Player == 1:
        if Device == 0 :
            return 0 #Player won
        elif Device == 2 :
            return 1 #Device won
    elif Player == 2:
        if Device == 1 :
            return 0 #Player won
        elif Device == 0 :
            return 1 #Device won
    else:
        return None


print ("Welcome, start here..")
while 1:
    Player = int(input('\nChoose "0" for ROCK, "1" for PAPER, or "3" for SCISSORS: '))
    Device = random.randint(0, 2)
    print ("--->>> " + Opt[Player] + " -vs- " + Opt[Device] + " <<<---", end=" ")
    if who_won() == 1:
        print ("Device won. :/")
    elif who_won() == 0:
        print ("You won! :)")
    else:  
        print ("It's a tie.")
        continue
