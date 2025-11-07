from modules.clear import clear
import textwrap


def menu():
    while True:
        print(textwrap.dedent("""
            ----------------------------
                    PRISON ESCAPE
            ----------------------------
                    1. Start
                    2. Info
                    3. Exit
        """))
        choice = input("Enter a number: ")

        if choice == "1":
            clear()
            return "start"
        elif choice == "2":
            clear()
            print(textwrap.dedent("""
                The game is about a person who gets stuck in prison.
                Throughout the game you'll encounter enemies and decisions that will ensure or ruin your escape.

                If you manage to beat everyone you'll achieve your goal of freedom.

                Or will you...
            """))
        elif choice == "3":
            clear()
            print('You left the game.')
            return "exit"
        else:
            clear()
            print("Choice was invalid, try again.")

if __name__ == "__main__":
    menu()