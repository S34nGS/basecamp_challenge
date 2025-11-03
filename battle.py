import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_battle(p, e):
    print(f"""
Player health:  [{"#" * (p.health // 3)}]
Enemy health:   [{"#" * (e.health // 3)}]
    """)

    if len(p.inventory) == 0:
        print(f"""
1. Light attack: {p.light_attack_pp}
2. Heavy attack: {p.heavy_attack_pp}
3. Defend
        """)
    elif len(p.inventory) == 1:
        print(f"""
1. Light attack: {p.light_attack_pp}
2. Heavy attack: {p.heavy_attack_pp}
3. Defend
4. {p.inventory[0].name}
        """)

    player_choice = input("Choose an option: ")
    enemy_options = ["1", "2", "3"]
    enemy_choice = random.choice(enemy_options)

    clear()

    # The results of the player's choice
    # The player chose light attack
    if player_choice == "1":
        if p.light_attack_pp > 0:
            p.light_attack_pp -= 1
            if enemy_choice == "3" and e.defense > p.light_attack:
                print("The defense of the enemy is too strong")
            elif enemy_choice == "3" and e.defense < p.light_attack:
                e.health -= (p.light_attack - e.defense)
                print(f"You dealth {p.light_attack - e.defense} damage to the enemy")
            else:
                e.health -= p.light_attack
                print(f"You dealth {p.light_attack} damage to the enemy")
        else:
            print("You can't do that attack anymore")

    # The player chose heavy attack
    elif player_choice == "2":
        if p.heavy_attack_pp > 0:
            p.heavy_attack_pp -= 1
            if enemy_choice == "3" and e.defense > p.heavy_attack:
                print("The defense of the enemy is too strong")
            elif enemy_choice == "3" and e.defense < p.heavy_attack:
                e.health -= (p.heavy_attack - e.defense)
                print(f"You dealth {p.heavy_attack - e.defense} damage to the enemy")
            else:
                e.health -= p.heavy_attack
                print(f"You dealth {p.heavy_attack} damage to the enemy")
        else:
            print("You can't do that attack anymore")
    
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

    # The player chose to use the weapon
    elif player_choice == "4" and len(p.inventory) == 1:
        if p.inventory[0].durability > 0:
            # If the chosen weapon is a shuriken the amount of shurikens thrown is randomized between 1 and 3
            if p.inventory[0].name == "Shuriken":
                randomized_number = random.randint(1, 3)
                shuriken_damage = p.inventory[0].damage * randomized_number
                p.inventory[0].durability -= randomized_number
                print(f"You threw {randomized_number} shurikens")
                if enemy_choice == "3" and e.defense > shuriken_damage:
                    print("The defense of the enemy is too strong")
                elif enemy_choice == "3" and e.defense < shuriken_damage:
                    e.health -= (shuriken_damage - e.defense)
                    print(f"You dealth {shuriken_damage - e.defense} damage to the enemy")
                else:
                    e.health -= shuriken_damage
                    print(f"You dealth {shuriken_damage} damage to the enemy")
            
            # If a weapon besides the shuriken was chosen the logic goes on normally
            else:
                p.inventory[0].durability -= 1
                if enemy_choice == "3" and e.defense > p.inventory[0].damage:
                    print("The defense of the enemy is too strong")
                elif enemy_choice == "3" and e.defense < p.inventory[0].damage:
                    e.health -= (p.inventory[0].damage - e.defense)
                    print(f"You dealth {p.inventory[0].damage - e.defense} damage to the enemy")
                else:
                    e.health -= p.inventory[0].damage
                    print(f"You dealth {p.inventory[0].damage} damage to the enemy")

        else:
            # When the durability of a weapon reaches 0 the weapon gets removed from inventory
            p.inventory.pop(0)
            print("Your weapon broke")

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
        return "Lose"
    elif e.health <= 0:
        return "Win"