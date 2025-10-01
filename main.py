import os

playing = False

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

print("""
Welcome to Prison Escape!
""")

# Give the option of starting the game
while True:
    start_choice = input('Do you want to start the game Y/n: ')
    start_choice_lower = start_choice.strip().lower()
    if start_choice_lower == 'n':
        clear()
        print('Goodbye!')
        break
    elif start_choice_lower in ('y', ''):
        clear()
        playing = True
        break
    else:
        print('Choose a valid option')


while playing:
    print("""
You wake up confused.
Your eyes slowly open...
Around you is a prison...
Why???

You have to escape!
    """)
    a = input("a")