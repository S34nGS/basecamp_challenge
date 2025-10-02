import random
import os

battle = False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_battle(p, e):
    print("""
        1. Light attack
        2. Heavy attack
        3. Defend
    """)
    print(f"""
        Player health:  {p.health}
        Enemy health:   {e.health}
    """)

    player_choice = input("Choose an option: ")
    enemy_options = ["1", "2", "3"]
    enemy_choice = random.choice(enemy_options)

    clear()

    # The results of the player's choice
    # The player chose light attack
    if player_choice == "1":
        if enemy_choice == "3" and e.defense > p.light_attack:
            print("The defense of the enemy is too strong")
        elif enemy_choice == "3" and e.defense < p.light_attack:
            e.health -= (p.light_attack - e.defense)
            print(f"You dealth {p.light_attack - e.defense} damage to the enemy")
        else:
            e.health -= p.light_attack
            print(f"You dealth {p.light_attack} damage to the enemy")

    # The player chose heavy attack
    elif player_choice == "2":
        if enemy_choice == "3" and e.defense > p.heavy_attack:
            print("The defense of the enemy is too strong")
        elif enemy_choice == "3" and e.defense < p.heavy_attack:
            e.health -= (p.heavy_attack - e.defense)
            print(f"You dealth {p.heavy_attack - e.defense} damage to the enemy")
        else:
            e.health -= p.heavy_attack
            print(f"You dealth {p.heavy_attack} damage to the enemy")
    
    # The player chose to defend
    elif player_choice == "3":
        if enemy_choice == "1" and p.defense > e.light_attack:
            print("Your defense is too strong for the enemy")
        elif enemy_choice == "1" and p.defense < e.light_attack:
            p.health -= e.light_attack
            print(f"The enemy dealth {e.light_attack - p.defense} damage to you")
        
        if enemy_choice == "2" and p.defense > e.heavy_attack:
            print("Your defense is too strong for the enemy")
        elif enemy_choice == "2" and p.defense < e.heavy_attack:
            p.health -= e.heavy_attack
            print(f"The enemy dealth {e.heavy_attack - p.defense} damage to you")
        
        if enemy_choice == "3":
            print("You chose to defend")

    else:
        print("Pick a valid option")


    # The results of the enemy's choice
    # The enemy chose light attack
    if enemy_choice == "1":
        if player_choice == "3" and p.defense > e.light_attack:
            print("Your defense is too strong for the enemy")
        elif player_choice == "3" and p.defense < e.light_attack:
            p.health -= (e.light_attack - p.defense)
            print(f"The enemy dealth {e.light_attack - p.defense} damage to you")
        else:
            p.health -= e.light_attack
            print(f"The enemy dealth {e.light_attack} damage to you")
    
    # The enemy chose heavy attack
    elif enemy_choice == "2":
        if player_choice == "3" and p.defense > e.heavy_attack:
            print("Your defense is too strong for the enemy")
        elif player_choice == "3" and p.defense < e.heavy_attack:
            p.health -= (e.heavy_attack - p.defense)
            print(f"The enemy dealth {e.heavy_attack - p.defense} damage to you")
        else:
            p.health -= e.heavy_attack
            print(f"The enemy dealth {e.heavy_attack} damage to you")

    # The enemy chose to defend
    elif player_choice == "3":
        if enemy_choice == "1" and e.defense > p.light_attack:
            print("The defense of the enemy is too strong")
        elif enemy_choice == "1" and e.defense < p.light_attack:
            p.health -= p.light_attack
            print(f"You dealth {p.light_attack - e.defense} damage to the enemy")
        
        if enemy_choice == "2" and e.defense > p.heavy_attack:
            print("The defense of the enemy is too strong")
        elif enemy_choice == "2" and e.defense < p.heavy_attack:
            p.health -= p.heavy_attack
            print(f"You dealth {p.heavy_attack - e.defense} damage to the enemy")
        
        if enemy_choice == "3":
            print("The enemy chose to defend")

    if p.health <= 0:
        clear()
        print("You died :(")
        return False
    elif e.health <= 0:
        clear()
        print("You have beaten the enemy")
        return False