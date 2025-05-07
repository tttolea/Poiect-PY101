import item

class inventory:
    def __init__(self):
        self.items = {}  # cheie: numele itemului, valoare: obiectul item

    def add_item(self, item_obj):
        if item_obj.name not in self.items:
            self.items[item_obj.name] = item_obj
        print(f"{item_obj.name} a fost adăugat în inventar.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} a fost eliminat din inventar.")
        else:
            print(f"{item_name} nu a fost găsit în inventar.")

    def list_items(self):
        if not self.items:
            print("Inventarul este gol.")
        else:
            print("Obiecte în inventar:")
            for item in self.items.values():
                print(f"- {item.name}")
