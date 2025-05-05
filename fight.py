import player
import enemy
import dice
def fight(play, enem):
    while(play.hp > 0 & enem.hp >0):
        choice=int(input("Your turn, what do you do: 1.Fight  2.Flee  3.Look cute"))
        if(choice==1):
                roll=dice.dice()
                print(f"You rolled a {roll} and dealt {roll*play.inventory.items["weapon"].dmg}")
                enemy.damage(play.inventory.items["weapon"], roll)
        else:
             print("you die")
            