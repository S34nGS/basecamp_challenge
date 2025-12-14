from modules.clear import clear
from modules.menus.selection_menu import selection_menu
from modules.health_bar import health_bar
import textwrap


class Negotiation:
    def __init__(self, ):
        pass

    def menu(player, enemy):
        menu_items = (
            "Befriend",
            "Buy out",
            "Lie",
            "Charm",
            "Back"
        )
        while True:
            menu_text = textwrap.dedent(f"""
            {player.name}'s health:   {health_bar(player.health, player.max_health, player.max_health // 3)}
            Enemy health:   {health_bar(enemy.health, enemy.max_health, enemy.max_health // 3)}
            """)
            selected = selection_menu(menu_items, menu_text)
            if menu_items[selected] == "Befriend":
                if player.stats[1] > (enemy.stats[1] // 2 + 3):
                    ...
                else:
                    return "not possible"
            elif menu_items[selected] == "Buy out":
                ...
            elif menu_items[selected] == "Lie":
                ...
            elif menu_items[selected] == "Charm":
                ...
            elif menu_items[selected] == "Back":
                break
