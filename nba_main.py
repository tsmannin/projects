from pathlib import Path

def nba_options():
    print("1. Conference")
    print("2. Team")
    print("3. Player")
    print("4. Quit")
    choice = int(input())
    return choice


def process_stats(choice):
    if choice == 1:
        #print conference stats here
    elif choice == 2:
        #print team stats here
    elif choice == 3:
        #print player stats here
    elif choice == 4:
        pass

def process_csv_creation(choice):
    if choice == 1:
        #create csv file for conference
    elif choice == 2:
        #create csv file for team
    elif choice == 3:
        #create csv file for player
    elif choice == 4:
        pass

def store_file():
    savedir = Path(input("Enter the directory you want to save in."))
    if not savedir.exists():
        savedir.mkdir()

    file_name = input("What is the name of the file you want to store? (include the extension)")




def main():
    print("Hi. Welcome to our NBA stats filing system. What would you like to do?")
    print("1. Get stats")
    print("2. Create csv files")
    print("3. Update csv files")
    print("4. Quit")
    choice = int(input())
    if choice == 1:
        print("What kind of stats would you like?")
        choice = nba_options()
    elif choice == 2:
        print("What kind of csv file do you want to create?")
        choice = nba_options()
    elif choice == 3:
        #we need to find out what we want to update
        print("Please provide the csv file you want to update.")
    elif choice == 4:
        pass




if __name__ == "__main__":
    main()