def homescreen_shown():
   while True:
       print("----------------------------")
       print("      HOME SCREEN    ")
       print("----------------------------")
       print("       1. Start      ")
       print("       3. Exit       ")
       print("       5. Info       ")
       choice = input("Type een nummer in: ")
       if choice == "1":
           
           return
       elif choice == "3":
           print('Je hebt het spel verlaten.')
           exit()
       elif choice == "5":
           print("""Het spel gaat over een persoon die vastzit in een gevangenis.
                    Het doel is om een aantal levels te voltooien en 
                    om vijanden die je tegenkomt in de gevangenis te verslaan. 
                    Waardoor je uitenedlijk kunt onstnappen """)
       else:
           print("Keuze is niet valide, probeer opnieuw.")


homescreen_shown()