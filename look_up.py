import display as d
def get_fighter_by_id(conn,cur):
    
    while True:
        try: 
            ID = int(input("What is the fighters ID: "))
        except ValueError:
            print("please enter a number")
        else:
            break
    
    print("\nWhat competition are they in")
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
    
    cmd ="""Select * FROM {} WHERE {}.ID = {} """.format(data,data,ID)
    cur.execute(cmd)
    lis = cur.fetchall()
    if len(lis) > 0:
        print("\nWere you looking for: ")
        d.print_records2(lis, ["Name","Sponsor","Sex","Age","ID","Phone Number","Fights","Strikes","Take Downs","Knock Downs","Reversals","Submissions","Strike Acurracy","Take Down Acurracy"])
    else:
        print("\nSorry this person doesn't exist in the " + data + " competition")
        

def get_fighter_info(conn,cur):
    name = input("Whats the fighters name: ").lower()
    while True:
        try: 
            age = input("Whats the fighters age: ")
        except ValueError:
            print("please enter one of the options")
        else:
            break
    
    print("\nWhat competition are they in")
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
    
    cmd = """ SELECT {}.ID From {} WHERE LOWER({}.name) = ?""".format(data,data,data)
    cur.execute(cmd,(name,))
    info =  cur.fetchall()
    if len(info) > 0:
        print()
        d.print_records2(info,["Fighter ID"])
        print()
    else:
        print()
        print("Sorry, could not find that fighter")
        print()
        
def get_all_stats(conn,cur):
    print("\t=====Mens Heavyweight=====")
    comp =[]
    cmd = """
    SELECT * FROM Mens_Heavyweights
    """
    cur.execute(cmd)
    stats = cur.fetchall()
    #print(stats)
    for i in stats:
        sum1 = 0
        for j in range(7,13):
            sum1 += i[j]
        comp.append((i[0],sum1))
    d.print_records(comp,["Name","Overall Stats"])
    
    print("\n\t=====Mens Middleweights=====")
    
    cmd = """
    SELECT * FROM Mens_Middleweights
    """
    comp = []
    cur.execute(cmd)
    stats = cur.fetchall()
    for i in stats:
        sum1 = 0
        for j in range(7,13):
            sum1 += i[j]
        comp.append((i[0],sum1))
    d.print_records(comp,["Name","Overall Stats"])
    
    print("\n\t=====Womens Bantamweight=====")
    cmd = """
    SELECT * FROM Womens_Bantamweight
    """
    comp = []
    cur.execute(cmd)
    stats = cur.fetchall()
    for i in stats:
        sum1 = 0
        for j in range(7,13):
            sum1 += i[j]
        comp.append((i[0],sum1))
    d.print_records(comp,["Name","Overall Stats"])
    
    print("\n\t=====Womens Strawweight=====")
    cmd = """
    SELECT * FROM Womens_Strawweight
    """
    comp = []
    cur.execute(cmd)
    stats = cur.fetchall()
    for i in stats:
        sum1 = 0
        for j in range(7,13):
            sum1 += i[j]
        comp.append((i[0],sum1))
    d.print_records(comp,["Name","Overall Stats"])
    
def get_event_winners(conn,cur):
    cmd = """SELECT Awards.winner,Awards.id ,Awards.place,Awards.award FROM Awards WHERE Awards.winner != 'None' """
    cur.execute(cmd)
    table = cur.fetchall()
    if len(table)>0:
        d.print_records2(table,["Winner", "Fighter ID", "Place","Award"])
    else:
        print("Sorry there hasn't been any competitions\ngo back to the main menue and choose option 5 first")
    print()