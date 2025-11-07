from modules.clear import clear
import textwrap

# TODO weapon_decision can be empty and the story will continue

def medic_or_armory(decision, player, rock, shuriken, knife):
    if decision == "left":
        clear()
        player.health = 100
        print("You have regained your full health")
    elif decision == "right":
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
        clear()
        print("Pick either left or right")
        return "invalid"
