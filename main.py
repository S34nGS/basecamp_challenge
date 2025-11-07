from tools.clear import clear
from tools.menu import menu
from battle import run_battle
import textwrap
import story

# Import classes
from classes.player import Player
from classes.enemy import Enemy
from classes.weapon import Weapon

# Player
player = Player(100, 20, 5, 30, 15, 30, [])

# Weapons
knife = Weapon("Knife", 50, 5)
rock = Weapon("Rock", 30, 20)
shuriken = Weapon("Shuriken", 15, 20)

# Enemies
enemy1 = Enemy(100, 20, 5, 30)
enemy2 = Enemy(150, 30, 10, 50)
enemies = [enemy1, enemy2]

# Clean terminal for start of game
clear()

def main():
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
            print(story.storyline[story_step])
            next = input("Press enter to continue")
            if next == "":
                clear()
                story_step += 1
                if story_step == 5 or story_step == 10:
                    battle = True
                    playing = False
                elif story_step == 8:
                    left_right_decision = input("Do you pick left(medic) or right(armory): ").lower()
                    if left_right_decision == "left":
                        clear()
                        player.health = 100
                        print("You have regained your full health")
                    elif left_right_decision == "right":
                        clear()
                        print(textwrap.dedent("""
                            You have the choice between three different weapons: Rock, Shuriken, Knife.

                            Choose wisely as some weapons do more damage but may degrade faster.
                        """))
                        weapon_decision = input("I choose: ").lower()
                        clear()
                        if weapon_decision == "rock":
                            player.inventory.append(rock)
                            print("You grabbed the rock.")
                        elif weapon_decision == "shuriken":
                            player.inventory.append(shuriken)
                            print("You grabbed the shuriken.")
                        elif weapon_decision == "knife":
                            player.inventory.append(knife)
                            print("You grabbed the knife.")
                        else:
                            print("Make a valid decision")
                    else:
                        story_step = 7
                        clear()
                        print("Pick a valid option")

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