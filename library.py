import pymysql

while True:
    def less(numl):
        return numl - 1

    inp = int(input("1.Adding Book\n2.Show Books\n3.Deleting Books\n4.Issuing Books\n5.Returning Books\n6.Exit\nEnter Your Choice :- "))
    con = pymysql.connect(host='localhost', user="root", password='', database="library", port=3306)
    if inp == 1:
        cur2 = con.cursor()
        namea = input("Enter Your Book Name :- ")
        quantitya = input("Enter Your Book Quantity :- ")

        cur2.execute("INSERT INTO `lib` (`id`, `name`, `quantity`, `issue_quantity`) VALUES (NULL, %s, %s, '0')", (namea, quantitya))

        cur2.close()
        con.commit()

    elif inp == 2:
        cur1 = con.cursor()
        s = cur1.execute("select * from lib")
        fet = cur1.fetchall()
        for row in fet:
            print(row)
        cur1.close()
        con.commit()

    elif inp == 3:
        cur3 = con.cursor()
        libid = input("Enter Deleting Book ID :- ")
        cur3.execute("DELETE FROM lib WHERE `lib`.`id` = %s", libid)

        cur3.close()
        con.commit()

    elif inp == 4:
        cur4 = con.cursor()
        cur5 = con.cursor()
        ib = input("Enter Your issue Book :- ")
        b = cur4.execute("select * from `lib` where `name` = %s", (ib))
        fetchallt = cur4.fetchall()
        for r in fetchallt:
            rval = list(r)
            done = int(rval[3]) + 1

            # Update the issue_quantity in the database
            cur5.execute("UPDATE `lib` SET `issue_quantity` = %s WHERE `name` = %s", (done, ib))

            # Then select the row with the updated issue_quantity
            cur5.execute("SELECT * FROM `lib` WHERE `name` = %s AND `issue_quantity` = %s", (ib, done))

        cur4.close()
        cur5.close()
        con.commit()

    elif inp == 5:
        pass

    elif inp == 6:
        quit()

    else:
        print("Incorrect Query")


    con.close()
