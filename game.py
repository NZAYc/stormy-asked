import sys
import time

import entities
import interface
import combat
import config

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

def main():
    ilkhar = entities.entity("Ilkhar") 
    ilkhar.strength = 5
    ilkhar.speed = 20
    ilkhar.xp = 100
    ilkhar.inventory.append(entities.item("Ilkar's migration raft", 100, "The raft Ilkhar used to cross the mediterranian sea."))
    ilkhar.inventory[0].effects["criticalChance"] = 1

    kakapoop = entities.entity("Kakapoop")
    kakapoop.strength = 10
    kakapoop.speed = 11
    kakapoop.xp = 250
 
    if(config.debug):
        ilkhar.health = 10
        print(f"[DEBUG] Set ilkhar hp to 10.")

    print("You are a random ass faggot adventurer going down a gay ass road")
    time.sleep(1)
    if interface.getPlayerInput("You encounter a divergence in the road, do you go left or right? (left/right) : ") == "left":
        interface.coolTransition()
        interface.delayPrint(
            "An Ilkhar jumps out of the shrubbery with an intent to rape.", 1)
        if(ilkhar.speed > player.speed):
            interface.delayPrint(
                "It appears the Ilkhar is faster. Running away will probably end in disaster.", 1)
        if interface.getPlayerInput("Do you engage in combat or run away? (combat/run): ") == 'combat':
            interface.coolTransition()
            interface.delayPrint("Battle begins.", 1)
            combat.fight(player, ilkhar)
        else:  # runs away
            interface.coolTransition()
            interface.delayPrint("Ilkhar catches up to you and rapes you", 1)
            print("Game over")
            sys.exit()
    
    else:  # right
        interface.coolTransition()
        interface.delayPrint(
            "You keep going down the faggot ass road, when suddenly you encounter a cave entrence!", 1)
        if interface.getPlayerInput("Do you enter? (yes/no) : ") == 'yes':
            time.sleep(1)
            interface.delayPrint("A figure shrouded in pure blackness approaches", 1)
            print("It is Kakapoop")
        if(kakapoop.speed > player.speed):
            interface.delayPrint(
                "It appears the Kakapoop is faster. Running away will probably end in disaster.", 1)
        if interface.getPlayerInput("Do you engage in combat or run away? (combat/run): ") == 'combat':
            interface.coolTransition()
            interface.delayPrint("Battle begins.", 1)
            combat.fight(player, kakapoop)
        else:  # runs away
            interface.coolTransition()
            interface.delayPrint("Kakapoop catches up to you and converts you to the true path. Inshallah!", 1)
            print("Game over")
            sys.exit()
            #TODO:  make it download the entire kuran on disk C


if __name__ == "__main__":
    player = entities.entity(input("Enter your name: ").strip())
    print(f"Welcome, {player.name}.")
    if interface.getPlayerInput("Do you wish to start the game? (yes/no): ") == 'yes':
        interface.coolTransition()
        main()
    else:
        print("Nigger cracker kike fag gypsie muzzie chink")
        sys.exit(0)
