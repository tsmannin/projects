import csv
import sqlite3 as sq
import matplotlib
matplotlib.use("Agg") # so that we don't need GUI
import matplotlib.pyplot as plt
import look_up as l
import display as d
import modify as m
import random
def connect():
    #connect to the databse
    conn = sq.connect("UFC.sqlite")
    #create a cursor to the database
    curr = conn.cursor()
    return conn,curr
"""
create_db creates the databases
"""
def getWinner(lis1,lis2):
    sum1 = 0
    sum2 = 0
    for i in range(0 , 6):
        sum1 += lis1[i]
        sum2 += lis2[i]
    sums = [sum1,sum2]
    for i in range(2):
        if i > 1300:
            sums[i] = sums[i] * random.randint(5,10)
        elif i > 1000:
            sums[i] = sums[i] * random.randint(4,10)
        elif i > 800:
            sums[i] = sums[i] * random.randint(3,10)
        elif i > 500:
            sums[i] = sums[i] * random.randint(2,10)
        else:
            sums[i] = sums[i] * random.randint(1,10)

    if sums[0] > sums[1]:
        return 0
    elif sums[1] > sums[0]:
        return 1
    else:
        return 1

def compute_competition(conn,cur):
    print("\nWhat competition do you want to see the results of? ")
    print("1. Mens Heavyweights")
    print("2. Mens Middleweights")
    print("3. Womens Bantamweight")
    print("4. Womens Strawweight")
    while True:
        try:
            i = int(input())
        except ValueError:
            print("please enter one of the options")
        else:
            if i > 4:
                print("please enter a valid number")
            else:
                break

    if i == 1:
        data = "Mens_Heavyweights"
    elif i == 2:
        data = "Mens_Middleweights"
    elif i == 3:
        data = "Womens_Bantamweight"
    elif i == 4:
        data = "Womens_Strawweight"



    cmd = """SELECT * FROM {}""".format(data)
    cur.execute(cmd)
    fighters = cur.fetchall()

    cmd = """SELECT Competitions.start_time, competitions.date
            FROM Competitions
            WHERE Competitions.event = ?"""
    cur.execute(cmd,(data,))
    competitions = cur.fetchall()

    if len(fighters) >= 16:
        i = 0
        j = 0
        winner = 0
        winner_list = []
        print(fighters)
        print("\n\n\n\t\tRound of 16:\n\n")
        while(i < len(fighters)):
            print("\t\tStarts at:",competitions[j][0])
            winner = getWinner(fighters[i][7:13],fighters[i+1][7:13])
            print(fighters[i][0])
            print("    vs.               The winner is {}".format(fighters[winner + i][0]))
            print(fighters[i+1][0])
            winner_list.append(fighters[winner + i])
            i += 2
            j += 1


        i = 0
        print("\n\n\n\t\tNext Round: Quarter Finals\n\n")
        other_list = []
        while(i < len(winner_list)):
            print("\t\tStarts at:",competitions[j][0])
            winner = getWinner(winner_list[i][7:13],winner_list[i+1][7:13])
            print(winner_list[i][0])
            print("    vs.               The winner is {}".format(winner_list[winner + i][0]))
            print(winner_list[i+1][0],"\n")
            other_list.append(winner_list[winner + i])
            i += 2
            j += 1
        i = 0
        print("\n\n\n\t\tNext Round: Semi Finals\n\n")

        other_list2 = []
        while(i < len(other_list)):
            print("\t\tStarts at:",competitions[j][0])
            winner = getWinner(other_list[i][7:13],other_list[i+1][7:13])
            print(other_list[i][0])
            print("    vs.               The winner is {}".format(other_list[winner + i][0]))
            print(other_list[i+1][0],"\n")
            other_list2.append(other_list[winner + i])
            i += 2
            j += 1


        i = 0
        print("\n\n\n\t\tNext Round: Finals\n\n")
        finalist = []
        while(i < len(other_list2)):
            print("\t\tStarts at:",competitions[j][0])
            winner = getWinner(other_list2[i][7:13],other_list2[i+1][7:13])
            print(other_list2[i][0])
            print("    vs.               The winner is {}".format(other_list2[winner + i][0]))
            print(other_list2[i+1][0],"\n")
            finalist.append(other_list2[winner + i])
            i += 2
            j += 1


        if winner == 0:
            finalist.append(other_list2[winner+1])
            cmd = """UPDATE Awards
                     SET winner = ?, id = ?
                     WHERE Awards.event = ? AND Awards.place = "First";"""
            cur.execute(cmd,(str(finalist[0][0]),int(finalist[0][4]),data,))
            conn.commit
            cmd = """UPDATE Awards
                     SET winner = ?, id = ?
                     WHERE Awards.event = ? AND Awards.place = "Second";"""
            cur.execute(cmd,(str(finalist[1][0]),int(finalist[1][4]),data,))
            conn.commit
        else:
            finalist.append(other_list2[winner - 1])
            cmd = """UPDATE Awards
                     SET winner = ?, id = ?
                     WHERE Awards.event = ? AND Awards.place = "First";"""
            cur.execute(cmd,(str(finalist[0][0]),int(finalist[0][4]),data,))
            conn.commit
            cmd = """UPDATE Awards
                     SET winner = ?, id = ?
                     WHERE Awards.event = ? AND Awards.place = "Second";"""
            cur.execute(cmd,(str(finalist[1][0]),int(finalist[1][4]),data,))
            conn.commit


    else:
        print("Sorry, Need to add ",str(16 -len(fighters))," fighters")



