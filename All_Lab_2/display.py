def print_records(records, column_headers):
    """Pretty print the records with given column headers"""
    # Create a format string making each column left aligned and 30 characters wide
    fmt_string = "{:<40}" * len(column_headers)

    # Print header row
    print(fmt_string.format(*column_headers))

    # Print records
    # records is a list of tuples
    # each tuple is a specific record in the database
    # *row expands the tuple into separate arguments for format
    for row in records:
        print(fmt_string.format(*row))
    print()
    
def print_records2(records, column_headers):
    """Pretty print the records with given column headers"""
    # Create a format string making each column left aligned and 30 characters wide
    fmt_string = "{:<18}" * len(column_headers)
    # Print header row
    print(fmt_string.format(*column_headers))
    # Print records
    # records is a list of tuples
    # each tuple is a specific record in the database
    # *row expands the tuple into separate arguments for format
    for row in records:
        print(fmt_string.format(*row))
        
def display_all_comp(conn,cur):
    print("    ~~~ALL COMPETITORS~~~") 
    comp = []
    cmd = """
    SELECT Mens_Heavyweights.name, Mens_Heavyweights.ID FROM Mens_Heavyweights
    """
    cur.execute(cmd)
    stats = cur.fetchall()
    for i in stats:
        comp.append((i[0],i[1]))
    cmd = """
    SELECT Mens_Middleweights.name, Mens_Middleweights.ID FROM Mens_Middleweights
    """
    cur.execute(cmd)
    stats = cur.fetchall()
    for i in stats:
        comp.append((i[0],i[1]))
    cmd = """
    SELECT Womens_Bantamweight.name, Womens_Bantamweight.ID FROM Womens_Bantamweight
    """
    cur.execute(cmd)
    stats = cur.fetchall()
    for i in stats:
        comp.append((i[0],i[1]))
    cmd = """
    SELECT Womens_Strawweight.name, Womens_Strawweight.ID FROM Womens_Strawweight
    """
    cur.execute(cmd)
    stats = cur.fetchall()
    for i in stats:
        comp.append((i[0],i[1]))
    comp = sorted(comp)
    # for i in comp:
    #     print('\t{:<20}{:>20}'.format(i[0],i[1]))
    print_records(comp, ["NAME ", "ID"])
    
        
def display_each_event(conn,cur):
    cmd = """
    SELECT Competitions.stage, Competitions.date, Competitions.start_time FROM Competitions Where Competitions.event = 'Mens_Heavyweights'
    """
    cur.execute(cmd)
    stats = cur.fetchall()
    print("\nHere are all the date and times for the Mens Heavyweight fights\n")
    print_records(stats, ["Stage","Date","Time"])

    cmd = """
    SELECT Competitions.stage, Competitions.date, Competitions.start_time FROM Competitions Where Competitions.event = 'Mens_Middleweights'
    """
    cur.execute(cmd)
    stats = cur.fetchall()
    print("\nHere are all the date and times for the Mens Middleweights fights\n")
    print_records(stats, ["Stage","Date","Time"])
    
    cmd = """
    SELECT Competitions.stage, Competitions.date, Competitions.start_time FROM Competitions Where Competitions.event = 'Womens_Bantamweight'
    """
    cur.execute(cmd)
    stats = cur.fetchall()
    print("\nHere are all the date and times for the Womens Bantaweight fights\n")
    print_records(stats, ["Stage","Date","Time"])
    
    cmd = """
    SELECT Competitions.stage, Competitions.date, Competitions.start_time FROM Competitions Where Competitions.event = 'Womens_Strawweight'
    """
    cur.execute(cmd)
    stats = cur.fetchall()
    print("\nHere are all the date and times for the Womens Strawweight fights\n")
    print_records(stats, ["Stage","Date","Time"])
    
    
    
def display_all_competitor_male(conn,cur):
    male = []
    cmd = """
    SELECT Mens_Heavyweights.name FROM Mens_Heavyweights
    """
    cur.execute(cmd)
    stats = cur.fetchall()
    for i in stats:
        male.append(i[0])
    cmd = """
    SELECT Mens_Middleweights.name FROM Mens_Middleweights
    """
    cur.execute(cmd)
    stats = cur.fetchall()
    for i in stats:
        male.append(i[0])
    male = sorted(male)
    print("\n   ~~~ALL MALE COMPETITORS~~~") 
    for i in male:
        print('\t{:<5}'.format(i))


def display_all_competitor_female(conn,cur):
    female = []
    cmd = """
    SELECT Womens_Bantamweight.name FROM Womens_Bantamweight
    """
    cur.execute(cmd)
    stats = cur.fetchall()
    for i in stats:
        female.append(i[0])
    cmd = """
    SELECT Womens_Strawweight.name FROM Womens_Strawweight
    """
    cur.execute(cmd)
    stats = cur.fetchall()
    for i in stats:
        female.append(i[0])
    female = sorted(female)
    print("\n~~~ALL FEMALE COMPETITORS~~~")
    for i in female:
        print('\t{:<5}'.format(i))