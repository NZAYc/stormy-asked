import random, sys, time
from dataclasses import dataclass

'''
Stormy & Sl*v License

Copyright (c) 2021 Adolf and Stormy.Inc

Permission is hereby NOT granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Stealing niggas gotta pay royalties
'''

def askPlayer(question):
    answer = input(question)
    return answer.lower().strip()

def coolTransition():
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)

class entity:
    name = "0"
    health = 100
    strenght = 10
    speed = 10
    xp = 0
    energy = 100

def calculateAttack(attackType, enemy):
    if enemy.energy == 0:
        print("You ran out of energy.")
        return # OR, continue getting raped

    attackTypeDmg1 = 0
    totalDmg = 0                  
    
    if attackType == "hard attack":
        attackTypeDmg = random.randint(5,10) + enemy.strenght
        enemy.health -= attackTypeDmg
        print(f"{enemy.name} took {attackTypeDmg} damage!")
        totalDmg += attackTypeDmg + attackTypeDmg1
        print(f"Total damage dealt: {totalDmg}") 
        enemy.energy -= 100

    elif attackType == "fast attack":
        attackTypeDmg = random.randint(1,7) + enemy.strenght
        enemy.health -= attackTypeDmg
        print(f"{enemy.name} took {attackTypeDmg} damage!")
        enemy.energy -= 50

        attackType = askPlayer("Pick an attack: (hard attack/fast attack) : ")

        if attackType == "fast attack":
            attackTypeDmg1 = random.randint(1,7) + enemy.strenght
            enemy.health -= attackTypeDmg1
            print(f"{enemy.name} took {attackTypeDmg} damage!")
            totalDmg += attackTypeDmg + attackTypeDmg1
            print(f"Total damage dealt: {totalDmg}")
            enemy.energy -= 50

    if attackType == "hard attack":
        if(enemy.energy < 100):
            print("Too tired to do a hard attack now.")
        else:
            attackTypeDmg = random.randint(5,10) + enemy.strenght
            enemy.health -= attackTypeDmg
            print(f"{enemy.name} took {attackTypeDmg} damage!")
            totalDmg += attackTypeDmg + attackTypeDmg1
            print(f"Total damage dealt: {totalDmg}") 
            enemy.energy -= 100

def fight(enemy):
    print(f"Battling {enemy.name}!")
    time.sleep(1)

    fightOver = False
    while fightOver == False and player.health > 1 and enemy.health > 1:
        attackType = askPlayer("Pick an attack: (hard attack/fast attack) : ")
        calculateAttack(attackType, enemy)
        if player.health == 0 or enemy.health == 0:
            fightOver = True

    if(player.health < 1):
        print(f"{player.name} has died.")
        print("Game over.")
        sys.exit()

    if(enemy.health < 1):
        print(f"{enemy.name} is dead. {player.name} has gained {enemy.xp} experience.")
        player.xp += enemy.xp

player = entity()
player.name = input("Enter your name: ").strip()
print(f"Welcome, {player.name}.")

enemy = entity()
ilkhar = enemy()
ilkhar.name = "Ilkhar"
ilkhar.strenght = 5
ilkhar.speed = 20
ilkhar.xp = 100

if player.energy == 0:
    print(f"{enemy}'s turn.")
    

if askPlayer("Do you wish to start the game? (yes/no): ") == 'yes':
    print("You are a random ass faggot adventurer going down a gay ass road")
    time.sleep(1)
    if askPlayer("You encounter a divergence in the road, do you go left or right? (left/right) : ") == "left":
        coolTransition()
        print("An Ilkhar jumps out of the shrubbery with an intent to rape.")
        time.sleep(1)
        if(ilkhar.speed > player.speed):
            print("It appears the Ilkhar is faster. Running away will probably end in disaster.")
            time.sleep(1)
        if askPlayer("Do you engage in combat or run away? (combat/run): ") == 'combat':
            coolTransition()
            time.sleep(1)
            print("Battle begins.")
            time.sleep(1)
            ilkhar.name = "Ilkhar"
            fight(ilkhar)
        else: # runs away
            coolTransition()
            time.sleep(1)
            print("Ilkhar catches up to you and rapes you")
            time.sleep(1)
            print("Game over")
            sys.exit()
    else: # right
        coolTransition()
        print("You keep going down the faggot ass road, when suddenly you encounter a cave entrence!")
        time.sleep(1)
        if askPlayer("Do you enter? (yes/no) : ") == 'yes':
            time.sleep(1)
            print("A figure shrouded in pure blackness approaches")
            time.sleep(1)
            print("It is Kakapoop")
else:
    print("Nigger cracker kike fag gypsie muzzie chink")
    sys.exit()

