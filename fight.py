import player
import enemy
import random
import inventory
class Fight:
    def fight(self, character, enemy, inventory, MAXHP):
        print(f"\nLupta a inceput intre {character.name} si {enemy.name}!")
        
        while int(character.hp) > 0 and int(enemy.hp) > 0:
            # Afiseaza starea curenta a characterului si inamicului
            print(f"\n{character.name} - HP: {character.hp}")
            print(f"{enemy.name} - HP: {enemy.hp}")
            
            # characterul ataca
            zar_player = random.randint(1, 10)  # Zar character
            damage_player = zar_player * character.dmg # Daune character
            enemy.hp =enemy.hp- damage_player
            print(f"{character.name} loveste cu un zar de {zar_player} si da {damage_player} daune!")

            # Verifica daca inamicul este invins
            if int(enemy.hp)<= 0:
                print(f"{enemy.name} a fost invins!")
                break
            
            # Inamicul ataca
            zar_enemy = random.randint(1, 10)  # Zar inamic
            damage_enemy = zar_enemy * int(enemy.dmg ) # Daune inamic
            character.hp = character.hp-damage_enemy
            print(f"{enemy.name} loveste cu un zar de {zar_enemy} si da {damage_enemy} daune!")

            # Verifica daca characterul este invins
            if int(character.hp) <= 0:
                print(f"{character.name} a fost invins...")
                break
            if "Potiune de viata" in inventory.items:
                print("Foloseste potiunea de viata?")

                command = input("\nVrei sa o folosesti?(da/nu) ").lower()
                if command =="da":
                    if (character.hp+40)>MAXHP:
                        character.hp=MAXHP
                    else:
                        character.hp+=40

                    inventory.remove_item("Potiune de viata")

            