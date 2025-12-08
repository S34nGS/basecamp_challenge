# Import modules
from modules.clear import clear
from modules.menus.stat_menu import stat_menu
from modules.menus.main_menu import menu
from modules.menus.new_or_load_menu import new_or_load_menu
from modules.menus.battle_menu import battle_menu
from modules.medic_or_armory import medic_or_armory

# Import story and battle loops
from story import storyline
# from battle import run_battle

# Import classes
from classes.player import Player
from classes.enemy import Enemy
from classes.weapon import Weapon

# Player
player = Player(100, 100, 20, 5, 15, 15, 15, 30, 30, [], [5, 5, 5, 5], 10)

# Enemies
enemy1 = Enemy(100, 100, 20, 5, 30, [6, 6, 6, 6])
enemy2 = Enemy(150, 150, 30, 10, 50, [7, 7, 7, 7])
enemies = [enemy1, enemy2]

# Weapons
knife = Weapon("Knife", 50, 5, 5)
rock = Weapon("Rock", 30, 20, 20)
shuriken = Weapon("Shuriken", 15, 20, 20)


def main():
    while True:
        # Clean terminal for start of game
        clear()

        # Game variables
        main_menu = True
        character_creation = False
        playing = False
        new_or_load = False
        battle = False
        story_step = 0
        enemy_step = 0

        # Main menu
        while main_menu:
            choice = menu()
            if choice == "start":
                new_or_load = True
                main_menu = False
            elif choice == "exit":
                break

        # New or load menu loop
        while new_or_load:
            nol = new_or_load_menu()
            if nol == "new":
                clear()
                player_name = input("What is your name: ")
                player.name = player_name
                character_creation = True
                new_or_load = False
            elif nol == "load":
                clear()
                playing = True
                new_or_load = False
            elif nol == "back":
                main_menu = True
                new_or_load = False

        # Character creation loop
        while character_creation:
            stats = stat_menu(player)
            if stats == "done":
                clear()
                character_creation = False
                playing = True

        # Storyline loop
        while playing:
            print(storyline[story_step])
            next = input("Press enter to continue")
            if next == "":
                clear()
                story_step += 1
                if story_step == 5 or story_step == 10:
                    battle = True
                    playing = False
                elif story_step == 8:
                    left_right_decision = input("Do you pick medic(left) or armory(right): ").lower()
                    result = medic_or_armory(left_right_decision, player, rock, shuriken, knife)
                    if result == "invalid":
                        story_step = 7
                        clear()
                        print("Pick either left or right")
            else:
                clear()

        # Battle loop
        while battle:
            battle_menu(player, enemies[enemy_step])
            if battle_menu(player, enemies[enemy_step]) == "Win":
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
            elif battle_menu(player, enemies[enemy_step]) == "Lose":
                clear()
                print("You died :(")
                break


if __name__ == "__main__":
    main()
