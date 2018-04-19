import display as d
def add_fighter(conn,cur):
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

    cmd = "SELECT COUNT(*) FROM {}".format(data)
    cur.execute(cmd)
    size = cur.fetchall()
    if size[0][0] >= 16:
        print("\nSorry, this competition is full\n")
    else:
        text = ['name(Last Name, First)','age','sex','sponsor']
        personal = ['id number','phone number',]
        integer = ['fights','strikes','take downs','knock downs','reversals','submissions']
        DOUBLE = ['strike accuracy','take down accuracy']
        print("In order to add a comptetor you need to provid some information")
        tupe = ()
        for i in text:
             while True:
                try:
                    info = str(input("Enter the competetors {} ".format(i)))
                    tupe += (info,)
                except ValueError:
                    print("Please enter a string")
                else:
                    break
        tupe += ()
        for i in personal:
            while True:
                try:
                    info = input("Enter the competetors {} ".format(i))
                    tupe += (info,)
                except ValueError:
                    print("Please enter a number")
                else:
                    break
        for i in integer:
            while True:
                try:
                    info = input("Enter the competetors {} ".format(i))
                    tupe += (info,)
                except ValueError:
                    print("Please enter a number")
                else:
                    break
        for i in DOUBLE:
            while True:
                try:
                    info = input("Enter the competetors {} ".format(i))
                    tupe += (info,)
                except ValueError:
                    print("Please enter a number")
                else:
                    break

        cmd = """
            INSERT INTO {}(
            name,
            age,
            sex,
            ID,
            sponsor,
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
            """.format(data)
        cur.execute(cmd,tupe)
        conn.commit

def delete_fighter(conn, cur):
    while True:
        try:
            name = input("What fighter do you want to delete(last name, first): ")
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
    cur.execute("""SELECT {}.name FROM {} WHERE LOWER({}.name) = (?)""".format(data,data,data),(name.lower(),))
    if len(cur.fetchall()) > 0:
        print("\nOkay all done")
        cmd = """DELETE FROM {} WHERE LOWER({}.name) = (?)""".format(data,data)
        cur.execute(cmd,(name.lower(),))
    else:
        print("\nSorry couldn't find {}".format(name))


def update_records(conn,cur):
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
        #fname =
    elif i == 2:
        data = "Mens_Middleweights"
        #fanme =
    elif i == 3:
        data = "Womens_Bantamweight"
        #fname =
    elif i == 4:
        data = "Womens_Strawweight"
        #fname

    name = input("\nWhat is the fighters name(Last Name, First): ").lower()
    print(name)

    stats_list = ["ID","Phone_Number","Fights","strikes","take_downs","reversals","submissions","strike_accuracy","take_down_accuracy"]



    cmd = """SELECT * FROM {} WHERE LOWER({}.name) = ?""".format(data,data)
    cur.execute(cmd,(name,))
    lis = cur.fetchall()

    if len(lis) > 0:

        print("\nWhat stats would you like to change")

        for i in (stats_list):
            print("\nWould you like to update ",i)
            user = input("\nY or N? ")
            if user.lower() == 'y':
                new_data = input("\nWhat is the new "+ i +" data ")
                cmd = '''UPDATE {} SET {} = {} WHERE LOWER({}.name) = (?)'''.format(data,i.lower(),new_data,data)
                cur.execute(cmd,(name,))
                conn.commit

                print("\n This is the updated data: \n")
                cmd = """ Select * FROM {} WHERE LOWER({}.name) = (?)""".format(data,data)
                cur.execute(cmd,(name,))
                d.print_records2(cur.fetchall(),["Name","Sponsor","Sex","Age","ID","Phone Number","Fights","Strikes","Take Downs","Knock Downs","Reversals","Submissions","Strike Acurracy","Take Down Acurracy"])
                print()
    else:
        print("\nSorry, no one by that name\n")
