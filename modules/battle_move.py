from classes.negotiation import Negotiation
# TODO Add special attack?


def battle_move(player, enemy, player_choice: str, enemy_choice: str) -> None:
    if player_choice == "1":
        player.attack(enemy, enemy_choice, "light")
        enemy.attack(player, player_choice, enemy_choice)
    elif player_choice == "2":
        player.attack(enemy, enemy_choice, "heavy")
        enemy.attack(player, player_choice, enemy_choice)
    elif player_choice == "3":
        player.defend(enemy, enemy_choice)
        enemy.attack(player, player_choice, enemy_choice)
    elif player_choice == "4":
        # TODO Fix negotiation logic. with return something and then give the menu
        Negotiation.menu()
    elif player_choice == "5" and len(player.inventory) > 0:
        player.weapon(enemy, enemy_choice, 0)
        enemy.attack(player, player_choice, enemy_choice)
    else:
        print("Pick a valid option")
