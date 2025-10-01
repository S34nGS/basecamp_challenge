import os

playing = False

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

# print("""
# Welcome to Prison Escape!
# """)

# # Give the option of starting the game
# while True:
#     start_choice = input('Do you want to start the game Y/n: ')
#     start_choice_lower = start_choice.strip().lower()
#     if start_choice_lower == 'n':
#         clear()
#         print('Goodbye!')
#         break
#     elif start_choice_lower in ('y', ''):
#         clear()
#         playing = True
#         break
#     else:
#         print('Choose a valid option')



while True:
    print("""
----------------------------
        PRISON ESCAPE  
----------------------------
        1. Start
        2. Info
        3. Exit
    """)
    choice = input("Type een nummer in: ")

    if choice == "1":
        clear()
        playing = True
        break
    elif choice == "2":
        clear()
        print("""
Het spel gaat over een persoon die vastzit in een gevangenis.
Het doel is om een aantal levels te voltooien en 
om vijanden die je tegenkomt in de gevangenis te verslaan. 
Waardoor je uitenedlijk kunt onstnappen 
        """)
    elif choice == "3":
        clear()
        print('Je hebt het spel verlaten.')
        break
    else:
        clear()
        print("Keuze is niet valide, probeer opnieuw.")


while playing:
    print("""
You wake up confused.
Your eyes slowly open...
Around you is a prison...
Why???

You have to escape!
    """)
    a = input("a")