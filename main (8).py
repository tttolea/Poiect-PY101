import room
import enemy
import item
import fight
import inventory
import player
import Jurnal
import random
map="""
                    	   room8
                    	     |
        room10 <- room9 <- room7
                             |
                    	   room5-> room6
                             |
                           room4
                             |
          room3 <- room2 <-room1
"""
class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

    def talk(self):
        print(f"\n {self.name} spune:")
        print(f"\"{self.dialogue}\"")

init_dmg=2
nume=input("Introdu numele jucatorului:")
jucator=player.player(nume,100,init_dmg)
MAXHP=jucator.hp
inventory=inventory.inventory()
room4_opend=False
# Creeaza camera 1
room1 = room.Room("Te afli intr-o sala rotunda, luminata de torte albastre. In fata ta sta un batran cu o mantie lunga.")
# Creeaza NPC
batranul = NPC("Maestrul Argan", "Bine ai venit, calatorule... Soarta acestui loc depinde de tine. Alege-ti bine arma, caci drumuri intunecate te asteapta.")
# Creeaza doua arme
sabie = item.item("Sabie de otel", "arma", 6)
barda = item.item("Barda grea", "arma", 8)
# Creeaza Camera 2
room2 = room.Room("Te afli intr-o pestera rece si intunecata. Pe peretii din jur sunt urme de pasi. Un zgomot ciudat se aude din adancurile intunericului.")
# Creeaza inamic (monstru)
cave_spider = enemy.enemy("Cave Spider",4, "beast",50, "Un paianjen uriasa, cu ochi care stralucesc in intuneric, se apropie amenintator.")
# Adauga inamic in camera
room2.add_enemy(cave_spider)
# Creeaza Camera 3
room3 = room.Room("Te afli intr-o sala linistita, cu tavanul inalt si pereti acoperiti de mucegai. In mijlocul camerei, la lumina slaba, se afla un chest vechi si prafuit. Pare ca a stat acolo de mult timp.")
# Creeaza obiectele care sunt gasite in chest
key1 = item.item("Cheie stralucitoare", "obiect", 0)  # Cheia nu face daune
health_potion = item.item("Potiune de viata", "potiune", 0)  # Potiunea de viata restaureaza HP-ul jucatorului
chest_deschis=False
# Creeaza Camera 4
room4 = room.Room("Ai ajuns intr-o camera mica, cu pereti murdari si un miros de umiditate. In fata ta, este o usa metalica, blocata cu un lacat vechi. Pare ca ai nevoie de o cheie pentru a deschide aceasta usa.")

# Creeaza Camera 5
room5 = room.Room("Ai ajuns intr-o camera misterioasa, unde pe un raft prafuit se afla un jurnal vechi. Scrisul altor jucatori poate fi citit, iar tu ai sansa sa adaugi propriile tale ganduri.")

# Creeaza obiectul Jurnal
jurnal = Jurnal.Jurnal()

# Creeaza Camera 6
room6 = room.Room("Ajungi intr-o sala luminata de torțe. Pe un piedestal din piatra, o arma straluceste sub lumina focului.")

# Creeaza arma
sword_of_doom = item.item("Sabia Distrugerii", "magic", 15)

# Adauga arma in camera
room6.add_item(sword_of_doom)

# Creeaza Camera 7
room7 = room.Room("In aceasta incapere, aerul este greu si tensionat. Din umbra, un monstru urias cu doua topoare paseste incet spre tine...")

# Creeaza un inamic puternic
brutus = enemy.enemy("Brutus",6, "orc",150, "Un monstru urias, plin de cicatrici si cu o forta inspaimantatoare.")

# Adauga inamicul in camera
room7.add_enemy(brutus)

# Creeaza Camera 8
room8 = room.Room("In mijlocul camerei se afla un cufar vechi de lemn, prafuit.")

# Creeaza itemele
key_to_room9 = item.item("cheie_camera_9", "key", 0)
steel_armor = item.item("Armura din otel", "armor", 100)

# Creeaza Camera 9
room9 = room.Room("Ajungi in fata unei usi masive, din piatra, acoperita cu rune vechi. Pare sa poata fi deschisa doar cu o cheie speciala...")

# Creeaza Camera 10
room10 = room.Room("Ai pasit intr-o arena uriasa, luminata de focuri albastre. Din intuneric apare o silueta colosala cu ochi rosii stralucitori. Este finalul... \nBoss-ul final te priveste in tacere. Este timpul sa lupti...")

