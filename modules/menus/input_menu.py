from modules.clear import clear
from readchar import key, readkey


def input_menu(player):
    menu = (
        "Done",
        "Back"
    )
    for index in range(len(menu)):
        selected = 0
        name = ""
        while True:
            clear()
            print("Enter your name")
            print(f"Name: {name}")
            longest = len(max(menu, key=len))
            print(f"╔{'═' * (longest + 4)}╗")
            for index in range(len(menu)):
                if index == selected:
                    print(f"║> {menu[index]} {' ' * (longest - len(menu[index]))}<║")
                else:
                    print(f"║  {menu[index]} {' ' * (longest - len(menu[index]))} ║")
            print(f"╚{'═' * (longest + 4)}╝")

            pressed = readkey()

            if pressed == key.DOWN and selected < len(menu) - 1:
                selected += 1
            elif pressed == key.UP and selected > 0:
                selected -= 1
            elif pressed == key.ENTER:
                if selected == 0:
                    player.name = name
                    return "continue"
                elif selected == 1:
                    return "back"
            elif len(pressed) == 1 and pressed.isprintable():
                name += pressed
