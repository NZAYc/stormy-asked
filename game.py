import random
import sys
import time
from dataclasses import dataclass

'''
Copyright (c) 2021 Adolf and Stormy
Notable contributors: TrollerOfHolland

Permission is hereby granted, free of charge, to any person obtaining a copy
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
'''

debug = False


def askPlayer(question):
    answer = input(question)
    return answer.lower().strip()


def delayPrint(text, delay):
    print(text)
    time.sleep(delay)


def coolTransition(delay=0.25):
    time.sleep(delay)
    for i in range(3):
        delayPrint(".", delay)
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


def handleAttack(attacker, defender):
    time.sleep(0.1)
    print(f"===\n{attacker.name}: {attacker.health}HP, {attacker.strength}STR")
    print(f"{defender.name}: {defender.health}HP, {defender.strength}STR\n===")
    time.sleep(0.1)
    print(f"{attacker.name} IS ATTACKING")
    time.sleep(0.2)
    while (attacker.energy > 0):
        time.sleep(0.2)
        time.sleep(0.2)
        attackType = askPlayer("Pick an attack: (hard attack/fast attack) : ")

        totalDmg = 0
        if attackType == "hard attack":
            if(attacker.energy < 100):
                time.sleep(0.1)
                print("Too tired to do a hard attack now.")
            else:
                time.sleep(0.1)
                attackTypeDmg = random.randint(5, 10) + attacker.strength
                if(debug):
                    attackTypeDmg = 50
                defender.health -= attackTypeDmg
                print(f"{defender.name} took {attackTypeDmg} damage!")
                time.sleep(0.1)
                attacker.energy -= 100
                time.sleep(0.1)

        elif attackType == "fast attack":
            time.sleep(0.1)
            attackTypeDmg = random.randint(1, 7) + defender.strength
            if(debug):
                attackTypeDmg = 50
            defender.health -= attackTypeDmg
            print(f"{defender.name} took {attackTypeDmg} damage!")
            attacker.energy -= 50
            time.sleep(0.1)

    # out of loop, attacker's turn is done
    time.sleep(0.15)
    totalDmg += attackTypeDmg
    # print("\n")
    # print(f"{player.name} ran out of energy.")
    print(f"Total damage dealt: {totalDmg}")
    player.energy = 100

    if(defender.health > 0):
        coolTransition(0.25)
        delayPrint(f"{defender.name} IS ATTACKING", 0.1)
        while (defender.energy > 0):
            time.sleep(0.1)
            attacker.health -= defender.strength
            print(f"{attacker.name} took {defender.strength} damage!")
            defender.energy -= 50
    else:
        return
    defender.energy = 100


def fight(enemy):
    delayPrint(f"Battling {enemy.name}!", 1)

    while True:
        coolTransition(0.25)
        # completes one turn of attack for both args
        handleAttack(player, enemy)

        if(player.health < 1):
            print(f"{player.name} has died.")
            print("Game over.")
            sys.exit(0)
            break
        elif(enemy.health < 1):
            print(f"{enemy.name} has died. {player.name} has gained {enemy.xp} xp.")
            player.xp += enemy.xp
            break


if askPlayer("Do you wish to start the game? (yes/no): ") == 'yes':
    coolTransition()
    print("You are a random ass faggot adventurer going down a gay ass road")
    time.sleep(1)
    if askPlayer("You encounter a divergence in the road, do you go left or right? (left/right) : ") == "left":
        coolTransition(0.25)
        delayPrint(
            "An Ilkhar jumps out of the shrubbery with an intent to rape.", 1)
        if(ilkhar.speed > player.speed):
            delayPrint(
                "It appears the Ilkhar is faster. Running away will probably end in disaster.", 1)
        if askPlayer("Do you engage in combat or run away? (combat/run): ") == 'combat':
            coolTransition(0.25)
            delayPrint("Battle begins.", 1)
            ilkhar.name = "Ilkhar"
            fight(ilkhar)
        else:  # runs away
            coolTransition(0.25)
            delayPrint("Ilkhar catches up to you and rapes you", 1)
            print("Game over")
            sys.exit()
    else:  # right
        coolTransition(0.25)
        delayPrint(
            "You keep going down the faggot ass road, when suddenly you encounter a cave entrence!", 1)
        if askPlayer("Do you enter? (yes/no) : ") == 'yes':
            time.sleep(1)
            delayPrint("A figure shrouded in pure blackness approaches", 1)
            print("It is Kakapoop")
else:
    print("Nigger cracker kike fag gypsie muzzie chink")
    sys.exit()