def fill_heavyweight_db(conn, cur):
    with open('Heavyweights.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        phone_number = 7144825333
        id_number = 5000001
        for i in reader:
            stats = []
            for j in header:
                stats.append(i[j])
            cmd = """
            INSERT INTO Mens_Heavyweights(
            name,
            age,
            sex,
            sponsor,
            ID,
            phone_number,
            fights,
            strikes,
            take_downs,
            knock_downs,
            reversals,
            submissions,
            strike_accuracy,
            take_down_accuracy
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """
            cur.execute(cmd,(stats[0],stats[1],'male',stats[2],id_number,phone_number,int(stats[3]),int(stats[4]),int(stats[6]),int(stats[8]),int(stats[9]),int(stats[10]),float(stats[5]),float(stats[7])))
            conn.commit
            phone_number += 3
            id_number += 1


def fill_middleweight_db(conn, cur):
    with open('middleweight.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        phone_number = 7145327921
        id_number = 4000001
        for i in reader:
            stats = []
            for j in header:
                stats.append(i[j])
            cmd = """
            INSERT INTO Mens_Middleweights(
            name,
            age,
            sex,
            sponsor,
            ID,
            phone_number,
            fights,
            strikes,
            take_downs,
            knock_downs,
            reversals,
            submissions,
            strike_accuracy,
            take_down_accuracy
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """
            cur.execute(cmd,(stats[0],stats[1],'male',stats[2],id_number,phone_number,int(stats[3]),int(stats[4]),int(stats[6]),int(stats[8]),int(stats[9]),int(stats[10]),float(stats[5]),float(stats[7])))
            conn.commit
            phone_number += 3
            id_number += 1

def fill_womens_bantamweight_db(conn, cur):
    with open('womensbantamweight.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        phone_number = 7145996090
        id_number = 3000001
        for i in reader:
            stats = []
            for j in header:
                stats.append(i[j])
            cmd = """
            INSERT INTO Womens_Bantamweight(
            name,
            age,
            sex,
            sponsor,
            ID,
            phone_number,
            fights,
            strikes,
            take_downs,
            knock_downs,
            reversals,
            submissions,
            strike_accuracy,
            take_down_accuracy
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """
            cur.execute(cmd,(stats[0],stats[1],'male',stats[2],id_number,phone_number,int(stats[3]),int(stats[4]),int(stats[6]),int(stats[8]),int(stats[9]),int(stats[10]),float(stats[5]),float(stats[7])))
            conn.commit
            phone_number += 3
            id_number += 1

def fill_womens_strawweight_db(conn, cur):
    with open('womenstrawweight.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        phone_number = 7143172612
        id_number = 2000001

        for i in reader:
            stats = []
            for j in header:
                stats.append(i[j])
            cmd = """
            INSERT INTO Womens_Strawweight(
            name,
            age,
            sex,
            sponsor,
            ID,
            phone_number,
            fights,
            strikes,
            take_downs,
            knock_downs,
            reversals,
            submissions,
            strike_accuracy,
            take_down_accuracy
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """
            cur.execute(cmd,(stats[0],stats[1],'male',stats[2],id_number,phone_number,int(stats[3]),int(stats[4]),int(stats[6]),int(stats[8]),int(stats[9]),int(stats[10]),float(stats[5]),float(stats[7])))
            conn.commit
            phone_number += 3
            id_number += 1

def fill_awards(conn,cur):
    with open('awards.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames

        for i in reader:
            stats = []
            for j in header:
                stats.append(i[j])
            cmd = """
            INSERT INTO Awards(winner,id,event,place,award)
            VALUES(?,?,?,?,?)
            """
            cur.execute(cmd,("None","None",str(stats[0]),stats[1],stats[2]))
            conn.commit

def fill_competitions(conn,cur):
    with open('competitions.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        for i in reader:
            stats = []
            for j in header:
                stats.append(i[j])
            cmd = """
            INSERT INTO Competitions(event,start_time,date,stage)
            VALUES(?,?,?,?)
            """
            cur.execute(cmd,(str(stats[0]),stats[1],stats[2],stats[3]))
            conn.commit

def create_db(conn, cur):
    cur.executescript("""
    DROP TABLE IF EXISTS Mens_Heavyweights;
    DROP TABLE IF EXISTS Mens_Middleweights;
    DROP TABLE IF EXISTS Womens_Bantamweight;
    DROP TABLE IF EXISTS Womens_Strawweight;
    DROP TABLE IF EXISTS Awards;
    DROP TABLE IF EXISTS Competitions;
    """)

    # create Tables
    create_tables = """
    CREATE TABLE Mens_Heavyweights(
        name TEXT,
        age TEXT,
        sex TEXT,
        sponsor TEXT,
        ID INTEGER UNIQUE,
        phone_number INTEGER UNIQUE,
        fights INTEGER,
        strikes INTEGER,
        take_downs INTEGER,
        knock_downs INTEGER,
        reversals INTEGER,
        submissions INTEGER,
        strike_accuracy REAL,
        take_down_accuracy REAL
        );
    CREATE TABLE Mens_Middleweights(
        name TEXT,
        age TEXT,
        sex TEXT,
        sponsor TEXT,
        ID INTEGER UNIQUE,
        phone_number INTEGER UNIQUE,
        fights INTEGER,
        strikes INTEGER,
        take_downs INTEGER,
        knock_downs INTEGER,
        reversals INTEGER,
        submissions INTEGER,
        strike_accuracy REAL,
        take_down_accuracy REAL
        );
    CREATE TABLE Womens_Bantamweight(
        name TEXT,
        age TEXT,
        sex TEXT,
        sponsor TEXT,
        ID INTEGER UNIQUE,
        phone_number INTEGER UNIQUE,
        fights INTEGER,
        strikes INTEGER,
        take_downs INTEGER,
        knock_downs INTEGER,
        reversals INTEGER,
        submissions INTEGER,
        strike_accuracy REAL,
        take_down_accuracy REAL
        );
    CREATE TABLE Womens_Strawweight(
        name TEXT,
        age TEXT,
        sex TEXT,
        sponsor TEXT,
        ID INTEGER UNIQUE,
        phone_number INTEGER UNIQUE,
        fights INTEGER,
        strikes INTEGER,
        take_downs INTEGER,
        knock_downs INTEGER,
        reversals INTEGER,
        submissions INTEGER,
        strike_accuracy REAL,
        take_down_accuracy REAL
        );
    CREATE TABLE Awards(
        winner TEXT,
        id INTEGER,
        event TEXT,
        place TEXT,
        award TEXT
    );
    CREATE TABLE Competitions(
        event TEXT,
        start_time TEXT,
        date TEXT,
        stage TEXT
    )
    """
    cur.executescript(create_tables)
    conn.commit


def menu():
    print("\n1. Modify data")
    print("2. Generate graph")
    print("3. Display all fighters")
    print("4. Look up information")
    print("5. Compute Cometiton")
    print("6. Many To Many Relatioinships")
    print("7. Quit")
    print()

def modify(conn,cur):
    # print()
    # print("1. Add Fighter")
    # print("2. Delete Fighter")
    # print("3. Update Stats or Info")
    # print("4. Quit")
    # print()
    choice = 0
    while choice != 4:
        print()
        print("1. Add Fighter")
        print("2. Delete Fighter")
        print("3. Update Stats or Info")
        print("4. Quit")
        print()
        while True:
            try:
                choice = int(input())
            except ValueError:
                print("Please enter one of the options")
            if choice > 4:
                print("Please enter a valid number")
            else:
                break
        if choice == 1:
            m.add_fighter(conn, cur)
        elif choice == 2:
            m.delete_fighter(conn,cur)
        elif choice == 3:
            m.update_records(conn,cur)




def display(conn,cur):
    choice = 0
    while choice != 5:
        print("\nWhat do you want to display:")
        print("1. All Cometitors")
        print("2. Only Male Competitors")
        print("3. Only Female Competitors")
        print("4. All Competitions")
        print("5. Exit\n")
        while True:
            try:
                choice = int(input())
            except ValueError:
                print("\nPlease enter one of the options")
            if choice > 5:
                print("\nPlease enter a valid number")
            else:
                break
        if choice == 6:
            return choice
        elif choice == 1:
            d.display_all_comp(conn,cur)
        elif choice == 2:
            d.display_all_competitor_male(conn,cur)
        elif choice == 3:
            d.display_all_competitor_female(conn,cur)
        elif choice == 4:
            d.display_each_event(conn,cur)




def look_up(conn, cur):
    choice = 0
    while choice != 5:
        print()
        print("\nWhat do you want to look up?")
        print("1. Fighters Information")
        print("2. Fighters ID")
        print("3. Fihgters Overall Score")
        print("4. Events Winners")
        print("5. Quit")
        print()
        while True:
            try:
                choice = int(input())
            except ValueError:
                print("Please enter one of the options")
            if choice > 5:
                print("\nPlease enter a valid number")
            else:
                break
        if choice == 1:
            l.get_fighter_by_id(conn,cur)
        elif choice == 2:
            l.get_fighter_info(conn,cur)
        elif choice == 3:
            l.get_all_stats(conn,cur)
        elif choice == 4:
            l.get_event_winners(conn,cur)

def generate_graph(x, y, user):
    # Graphing fighter's efficiency either when striking or attempting take downs
    # Paramters will be x and y axis, along with string that speficies type of graph
    # x = total number of strikes/takedowns
    # y = striking accuaracy/take down accuracy
    fig = plt.figure()
    ax = fig.subplots(1, 1)
    ax.scatter(x, y, c="b", marker='8')

    if user.lower() == 's':
        ax.set_title("Striking Efficiency")
        ax.set_xlabel("Total Strikes")
        ax.set_ylabel("Strike Accuracy")
    elif user.lower() == "t":
        ax.set_title("Take Down Efficiency")
        ax.set_xlabel("Total Take Downs")
        ax.set_ylabel("Take Down Accuracy")

    i = 0
    myFile = "UFC_Graph" + str(i) + ".png"
    i += 1
    fig.savefig(myFile)

def junction(conn, cur):
        print("Enter 2 weight class: ")
        print("1. Mens Heavyweights")
        print("2. Mens Middleweights")
        print("3. Womens Bantamweight")
        print("4. Womens Strawweight")
        num = int(input())
        num2 = int(input())
        data = ""
        data2 = ""
        if num == 1:
            data = "Mens_Heavyweights"
        elif num == 2:
            data = "Mens_Middleweights"
        elif num == 3:
            data = "Womens_Bantamweight"
        elif num == 4:
            data = "Womens_Strawweight"

        if num2 == 1:
            data2 = "Mens_Heavyweights"
        elif num2 == 2:
            data2 = "Mens_Middleweights"
        elif num2 == 3:
            data2 = "Womens_Bantamweight"
        elif num2 == 4:
            data2 = "Womens_Strawweight"

        cmd = """
        SELECT {}.name, {}.name, {}.age, {}.age
        FROM {} INNER JOIN {}
        ON {}.age = {}.age
        ORDER BY {}.age, {}.name;
        """.format(data, data2, data, data2, data, data2, data, data2, data, data)
        cur.execute(cmd)
        l = cur.fetchall()
        d.print_records(l, ["{} Name".format(data), "{} Name".format(data2), "{} Sponsor".format(data), "{} Sponsor".format(data2)])


def main():
    conn , cur = connect()
    create_db(conn,cur)
    fill_heavyweight_db(conn,cur)
    fill_middleweight_db(conn,cur)
    fill_womens_bantamweight_db(conn,cur)
    fill_womens_strawweight_db(conn,cur)
    fill_awards(conn,cur)
    fill_competitions(conn,cur)
    print("""

|==================================================================|
|   __  ______________   __________________  __________________    |
|  / / / / ____/ ____/  / ____/  _/ ____/ / / /_  __/ ____/ __ \   |
| / / / / /_  / /      / /_   / // / __/ /_/ / / / / __/ / /_/ /   |
|/ /_/ / __/ / /___   / __/ _/ // /_/ / __  / / / / /___/ _, _/    |
|\____/_/    \____/  /_/   /___/\____/_/ /_/ /_/ /_____/_/ |_|     |
|                                                                  |
|==================================================================|
""")
    print("Hi. Welcome to our UFC Fighter database. What would you like to do?")
    print("1. Modify data")
    print("2. Generate Strike Efficiency graph")
    print("3. Display all fighters")
    print("4. Look up information")
    print("5. Compute Competiton")
    print("6. Many To Many Relatioinships")
    print("7. Quit")
    print()
    while True:
        try:
            choice = int(input())
        except ValueError:
            print("Please enter one of the options")
        else:
            break
    quit = False
    while choice != 7:
        if choice == 1:
            modify(conn, cur)
            # if choice == 4:
            #     quit = True
            #     choice = 5
        elif choice == 2:
            print("Enter a weight class: ")
            print("1. Mens Heavyweights")
            print("2. Mens Middleweights")
            print("3. Womens Bantamweight")
            print("4. Womens Strawweight")
            num = int(input())
            data = ""
            if num == 1:
                data = "Mens_Heavyweights"
            elif num == 2:
                data = "Mens_Middleweights"
            elif num == 3:
                data = "Womens_Bantamweight"
            elif num == 4:
                data = "Womens_Strawweight"
            cmd = """
            SELECT {}.strikes FROM {}
            """.format(data, data)
            cmd2 = """
            SELECT {}.strike_accuracy FROM {}
            """.format(data, data)
            cur.execute(cmd)
            strike = cur.fetchall()
            cur.execute(cmd2)
            acc = cur.fetchall()
            generate_graph(strike, acc, 's')
        elif choice == 3:
            display(conn,cur)
        elif choice == 4:
            look_up(conn,cur)
            # if choice == 3:
            #     quit = True
            #     choice = 5
        elif choice == 5:
            compute_competition(conn,cur)
        elif choice == 6:
            junction(conn, cur)
        else:
            print("\nSorry, invalid input. Try again.\n")
        if not quit:
            menu()
            while True:
                try:
                    choice = int(input())
                except ValueError:
                    print("Please enter one of the options")
                else:
                    break
    if choice == 7:
        print("Goodbye!")

if __name__ == "__main__":
    main()
