def pokemon_binder_manager():
    print("Hey there! Welcome to the Pokémon Card Binder Manager!\n")
    print("What would you like to do today?")
    print("1. Add a Pokémon Card")
    print("2. Reset the whole Binder")
    print("3. View what’s inside the Binder")
    print("4. Exit the program\n")

    binder = {}
    max_pokedex = 1025
    cards_per_page = 64
    rows = 8
    columns = 8
    keep_going = True

    while keep_going:
        user_input = input("Pick an option (1-4): ")
        if not user_input.isdigit():
            print("Oops! That wasn't a number. Try typing 1, 2, 3, or 4.\n")
            continue

        choice = int(user_input)

        if choice == 1:
            pokedex_input = input("Enter the Pokedex Number of the card (from 1 to 1025): ")

            if not pokedex_input.isdigit():
                print("Hmm... that doesn't look like a number.\n")
                continue

            pokedex = int(pokedex_input)

            if pokedex < 1 or pokedex > max_pokedex:
                print("That number is out of bounds! You can only add cards from #1 to #1025.\n")
                continue

            if pokedex in binder:
                info = binder[pokedex]
                print(f"Whoa! You already added that one. It's on Page {info[0]}, Row {info[1]+1}, Column {info[2]+1}.\n")
            else:
                index = pokedex - 1
                page = index // cards_per_page + 1
                spot = index % cards_per_page
                row = spot // columns
                col = spot % columns
                binder[pokedex] = (page, row, col)
                print(f"Awesome! You added Pokémon #{pokedex} to your binder.")
                print(f"It goes on Page {page}, Row {row+1}, Column {col+1}.\n")

        elif choice == 2:
            print("Are you REALLY sure you want to delete everything?")
            confirm = input("Type 'confirm' to wipe the binder, or anything else to cancel: ").lower().strip()
            if confirm == "confirm":
                binder.clear()
                print("All gone! Your binder is now empty.\n")
            else:
                print("Phew! That was close. Binder is safe.\n")

        elif choice == 3:
            print("Here's what's inside your binder right now:")
            print("-" * 30)
            if len(binder) == 0:
                print("Uh-oh... your binder is empty. Better start adding cards!\n")
            else:
                for pokedex_num in sorted(binder):
                    page, row, col = binder[pokedex_num]
                    print(f"Pokémon #{pokedex_num} is on Page {page}, Row {row+1}, Column {col+1}")
                print("-" * 30)
                total = len(binder)
                percent = total / max_pokedex * 100
                print(f"Total Cards: {total}")
                print(f"Completion: {percent:.2f}%")
                if total == max_pokedex:
                    print("WOW! You really caught them all!\n")
                else:
                    print("Keep going! You're doing great!\n")

        elif choice == 4:
            print("Thanks for using the Pokémon Card Binder Manager. See you next time!")
            keep_going = False

        else:
            print("Hmm... that's not a valid option. Try picking 1, 2, 3, or 4.\n")

# Run the program
pokemon_binder_manager()
