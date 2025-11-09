# Import modules
from modules.clear import clear
from modules.menu import menu
from modules.medic_or_armory import medic_or_armory

# Import story and battle loops
from story import storyline
from battle import run_battle

# Import classes
from classes.player import Player
from classes.enemy import Enemy
from classes.weapon import Weapon

# Player
player = Player(100, 20, 5, 15, 15, 30, [])

# Enemies
enemy1 = Enemy(100, 20, 5, 30)
enemy2 = Enemy(150, 30, 10, 50)
enemies = [enemy1, enemy2]

# Weapons
knife = Weapon("Knife", 50, 5)
rock = Weapon("Rock", 30, 20)
shuriken = Weapon("Shuriken", 15, 20)


def main():
    # Clean terminal for start of game
    clear()

    # Game variables
    playing = False
    battle = False
    story_step = 0
    enemy_step = 0

    # Main menu
    while True:
        choice = menu()
        if choice == "start":
            playing = True
            break
        elif choice == "exit":
            break

    # Main game loop
    while True:
        # Storyline loop
        if playing:
            print(storyline[story_step])
            next = input("Press enter to continue")
            if next == "":
                clear()
                story_step += 1
                if story_step == 5 or story_step == 10:
                    battle = True
                    playing = False
                elif story_step == 8:
                    left_right_decision = input("Do you pick left(medic) or right(armory): ").lower()
                    result = medic_or_armory(left_right_decision, player, rock, shuriken, knife)
                    if result == "invalid":
                        story_step = 7
                        clear()
                        print("Pick either left or right")
            else:
                clear()

        # Battle loop
        elif battle:
            run_battle(player, enemies[enemy_step])
            if run_battle(player, enemies[enemy_step]) == "Win":
                clear()
                print("You have beaten the enemy")
                print("")
                next = input("Press enter to continue")
                if next == "":
                    clear()
                    enemy_step += 1
                    playing = True
                    battle = False
                else:
                    clear()
            elif run_battle(player, enemies[enemy_step]) == "Lose":
                clear()
                print("You died :(")
                break

        else:
            break


if __name__ == "__main__":
    main()
