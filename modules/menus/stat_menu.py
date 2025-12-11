from modules.menus.selection_menu import selection_menu
import textwrap


def stat_menu(player):
    menu_items = (
        f"Intelligence  [{player.stats[0]}]",
        f"Charisma      [{player.stats[1]}]",
        f"Deception     [{player.stats[2]}]",
        f"Anger         [{player.stats[3]}]",
        "Reset",
        "Continue",
        "Back"
    )

    while True:
        menu_text = textwrap.dedent(f"""
        Allocate stat points
        Available: {player.stat_points}
        """)
        selected = selection_menu(menu_items, menu_text)
        if menu_items[selected] == "Reset":
            player.stats = [5, 5, 5, 5]
            player.stat_points = 10
        elif menu_items[selected] == "Continue":
            return "done"
        elif menu_items[selected] == "Back":
            return "back"
        else:
            if player.stat_points > 0:
                player.stats[selected] += 1
                player.stat_points -= 1
                print(f"You selected: {menu_items[selected]}")
            else:
                print("All stat points have been used")
        break
