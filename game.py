import random
import sys
import time

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

def getPlayerInput(question):
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
    name = "Default Entity"
    health = 100
    strength = 10
    speed = 10
    xp = 0
    energy = 100

    def __init__(self, name="Default Entity"):
        self.name = name

    def criticalHit(self, chance=10, bonus=10):
        criticalHit = 0
        if random.randint(1, chance) == 1:
            bonus = random.randint(1, bonus)
            criticalHit += bonus
            if(self.name == "Kakapoop"):
                print(f"Kakapoop calls upon the might of Allah, inshallah! +{bonus} DAMAGE!")
            else:
                print(f"CRITICAL HIT! +{bonus} DAMAGE!")

        return criticalHit

    def defaultAttack(self, target):
        attackTypeDmg = random.randint(1, 15) + self.strength + self.criticalHit(10, 10)
        self.energy -= 100
        target.health -= attackTypeDmg
        # return self.strength
        return attackTypeDmg

    def fastAttack(self, target):
        attackTypeDmg = random.randint(1, 7) + self.strength + self.criticalHit(5, 5)
        self.energy -= 50
        target.health -= attackTypeDmg
        return attackTypeDmg

    def hardAttack(self, target):
        attackTypeDmg = random.randint(5, 10) + self.strength + self.criticalHit(10, 40)
        self.energy -= 100
        target.health -= attackTypeDmg
        return attackTypeDmg

def handleAttack(attacker, defender):
    time.sleep(0.1)
    print(f"===\n{attacker.name}: {attacker.health}HP, {attacker.strength}STR")
    delayPrint(f"{defender.name}: {defender.health}HP, {defender.strength}STR\n===", 0.1)
    delayPrint(f"{attacker.name} IS ATTACKING", 0.6)
    while (attacker.energy > 0) and (defender.health > 0):

        attackType = getPlayerInput("Pick an attack: (hard attack/fast attack) : ")
        time.sleep(0.1)

        totalDmg = 0
        if attackType == "hard attack":
            if(attacker.energy < 100):
                delayPrint("Too tired to do a hard attack now.", 0.4)
            else:
                attackDmg = attacker.hardAttack(defender)
                totalDmg += attackDmg
                delayPrint(f"{defender.name} took {attackDmg} damage!", 0.6)

        elif attackType == "fast attack":
            attackDmg = attacker.fastAttack(defender)
            totalDmg += attackDmg
            delayPrint(f"{defender.name} took {attackDmg} damage!", 0.5)

    # out of loop, attacker's turn is done
    attacker.energy = 100
    time.sleep(0.15)
    print(f"Total damage dealt: {totalDmg}")

    if(defender.health <= 0):
        return

    coolTransition()
    delayPrint(f"{defender.name} IS ATTACKING", 0.2)
    while (defender.energy > 0):
        attackDmg = defender.defaultAttack(attacker)
        delayPrint(f"{attacker.name} took {attackDmg} damage!", 0.1)

    defender.energy = 100


def fight(player, enemy):
    delayPrint(f"Battling {enemy.name}!", 1)

    while True:
        coolTransition()
        # completes one turn of attack for both args
        handleAttack(player, enemy)

        if(player.health < 1):
            print(f"{player.name} has died.")
            print("Game over.")
            sys.exit(0)

        elif(enemy.health < 1):
            player.xp += enemy.xp
            print(f"{enemy.name} has died. {player.name} has gained {enemy.xp} xp.")
            break


def main():
    player = entity(input("Enter your name: ").strip())

    ilkhar = entity("Ilkhar") 
    ilkhar.strength = 5
    ilkhar.speed = 20
    ilkhar.xp = 100

    kakapoop = entity("Kakapoop")
    kakapoop.strength = 10
    kakapoop.speed = 11
    kakapoop.xp = 250

    print(f"Welcome, {player.name}.")
    if getPlayerInput("Do you wish to start the game? (yes/no): ") == 'yes':
        coolTransition()
        print("You are a random ass faggot adventurer going down a gay ass road")
        time.sleep(1)
        if getPlayerInput("You encounter a divergence in the road, do you go left or right? (left/right) : ") == "left":
            coolTransition()
            delayPrint(
                "An Ilkhar jumps out of the shrubbery with an intent to rape.", 1)
            if(ilkhar.speed > player.speed):
                delayPrint(
                    "It appears the Ilkhar is faster. Running away will probably end in disaster.", 1)
            if getPlayerInput("Do you engage in combat or run away? (combat/run): ") == 'combat':
                coolTransition()
                delayPrint("Battle begins.", 1)
                fight(player, ilkhar)
            else:  # runs away
                coolTransition()
                delayPrint("Ilkhar catches up to you and rapes you", 1)
                print("Game over")
                sys.exit()
        else:  # right
            coolTransition()
            delayPrint(
                "You keep going down the faggot ass road, when suddenly you encounter a cave entrence!", 1)
            if getPlayerInput("Do you enter? (yes/no) : ") == 'yes':
                time.sleep(1)
                delayPrint("A figure shrouded in pure blackness approaches", 1)
                print("It is Kakapoop")
            if(kakapoop.speed > player.speed):
                delayPrint(
                    "It appears the Kakapoop is faster. Running away will probably end in disaster.", 1)
            if getPlayerInput("Do you engage in combat or run away? (combat/run): ") == 'combat':
                coolTransition()
                delayPrint("Battle begins.", 1)
                fight(player, kakapoop)
            else:  # runs away
                coolTransition()
                delayPrint("Kakapoop catches up to you and converts you to the true path. Inshallah!", 1)
                print("Game over")
                sys.exit()
                
                #TODO:  make it download the entire kuran on disk C
                
    else:
        print("Nigger cracker kike fag gypsie muzzie chink")
        sys.exit()

if __name__ == "__main__":
    main()
