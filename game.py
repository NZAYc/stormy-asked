import random
import sys
import time
from dataclasses import dataclass

'''
Copyright (c) 2021 Adolf and Stormy <---- aka "The Retards"
And Larsy <---- aka "the Functioning Brain"

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

def delayPrint(text, delay):
    print(text)
    time.sleep(delay)


def coolTransition(delay = 0):
    time.sleep(0.25)
    for i in range(3):
        delayPrint(".", 0.25)

    time.sleep(delay)

class entity:
    def __init__(self, name="Default Entity", health=100, strength=10, speed=10, xp=0, energy=100):
        self.name = name
        self.health = health
        self.strength = strength
        self.speed = speed
        self.xp = xp
        self.energy = energy


player = entity(input("Enter your name: ").strip())
print(f"Welcome, {player.name}.")

ilkhar = entity("Ilkhar", strength=5, speed=20, xp=100)


def calculateAttack(enemy):
    print(f"{player.name} IS ATTACKING")
    while (player.energy > 0):
        time.sleep(0.1)
        attackType = askPlayer("Pick an attack: (hard attack/fast attack) : ")

        attackTypeDmg1 = 0
        totalDmg = 0

        if attackType == "hard attack":
            if(player.energy < 100):
                print("Too tired to do a hard attack now.")
            else:
                attackTypeDmg = random.randint(5, 10) + enemy.strength
                enemy.health -= attackTypeDmg
                print(f"{enemy.name} took {attackTypeDmg} damage!")
                totalDmg += attackTypeDmg + attackTypeDmg1
                print(f"Total damage dealt: {totalDmg}")
                player.energy -= 100

        elif attackType == "fast attack":
            attackTypeDmg = random.randint(1, 7) + enemy.strength
            enemy.health -= attackTypeDmg
            print(f"{enemy.name} took {attackTypeDmg} damage!")
            player.energy -= 50

    print(f"{player.name} ran out of energy.")
    player.energy = 100  # reset every turn?


def fight(enemy):
    delayPrint(f"Battling {enemy.name}!", 1)

    while True:
        # Player attack
        coolTransition()
        calculateAttack(enemy)

        #checking enemy hp before handling player attacks
        if(enemy.health < 1): 
            print(f"{enemy.name} is dead. {player.name} has gained {enemy.xp} experience.")
            player.xp += enemy.xp
            break

        # Enemy attack
        coolTransition()
        delayPrint(f"{enemy.name} IS ATTACKING", 0.1)
        player.health -= enemy.strength
        print(f"{player.name} took {enemy.strength} damage!")

        if(player.health < 1):
            print(f"{player.name} has died.")
            print("Game over.")
            break


if askPlayer("Do you wish to start the game? (yes/no): ") == 'yes':
    print("You are a random ass faggot adventurer going down a gay ass road")
    time.sleep(1)
    if askPlayer("You encounter a divergence in the road, do you go left or right? (left/right) : ") == "left":
        coolTransition()
        delayPrint("An Ilkhar jumps out of the shrubbery with an intent to rape.", 1)
        if(ilkhar.speed > player.speed):
            delayPrint("It appears the Ilkhar is faster. Running away will probably end in disaster.", 1)
        if askPlayer("Do you engage in combat or run away? (combat/run): ") == 'combat':
            coolTransition(delay = 1)
            delayPrint("Battle begins.", 1)
            ilkhar.name = "Ilkhar"
            fight(ilkhar)
        else:  # runs away
            coolTransition(delay = 1)
            delayPrint("Ilkhar catches up to you and rapes you", 1)
            print("Game over")
            sys.exit()
    else:  # right
        coolTransition()
        delayPrint("You keep going down the faggot ass road, when suddenly you encounter a cave entrence!", 1)
        if askPlayer("Do you enter? (yes/no) : ") == 'yes':
            time.sleep(1)
            delayPrint("A figure shrouded in pure blackness approaches", 1)
            print("It is Kakapoop")
else:
    print("Nigger cracker kike fag gypsie muzzie chink")
    sys.exit()
