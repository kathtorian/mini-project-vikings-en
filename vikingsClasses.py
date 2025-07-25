import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.health -= damage
        

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def battleCry(self):
        return f"Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"
        else:
            return f"An error has occurred"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)   

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health <= 0:
            return f"A Saxon has died in combat"
        else:
            return f"An error has occurred"


# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
        
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damage = viking.strength
        totaldamage = saxon.receiveDamage(damage)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return totaldamage
    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = saxon.strength
        totaldamage = viking.receiveDamage(damage)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return totaldamage

    def showStatus(self):
        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >=1:
            return f"Vikings and Saxons are still in the thick of battle."
        elif len(self.saxonArmy) <= 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) <= 0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"An error has occurred..."
    pass