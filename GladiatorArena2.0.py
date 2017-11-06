##Gladiator Arena 2.0
##Bryce Chung
##10-12-17

##A remake of Gladiator Arena in python

import random 

def mainMenu():
    ready = "no"
    while ready == "no":
        print("Welcome to....")
        age = int(input("Enter your age to play: "))
        if age >=18:
            ready = input("Are you ready?(yes/no)\n")
        else:
            print("Sorry too young to play")
mainMenu()
########################
def deathScreen():
    print("You died!!")
    mainMenu()
######################
def lightAttack(playerHp,dodge,enemyHp):
    attackChoice = random.randint(1,3)
    if attackChoice ==1:
        attackChance = random.randint(0,100)
        if attackChance<=100-dodge:
            playerHp=playerHp-3
            print("-----------------------------------")
            print("The enemy swings quickly and deals 3 damage")
            print("-----------------------------------")
            print("You have",playerHp,"HP")
            print("The enemy has",enemyHp,"HP")
    if attackChoice ==2:
        attackChance = random.randint(0,100)
        if attackChance<=70-dodge:
            playerHp=playerHp-5
            print("-----------------------------------")
            print("The enemy strikes and deals 5 damage")
            print("-----------------------------------")
            print("You have",playerHp,"HP")
            print("The enemy has",enemyHp,"HP")
    if attackChoice ==3:
        attackChance = random.randint(0,100)
        if attackChance<=50-dodge:
            playerHp=playerHp-7
            print("-----------------------------------")
            print("The enemy lands a heavy blow and deals 7 damage")
            print("-----------------------------------")
            print("You have",playerHp,"HP")
            print("The enemy has",enemyHp,"HP")
    if playerHp <=0:
        deathScreen()
    return(playerHp)








###################################
def Knight(enemyHp,playerHp,dodge,attackBonus):
    while playerHp >0:
        for i in range(10):
            print("#########################################################")
        playerChoice = int(input("Pick a move\n1)Light\n2)Medium\n3)Heavy\n"))
        if playerChoice ==1:
            attackDmg = 4 + attackBonus
            enemyHp = enemyHp - attackDmg
            print("-----------------------------------")
            print("You swing quickly and deal 4 damage")
            print("-----------------------------------")
        elif playerChoice ==2:
            attackDmg = 7 +attackBonus
            for x in range(1):
                attackChance = random.randint(0,100)
                if attackChance<=50:
                    enemyHp=enemyHp-7
                    print("-----------------------------------")
                    print("You strike and deal 7 damage")
                    print("-----------------------------------")
                else:
                    print("You swing and miss!")
        elif playerChoice==3:
            attackDmg=10+attackBonus
            for x in range(1):
                attackChance = random.randint(0,100)
                if attackChance<=30:
                    enemyHp=enemyHp-10
                    print("-----------------------------------")
                    print("You strike and deal 10 damage")
                    print("-----------------------------------")
                else:
                    print("You swing and miss!")
        else:
            print("You trip and nearly fall")
        if enemyHp <= 0:
            return
        print("You have",playerHp,"HP")
        print("The enemy has",enemyHp,"HP")
        lightAttack(playerHp,dodge,enemyHp)







def light(Class,hpBonus,attackBonus,dodgebonus):
    print("Enemy is light")
    enemyHp=10
    playerHp=20 + hpBonus
    dodge = 10 + dodgeBonus
    if Class == "knight":
        Knight(enemyHp,playerHp,dodge,attackBonus)
        return
##    if Class == "mage":
##        mage(enemyHp,playerHp,dodge,attackBonus)
        
        

        
    


hpBonus=0
attackBonus=0
dodgeBonus = 0
Class=input("Pick a class: knight, mage, or archer\n")
if Class== "knight":
    hpBonus = 10
##if Class=="mage":
##    attackBonus = 5
##if Class=="archer":
##    dodgeBonus = 25
i=0
while i <2:
    enemyType= random.randint(1,1)
    if enemyType == 1:
        light(Class,hpBonus,attackBonus,dodgeBonus)
    elif enemyType == 2:
        medium(Class,hpBonus,attackBonus,dodgeBonus)
    elif enemyType == 3:
        heavy(Class,hpBonus,attackBonus,dodgeBonus)
    i=i+1
