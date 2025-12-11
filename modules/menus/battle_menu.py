import random
import textwrap
from modules.menus.selection_menu import selection_menu
from modules.clear import clear
from modules.battle_move import battle_move
from modules.health_bar import health_bar
from classes.negotiation import Negotiation
from classes.player import Player
from classes.enemy import Enemy


def battle_menu(player: Player, enemy: Enemy):
    while True:
        if len(player.inventory) == 0:
            menu_items = (
                f"Light attack: {player.light_attack_pp}/{player.max_light_attack_pp}",
                f"Heavy attack: {player.heavy_attack_pp}/{player.max_heavy_attack_pp}",
                "Defend",
                "Negotiate"
            )
        elif len(player.inventory) == 1:
            menu_items = (
                f"Light attack: {player.light_attack_pp}/{player.max_light_attack_pp}",
                f"Heavy attack: {player.heavy_attack_pp}/{player.max_heavy_attack_pp}",
                "Defend",
                "Negotiate",
                f"{player.inventory[0].name}: {player.inventory[0].durability}"
            )
        menu_text = textwrap.dedent(f"""
        {player.name}'s health:   {health_bar(player.health, player.max_health, player.max_health // 3)}
        Enemy health:   {health_bar(enemy.health, enemy.max_health, enemy.max_health // 3)}
        """)
        selected = selection_menu(menu_items, menu_text)
        enemy_options = ["1", "2", "3"]
        enemy_choice = random.choice(enemy_options)

        clear()

        move = battle_move(player, enemy, selected, enemy_choice)
        if move == "negotiation":
            Negotiation.menu(player, enemy)
            continue

        if player.health <= 0:
            return "Lose"
        elif enemy.health <= 0:
            return "Win"
