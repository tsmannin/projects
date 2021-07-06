# import main.py as m, then when calling functions use m.function_call()

def menu():
    print("""
|==============================================================|
|   .______     ______   ___   ___  __  .__   __.   _______    |
|   |   _  \   /  __  \  \  \ /  / |  | |  \ |  |  /  _____|   |
|   |  |_)  | |  |  |  |  \  V  /  |  | |   \|  | |  |  __     |
|   |   _  <  |  |  |  |   >   <   |  | |  . `  | |  | |_ |    |
|   |  |_)  | |  `--'  |  /  .  \  |  | |  |\   | |  |__| |    |
|   |______/   \______/  /__/ \__\ |__| |__| \__|  \______|    |
|                                                              |
|==============================================================|
""")
    print("Hi. Welcome to our boxing database. What would you like to do?")
    print("1. Modify data")
    print("2. Generate graph")
    print("3. Display all boxers")
    print("4. Look up information")
    print("5. Quit")
    print()

def modify():
    print()
    print("1. Add")
    print("2. Delete")
    print("3. Update")
    print("4. Quit")
    print()
    choice = int(input())
    return choice

def look_up():
    print()
    print("What do you want to look up?")
    print("1. Boxer")
    print("2. Events")
    print("3. Quit")
    print()
    choice = int(input())
    return choice

def interface():
    menu()
    choice = int(input())
    quit = False
    while choice != 5:
        if choice == 1:
            choice = modify()
            if choice == 4:
                quit = True
                choice = 5
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            choice = look_up()
            if choice == 3:
                quit = True
                choice = 5
        else:
            print("Sorry, invalid input. Try again.")
        if not quit:
            menu()
            choice = int(input())
    if choice == 5:
        print("Goodbye!")



def main():
    interface()




if __name__ == "__main__":
    main()
