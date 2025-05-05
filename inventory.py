import item

class inventory:
    def __init__(self):
        self.items={}
    def add_item(self, item):
        if(item.cls=="weapon"):
            self.items["weapon"]=item
        if(item.cls=="armor"):
            self.items["weapon"]=item
        if(item.cls=="weapon"):
            self.items["weapon"]=item
        