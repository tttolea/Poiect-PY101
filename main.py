import room
import enemy
import item
import fight
import inventory
import player
#gamedata

inventory=inventory.inventory()
character=player.player("cretu", 69)
firstRoom= room.room("You see a lamp in the corner of the room, shady looking box underneath a burnt table, barely standing. Right beside the lamp, is a crouched silhoutte, you cant make out what IT is.")
Gorlax= enemy.enemy("gorlax", 3, 50, "whiteguy", "Old guy with one hand, doesnt look friendly" )
irn_swrd= item.item("iron sowrd", "steel", 5)
firstRoom.add_item(irn_swrd)

first#gamedata

print(firstRoom)

choice=input("You see a steel sword at your feet, do you take it or leave it?")
if(choice == "yes"):
    inventory.add_item(firstRoom.item)

print(firstRoom.enemy)
fight.fight(character, firstRoom.enemy)

print("game joever")