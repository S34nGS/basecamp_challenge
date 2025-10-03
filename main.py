import os

playing = False

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()


# Main menu
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



# Running game
while playing:
   
    a = input("a")