import item
import dice
class enemy:
    def __init__(self, name, dmg, type, hp,stry):
        self.name=name
        self.dmg=dmg
        self.type=type
        self.hp=hp
        self.stry=stry

    def damage(self,roll,weapon):
        self.hp-=weapon.dmg*roll

    def __str__(self):
        return self.stry
        