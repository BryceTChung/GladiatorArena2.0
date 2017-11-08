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
            print("\nEnemy miss\n")
    if attackChoice ==2:
        attackChance = randint(0,100)
        if attackChance<=enemyChances[1]-dodge:
            playerHp=playerHp-enemyDamages[0]
            print("-----------------------------------")
            print("The enemy strikes and deals",enemyDamages[1],"damage")
            print("-----------------------------------")
        else:
            print("\nEnemy miss\n")
    if attackChoice ==3:
        attackChance = randint(0,100)
        if attackChance<=enemyChances[2]-dodge:
            playerHp=playerHp-enemyDamages[2]
            print("-----------------------------------")
            print("The enemy lands a heavy blow and deals",enemyDamages[2],"damage")
            print("-----------------------------------")
        else:
            print("\nEnemy misses\n")
    return(playerHp)
###################################
def playerAttack(Class,enemyHp,attackBonus):
    if Class == "knight":
        damages = [4,7,10]
    if Class == "mage":
        damages = [3,8,11]
    if Class == "archer":
        damages= [3,6,9]
    playerChoice = int(input("\nPick a move\n1)Light\n2)Medium\n3)Heavy\n"))
    if playerChoice == 1:
        attackDmg = damages[0]+attackBonus
        attackChance = randint(0,100)
        if attackChance <=100:
            enemyHp = enemyHp-attackDmg
            print("---------------------------")
            print("You deal",attackDmg,"damage")
            print("---------------------------")
        else:
            print("\nYou miss\n")
    if playerChoice == 2:
        attackDmg = damages[1]+attackBonus
        attackChance = randint(0,100)
        if attackChance <=70:
            enemyHp = enemyHp-attackDmg
            print("---------------------------")
            print("You deal",attackDmg,"damage")
            print("---------------------------")
        else:
            print("\nYou miss\n")
    if playerChoice == 3:
        attackDmg = damages[2]+attackBonus
        attackChance = randint(0,100)
        if attackChance <=40:
            enemyHp = enemyHp-attackDmg
            print("---------------------------")
            print("You deal",attackDmg,"damage")
            print("---------------------------")
        else:
            print("\nYou miss\n")
    else:
        ("You trip and nearly fall!")
    return enemyHp
########################################################        
def enemy(Class,hpBonus,attackBonus,dodgeBonus,enemyHp,enemyDamages,enemyType,enemyChances):
    if enemyType ==1:
        print("\nEnemy is light\n")
    if enemyType ==2:
        print("\nEnemy is medium\n")
    if enemyType ==3:
        print("\nEnemy is heavy\n")
    playerHp=20 + hpBonus
    dodge = 10 + dodgeBonus
    while enemyHp >0:
        print("---------------------------")
        print("You have",playerHp,"hp")
        print("The enemy has",enemyHp,"hp")
        print("---------------------------")
        enemyHp=playerAttack(Class,enemyHp,attackBonus)
        if enemyHp <=0:
            print("Enemy killed!")
            break
        playerHp= enemyAttack(playerHp,dodge,enemyDamages,enemyChances)
        if playerHp<=0:
            deathScreen()
    return
####################################################

    
#####################################################
def fight():
    hpBonus=0
    attackBonus=0
    dodgeBonus = 0
    i=0
    gold = 0
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
        goToShop = input("Would you like to visit the shop? (yes/no)\n")
        if goToShop == "yes":
            while True:
                print("\nYou have",gold,"gold pieces")
                purchase=int(input("pick an item:\n1)+3hp Cost 3 gold\n2)+1attack Cost 2 gold\n3)+5Dodge Cost 3 gold\n4)Leave shop\n"))
                if purchase ==1:
                    if gold >=3:
                        gold = gold-3
                        hpBonus = hpBonus +3
                        print("Purchased!")
                    else:
                        print("Not enough gold")
                if purchase ==2:
                    if gold >=2:
                        gold = gold-2
                        attackBonus = attackBonus +1
                        print("Purchased!")
                    else:
                        print("Not enough gold")
                if purchase ==3:
                    if gold >=3:
                        gold = gold-3
                        dodgeBonus = dodgeBonus +5
                        print("Purchased!")
                    else:
                        print("Not enough gold")
                if purchase ==4:
                    break
            
            
        if enemyType == 1:
            enemyHp= 10
            enemyDamages=[3,5,7]
            enemyChances=[100,80,70]
            enemy(Class,hpBonus,attackBonus,dodgeBonus,enemyHp,enemyDamages,enemyType,enemyChances)
            gold = gold +1
        elif enemyType == 2:
            enemyHp= 20
            enemyDamages=[4,7,10]
            enemyChances=[100,60,40]
            enemy(Class,hpBonus,attackBonus,dodgeBonus,enemyHp,enemyDamages,enemyType,enemyChances)
            gold = gold +2
        elif enemyType == 3:
            enemyHp= 30
            enemyDamages=[5,7,13]
            enemyChances=[80,55,40]
            enemy(Class,hpBonus,attackBonus,dodgeBonus,enemyHp,enemyDamages,enemyType,enemyChances)
            gold = gold + 3
        i=i+1

    #Boss fight
    print("You approach the defending champion... goodluck")
    enemyHp=100
    enemyDamages=[10,15,20]
    enemyChances=[80,70,50]
    enemyType=4
    enemy(Class,hpBonus,attackBonus,dodgeBonus,enemyHp,enemyDamages,enemyType,enemyChances)
    print("you win!")
    deathScreen() 

######################################################################    
def mainMenu():
    ready = "no"
    while ready == "no":
        print("Welcome to Gladiator Arena 2.0 a python re-make\nThe goal is to beat 9 enemies and the defending champion")
        age = int(input("Enter your age to play: "))
        if age >=18:
            ready = input("Are you ready?(yes/no)\n")
        else:
            print("Sorry too young to play")
    fight()
###################################################################
mainMenu()
        
        

        
    


