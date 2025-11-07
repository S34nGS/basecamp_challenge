import random

# TODO pp doesn't go down because player_pp is a local variable instead of the actual object data


def battle_move(player, enemy, player_choice: str, enemy_choice: str) -> None:
    player_dict = {
        "1": [player.light_attack, player.light_attack_pp],
        "2": [player.heavy_attack, player.heavy_attack_pp],
        "3": player.defense
    }
    enemy_dict = {
        "1": enemy.light_attack,
        "2": enemy.heavy_attack,
        "3": enemy.defense
    }

    # Add the weapon to the inventory
    if len(player.inventory) == 1:
        player_dict["4"] = [player.inventory[0].damage, player.inventory[0].durability]

    if player_choice in player_dict.keys():
        player_move = player_dict.get(player_choice)
        if player_choice != "3":
            player_attack = player_move[0]
            player_pp = player_move[1]
            weapon_attack = player_move[0]
            weapon_durability = player_move[1]

        enemy_move = enemy_dict.get(enemy_choice)

        if isinstance(player_move, list):  # Player chooses an attack
            if player_pp > 0:
                player_pp -= 1
                if enemy_choice == "3" and enemy_move > player_attack:
                    print("The defense of the enemy is too strong")
                elif enemy_choice == "3" and enemy_move < player_attack:
                    enemy.health -= (player_attack - enemy_move)
                    print(f"You dealth {player_attack - enemy_move} damage to the enemy")
                else:
                    player.health -= enemy_move
                    enemy.health -= player_attack
                    print(f"You dealth {player_attack} damage to the enemy")
                    print(f"The enemy dealth {enemy_move} damage to you")
            elif player_choice == "4":  # Player uses weapon to attack
                if player.inventory[0].durability > 0:
                    # If the chosen weapon is a shuriken the amount of shurikens thrown is randomized between 1 and 3
                    if player.inventory[0].name == "Shuriken":
                        randomized_number = random.randint(1, 3)
                        shuriken_damage = weapon_attack * randomized_number
                        weapon_durability -= randomized_number
                        print(f"You threw {randomized_number} shurikens")
                        if enemy_choice == "3" and enemy_move > shuriken_damage:
                            print("The defense of the enemy is too strong")
                        elif enemy_choice == "3" and enemy_move < shuriken_damage:
                            enemy.health -= (shuriken_damage - enemy_move)
                            print(f"You dealth {shuriken_damage - enemy_move} damage to the enemy")
                        else:
                            enemy.health -= shuriken_damage
                            print(f"You dealth {shuriken_damage} damage to the enemy")

                    # If a weapon besides the shuriken was chosen the logic goes on normally
                    else:
                        weapon_durability -= 1
                        if enemy_choice == "3" and enemy_move > weapon_attack:
                            print("The defense of the enemy is too strong")
                        elif enemy_choice == "3" and enemy_move < weapon_attack:
                            enemy.health -= (weapon_attack - enemy_move)
                            print(f"You dealth {weapon_attack - enemy_move} damage to the enemy")
                        else:
                            enemy.health -= weapon_attack
                            print(f"You dealth {weapon_attack} damage to the enemy")
                else:
                    # When the durability of a weapon reaches 0 the weapon gets removed from inventory
                    player.inventory.pop(0)
                    player_dict.pop("4")
                    print("Your weapon broke")
            else:
                print("You can't do that attack anymore")
        else:  # Player chooses to defend
            if enemy_choice != "3" and player_move > enemy_move:
                print("Your defense is too strong for the enemy")
            elif enemy_choice != "3" and player_move < enemy_move:
                player.health -= (enemy_move - player_move)
                print(f"The enemy dealth {enemy_move - player_move} damage to you")
            else:
                print("You chose to defend")
    else:
        print("Pick a valid option")
