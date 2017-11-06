##Gladiator Arena 2.0
##Bryce Chung
##10-12-17

##A remake of Gladiator Arena in python

from random import randint  



########################
def deathScreen():
    print("You died!!")
    playAgain=input("Would you like to play again? (yes/no)\n")
    if playAgain=="yes":
        fight()
    else:
        quit()
######################
def enemyAttack(playerHp,dodge,enemyDamages,enemyChances):
    attackChoice = randint(1,3)
    if attackChoice ==1:
        attackChance = randint(0,100)
        if attackChance<=enemyChances[0]-dodge:
            playerHp=playerHp-enemyDamages[0]
            print("-----------------------------------")
            print("The enemy swings quickly and deals",enemyDamages[0],"damage")
            print("-----------------------------------")
        else:
            print("Enemy miss")
    if attackChoice ==2:
        attackChance = randint(0,100)
        if attackChance<=enemyChances[1]-dodge:
            playerHp=playerHp-enemyDamages[0]
            print("-----------------------------------")
            print("The enemy strikes and deals",enemyDamages[1],"damage")
            print("-----------------------------------")
        else:
            print("Enemy miss")
    if attackChoice ==3:
        attackChance = randint(0,100)
        if attackChance<=enemyChances[2]-dodge:
            playerHp=playerHp-enemyDamages[2]
            print("-----------------------------------")
            print("The enemy lands a heavy blow and deals",enemyDamages[2],"damage")
            print("-----------------------------------")
        else:
            print("Enemy miss")
    return(playerHp)
###################################
def playerAttack(Class,enemyHp,attackBonus):
    if Class == "knight":
        damages = [4,7,10]
    if Class == "mage":
        damages = [3,8,11]
    if Class == "archer":
        damages= [3,6,9]
    playerChoice = int(input("Pick a move\n1)Light\n2)Medium\n3)Heavy\n"))
    if playerChoice == 1:
        attackDmg = damages[0]+attackBonus
        attackChance = randint(0,100)
        if attackChance <=100:
            enemyHp = enemyHp-attackDmg
            print("---------------------------")
            print("You deal",attackDmg,"damage")
            print("---------------------------")
        else:
            print("You miss")
    if playerChoice == 2:
        attackDmg = damages[1]+attackBonus
        attackChance = randint(0,100)
        if attackChance <=50:
            enemyHp = enemyHp-attackDmg
            print("---------------------------")
            print("You deal",attackDmg,"damage")
            print("---------------------------")
        else:
            print("you miss")
    if playerChoice == 3:
        attackDmg = damages[2]+attackBonus
        attackChance = randint(0,100)
        if attackChance <=30:
            enemyHp = enemyHp-attackDmg
            print("---------------------------")
            print("You deal",attackDmg,"damage")
            print("---------------------------")
        else:
            print("you miss")
    else:
        ("You trip and nearly fall!")
    return enemyHp
########################################################        
def enemy(Class,hpBonus,attackBonus,dodgeBonus,enemyHp,enemyDamages,enemyType,enemyChances):
    if enemyType ==1:
        print("Enemy is light")
    if enemyType ==2:
        print("Enemy is medium")
    if enemyType ==3:
        print("Enemy is heavy")
    playerHp=20 + hpBonus
    dodge = 10 + dodgeBonus
    while enemyHp >0:
        print("You have",playerHp,"hp")
        print("The enemy has",enemyHp,"hp")
        enemyHp=playerAttack(Class,enemyHp,attackBonus)
        if enemyHp <=0:
            print("Enemy killed")
            break
        playerHp= enemyAttack(playerHp,dodge,enemyDamages,enemyChances)
        if playerHp<=0:
            deathScreen()
    return
#####################################################
def fight():
    hpBonus=0
    attackBonus=0
    dodgeBonus = 0
    i=0
    print("knights have extra health, mages do extra damage, archers are highly evasive")
    Class=input("Pick a class: knight, mage, or archer\n")
    if Class== "knight":
        hpBonus = 10
    if Class=="mage":
        attackBonus = 6
        hpBonus = -7
    if Class=="archer":
        dodgeBonus = 25
        attackBonus = 1
    while i <9:
        enemyType= randint(1,3)
        if enemyType == 1:
            enemyHp= 10
            enemyDamages=[3,5,7]
            enemyChances=[100,80,70]
            enemy(Class,hpBonus,attackBonus,dodgeBonus,enemyHp,enemyDamages,enemyType,enemyChances)
        elif enemyType == 2:
            enemyHp= 20
            enemyDamages=[4,7,10]
            enemyChances=[100,60,40]
            enemy(Class,hpBonus,attackBonus,dodgeBonus,enemyHp,enemyDamages,enemyType,enemyChances)
        elif enemyType == 3:
            enemyHp= 30
            enemyDamages=[5,7,13]
            enemyChances=[80,55,40]
            enemy(Class,hpBonus,attackBonus,dodgeBonus,enemyHp,enemyDamages,enemyType,enemyChances)
        i=i+1
######################################################################    
def mainMenu():
    ready = "no"
    while ready == "no":
        print("Welcome to....")
        age = int(input("Enter your age to play: "))
        if age >=18:
            ready = input("Are you ready?(yes/no)\n")
        else:
            print("Sorry too young to play")
    fight()
###################################################################
mainMenu()
        
        

        
    


