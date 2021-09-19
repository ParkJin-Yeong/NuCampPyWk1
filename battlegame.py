from bg_classes import char
from bg_classes import player

wizard, elf, human, dragon = char("Wizard", 70, 150), char(
    "Elf", 100, 100), char("Human", 150, 20), char("Dragon", 300, 50)


while True:  # todo create char selector class
    print(f"1) {wizard.name}")
    print(f"2) {elf.name}")
    print(f"3) {human.name}")

    try:
        playerchoice = int(input("Choose a character: "))
        break

    except:
        print("Invalid choice")

name = input("What is your name, adventurer? ")


if playerchoice == 1:
    p = player(name, wizard)

if playerchoice == 2:
    p = player(name, elf)

if playerchoice == 3:
    p = player(name, human)

print(
    f"You have chosen {p.get_type_name()}, which has {p.get_hp()} hitpoints and deals {p.get_dmg()} damage.")

enemy = dragon

while True:     # ToDo create battle class

    enemy.receive_dmg(p.get_dmg())

    # ToDO create battle round func
    print(f"The {enemy.get_name()} takes {p.get_dmg()} damage from {p.get_name()} and has {enemy.get_hp()} hp remaining.")

    if(enemy.get_hp() <= 0):
        print(f"The {enemy.get_name()} has been defeated!!")
        break

    p.receive_dmg(enemy.get_dmg())
    # ToDO create battle round func
    print(f"{p.get_name()} takes {enemy.get_dmg()} damage from {enemy.get_name()} and has {p.get_hp()} hp remaining.")

    if(p.get_hp() <= 0):

        print(f"{p.get_name()} has been defeated!!")
        break
