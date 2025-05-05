import item 
import dice
import inventory
class player:
    def __init__(self, name, hp):
        self.name=name
        self.hp=hp
        

    def heal(self, item, roll):
        self.hp+=item.dmg*roll

    def dmg(self,dmg):
        self.hp-=dmg*dice.dice()
