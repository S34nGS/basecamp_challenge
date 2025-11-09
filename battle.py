import random
import textwrap
from modules.clear import clear
from modules.battle_move import battle_move


def run_battle(player, enemy):
    print(textwrap.dedent(f"""
        Player health:  [{"#" * (player.health // 3)}]
        Enemy health:   [{"#" * (enemy.health // 3)}]
    """))

    if len(player.inventory) == 0:
        print(textwrap.dedent(f"""
            1. Light attack: {player.light_attack_pp}
            2. Heavy attack: {player.heavy_attack_pp}
            3. Defend
        """))
    elif len(player.inventory) == 1:
        print(textwrap.dedent(f"""
            1. Light attack: {player.light_attack_pp}
            2. Heavy attack: {player.heavy_attack_pp}
            3. Defend
            4. {player.inventory[0].name}: {player.inventory[0].durability}
        """))

    player_choice = input("Choose an option: ")
    enemy_options = ["1", "2", "3"]
    enemy_choice = random.choice(enemy_options)

    clear()

    battle_move(player, enemy, player_choice, enemy_choice)

    if player.health <= 0:
        return "Lose"
    elif enemy.health <= 0:
        return "Win"
