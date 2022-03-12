import random
import config

class entity:
    name = "Default Entity"
    health = 100
    strength = 10
    speed = 10
    xp = 0
    energy = 100
    inventory = []

    def __init__(self, name="Default Entity"):
        self.name = name

    def criticalHit(self, chance=10, bonus=10):
        criticalHit = 0
        n = random.randint(1, chance)
        for item in self.inventory:
            if(item.name == "Ilkar's migration raft"):
                if(config.debug):
                    print(f"Base crit: {n}")
                n -= item.effects["criticalChance"]
                if(config.debug):
                    print(f"New crit: {n}")

        if n <= 1:
            bonus = random.randint(1, bonus)
            criticalHit += bonus

            # We can add more elifs per entity, but a better method would be IDs.
            if(self.name == "Kakapoop"):
                print(f"Kakapoop calls upon the might of Allah, inshallah! +{bonus} DAMAGE!")
            else:
                print(f"CRITICAL HIT! +{bonus} DAMAGE!")

        return criticalHit

    def defaultAttack(self, target):
        attackTypeDmg = random.randint(1, 15) + self.strength + self.criticalHit(10, 10)
        self.energy -= 100
        target.health -= attackTypeDmg
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

class item:
    effects = {}

    def __init__(self, name="Default Item", durability=100, description="Just a default item."):
        self.name = name
        self.durability = durability
        self.description = description
