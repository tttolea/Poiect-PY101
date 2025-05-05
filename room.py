class room:
    def __init__(self, stry):
        self.stry=stry
        
    def add_enemy(self, enemy):
        self.enemy=enemy
    
    def add_item(self, item):
        self.item=item

    def __str__(self):
        return self.stry
    def alegere(self, inainte, stanga, dreapta, inapoi):
        self.inainte=inainte

    def cheie(self, inventory):
        if inventory.items[key]==NULL