# Creeaza boss-ul
final_boss = enemy.enemy("Umbra Regelui",15,"demon",300,"O entitate masiva formata din fum negru si foc, emanand ura si putere pura.")

# Adauga boss-ul in camera
room10.add_enemy(final_boss)

room1.connect("stanga", room2)
room1.connect("inainte", room4)

room2.connect("inainte", room3)
room2.connect("inapoi", room1)

room3.connect("inapoi", room2)

room4.connect("inainte", room5)
room4.connect("inapoi", room1)

room5.connect("dreapta", room6)
room5.connect("inainte", room7)
room5.connect("inapoi",room4)

room6.connect("inapoi", room5)

room7.connect("stanga", room9)
room7.connect("inainte", room8)
room7.connect("inapoi", room5)

room8.connect("inapoi", room7)

room9.connect("inainte", room10)
room9.connect("inapoi", room7)

current_room = room1  # Pornim din Camera 1

while True: 
    
    if current_room==room1 and room1.visited==False:
        room1.describe()
        batranul.talk()
        print("\nPe un piedestal vezi doua arme:")
        print(f"1. {sabie.name} (Dmg: {sabie.dmg})")
        print(f"2. {barda.name} (Dmg: {barda.dmg})")
        alegere = input("Care arma o alegi? (1/2): ")
        if alegere == "1":
            first_item=sabie
            inventory.add_item(first_item)
            print(f"Ai ales {sabie.name}!")
            jucator.dmg+=sabie.dmg
        elif alegere == "2":
            first_item=barda
            inventory.add_item(first_item)
            print(f"Ai ales {barda.name}!")
            jucator.dmg+=barda.dmg
        else:
            print("Nu ai ales nicio arma... Batranul ofteaza.")
        room1.visited=True
    
    if current_room == room3 and room3.visited == False:
        current_room.describe()
        print("\nDeschide-l! (da/nu)")
        room3.visited = True
        alegere = input("> ").strip().lower()
        if alegere == "da":
            inventory.add_item(key1)
            inventory.add_item(health_potion)
            print("Ai gasit o cheie si o potiune de viata. Le-ai pus in inventar.")
        else:
            room3.visited = False
            print("Ai ales sa nu deschizi cufarul.")
    elif current_room==room3 and room3.visited==True:
        print("Ai fost aici si ai deschis chestul ")    


    if current_room==room4 and room4.visited==False:
        room4.describe()
        room4.visited=True

    if current_room == room5 and room5.visited==False:  # Camera 5 - Jurnal
        if any(item == "Cheie stralucitoare" for item in inventory.items):
            print("\nAi gasit cheia! Deschizi usa cu usurinta.")
            room5.visited=True
            print("Usa se deschide, iar in fata ta se dezvaluie o camera secreta.")
            print("\nPe o masa prafuita gasesti un jurnal cu scrieri de la alti jucatori.")
            try:
                with open("jurnal.txt", "r") as f:
                    print("\n--- Pagini din jurnal ---")
                    print(f.read())
            except FileNotFoundError:
                print("\nJurnalul este gol.")

            scrie = input("Vrei sa scrii si tu in jurnal? (da/nu): ").lower()
            if scrie == "da":
                text = input("Scrie ce vrei sa ramana in jurnal: ")
                with open("jurnal.txt", "a") as f:
                    f.write(f"{jucator.name}: {text}\n")
                print("Ai scris in jurnal.")
    
        else:
            current_room=room4
            print("\nNu ai cheia necesara pentru a deschide usa.")
            print("Camera ramane blocata si nu poti trece mai departe.")

    if current_room==room8 and room8.visited==False:
        room8.describe()
        print("Alegi sa-l deschizi sau nu? (da/nu)")
        alegere = input("> ").strip().lower()
        room8.visited==True
        if alegere == "da":
            inventory.add_item(key_to_room9)
            inventory.add_item(steel_armor)
            print("Ai gasit o cheie si o armura. Le-ai pus in inventar.")
            jucator.hp=jucator.hp+steel_armor.dmg
            MAXHP=MAXHP+steel_armor.dmg
            print("Viata a fost crescuta! ")
        else:
            room8.visited = False
            print("Ai ales sa nu deschizi cufarul.")
    elif current_room==room8 and room8.visited==True:
        print("Ai fost aici si ai deschis chestul ")   

 # Camera 9 - Cheia pentru usa
    if current_room == room9: 

        if any(item == "cheie_camera_9" for item in inventory.items):
            print("\nAi gasit cheia! Deschizi usa cu usurinta.")
            room9.visited=True
            print("O voce iti sopteste: 'Cel ce paseste mai departe nu se mai intoarce.'")
        else:
            current_room=room7
            print("\nNu ai cheia necesara pentru a deschide usa.")
            print("Camera ramane blocata si nu poti trece mai departe.")
    # 📖 Verifica inamicii
    if current_room.enemy:
        current_room.describe()
        print(f"\nUn inamic apare: {current_room.enemy.name}")
        fight_choice = input("Te lupti? (da/nu): ").lower()
        if fight_choice == "da":
            fight_instance = fight.Fight()
            fight_instance.fight(jucator, current_room.enemy, inventory, MAXHP)  
            if jucator.hp <= 0:
                print("Ai murit. Jocul s-a incheiat.")
                break  # Jocul se incheie daca playerul moare
            current_room.enemy = None  # Inamicul a fost invins
        else:
            print("Ai ales sa fugi.")
            continue

    if current_room==room6 and room6.visited==False:
        room6.describe()
        print("Vrei sa iei aceasta sabie? (da/nu) ")
        room6.visited==True
        alegere = input("> ").strip().lower()
        if alegere=="da":
            inventory.add_item(sword_of_doom)
            jucator.dmg=init_dmg+sword_of_doom.dmg
            print("Damage-ul a fost modificat")
            inventory.remove_item(first_item.name)
        elif alegere=="nu":
            room6.visited=False
            print("Atunci intorcete inapoi")
    elif current_room==room6 and room6.visited==True:
        print("Ai fost aici si ai luat arma ")

    # 🧭 Meniu de comenzi
    print("\nComenzi disponibile:")
    print("1. Iesi din camera? (da/nu)")
    print("2. Vezi inventarul (scrie 'inventar')")
    print("3. Vezi starea personajului (scrie 'status')")
    print("4. Verifica descrierea camerei curente (scrie 'descriere')")
    print("5. Uita-te pe harta (scrie 'harta')")
    if "Potiune de viata" in inventory.items:
        print("6. Foloseste potiunea de viata (scrie 'potiune')")

    command = input("\nCe vrei sa faci? ").lower()
    if command =="potiune":
        if (jucator.hp+40)>MAXHP:
            jucator.hp=MAXHP
        else:
            jucator.hp+=40

        inventory.remove_item("Potiune de viata")
  
    if command =="harta":
        print(map)
    # Comanda pentru inventar
    if command == "inventar":
        print("\nInventarul tau:")
        if len(inventory.items) > 0:
            for item in inventory.items:
                print(f"- {item}")
        else:
            print("Inventarul este gol.")
        continue
        
    # Comanda pentru status (afisare viata si nivel)
    if command == "status":
        print(f"\nStatusul tau: {jucator.name}")
        print(f"Viata: {jucator.hp}/{MAXHP}")
        print(f"Damage: {jucator.dmg}")
        continue
    if command=="da":
        direction = input(f"\nUnde vrei sa mergi? {list(current_room.connections.keys())}: ").lower()
        if direction in current_room.connections:
            current_room = current_room.connections[direction]
        else:
            print("Nu poti merge in acea directie. Incearca din nou.")

    if command == "descriere":
        current_room.describe()        
    # 🏆 Camera finala cu Boss
    if current_room == room10:
        print("\nAi ajuns la ultima camera! Un monstru foarte puternic te asteapta!")
        current_room.describe()
        print(f"\nUn inamic apare: {current_room.enemy.name}")
        fight_choice = input("Te lupti? (da/nu): ").lower()
        if fight_choice == "da":
            fight_instance = fight.Fight()
            fight_instance.fight(jucator, current_room.enemy, inventory, MAXHP)  
            if jucator.hp <= 0:
                print("Ai murit. Jocul s-a incheiat.")
                break  # Jocul se incheie daca playerul moare
            else:
                print("Ai invins boss-ul final!")
                print("Felicitari! Ai castigat jocul!")
                break  # Jocul se incheie daca playerul invinge boss-ul
        else:
            print("Ai ales sa fugi. Jocul se incheie. Coward.")
            break  # Jocul se incheie daca playerul fuge de boss