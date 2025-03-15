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
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage    
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage    
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
        

# WAAAAAAAAAGH
class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy  = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            output = self.saxonArmy[0].receiveDamage(self.vikingArmy[0].strength)
            if "died" in output:
                self.saxonArmy.pop(0)
        
            return output
    
    def saxonAttack(self):
        if len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0:
            output = self.vikingArmy[0].receiveDamage(self.saxonArmy[0].strength)
            if "died" in output:
                self.vikingArmy.pop(0)
        
            return output

    def showStatus(self):
        saxon_quantity = len(self.saxonArmy)
        viking_quantity = len(self.vikingArmy)
        
        if saxon_quantity > 0 and viking_quantity > 0:
            return "Vikings and Saxons are still in the thick of battle."
        if viking_quantity > 0:
            return "Vikings have won the war of the century!"
        if saxon_quantity:
            return "Saxons have fought for their lives and survive another day..."
        


