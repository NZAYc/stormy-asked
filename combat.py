import random
import time
import sys

import interface

def handleAttack(attacker, defender):
    time.sleep(0.1)
    print(f"===\n{attacker.name}: {attacker.health}HP, {attacker.strength}STR")
    interface.delayPrint(f"{defender.name}: {defender.health}HP, {defender.strength}STR\n===", 0.1)
    interface.delayPrint(f"{attacker.name} IS ATTACKING", 0.6)
    while (attacker.energy > 0) and (defender.health > 0):

        attackType = interface.getPlayerInput("Pick an attack: (hard attack/fast attack) : ")
        time.sleep(0.1)

        totalDmg = 0
        if attackType == "hard attack":
            if(attacker.energy < 100):
                interface.delayPrint("Too tired to do a hard attack now.", 0.4)
            else:
                attackDmg = attacker.hardAttack(defender)
                totalDmg += attackDmg
                interface.delayPrint(f"{defender.name} took {attackDmg} damage!", 0.6)

        elif attackType == "fast attack":
            attackDmg = attacker.fastAttack(defender)
            totalDmg += attackDmg
            interface.delayPrint(f"{defender.name} took {attackDmg} damage!", 0.5)

    # out of loop, attacker's turn is done
    attacker.energy = 100
    time.sleep(0.15)
    print(f"Total damage dealt: {totalDmg}")

    if(defender.health <= 0):
        return

    interface.coolTransition()
    interface.delayPrint(f"{defender.name} IS ATTACKING", 0.2)
    while (defender.energy > 0):
        attackDmg = defender.defaultAttack(attacker)
        interface.delayPrint(f"{attacker.name} took {attackDmg} damage!", 0.1)

    defender.energy = 100


def fight(player, enemy):
    interface.delayPrint(f"Battling {enemy.name}!", 1)

    while True:
        interface.coolTransition()
        # completes one turn of attack for both args
        handleAttack(player, enemy)

        if(player.health < 1):
            print(f"{player.name} has died.")
            print("Game over.")
            sys.exit(0)

        elif(enemy.health < 1):
            player.xp += enemy.xp
            print(f"{enemy.name} has died. {player.name} has gained {enemy.xp} xp.")
            if(enemy.name == "Ilkhar"):
                player.inventory.append(enemy.inventory[0])
                print(f"NEW ITEM: {player.name} has gained {enemy.inventory[0].name}!")
                print(f"{enemy.inventory[0].name}:")
                print(f"{enemy.inventory[0].description}")
                for effect in enemy.inventory[0].effects:
                    print(f"{effect}: {enemy.inventory[0].effects[effect]}")
                print("")
            break
