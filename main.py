from DB import DB

def output(x):
    print(f"PRESS 1 to insert new {x}")
    print(f"PRESS 2 to display all {x}")
    print(f"PRESS 3 to delete  {x}")
    print(f"PRESS 4 to update  {x}")
    print(f"PRESS 5 to go back", end='\n\n')

def main():
    db = DB()
    while True:
        print("***********WELCOME**********")
        print("PRESS 1 to make changes in Employee")
        print("PRESS 2 to make changes in Position")
        print("PRESS 3 to make changes in Note")
        print("PRESS 4 to make changes in Work_graphic")
        print("PRESS 5 to make changes in KPP")
        print("PRESS 6 to make changes in Penalty")
        print("PRESS 7 to make changes in Penalty_reason")
        print("PRESS 8 to make changes in Penalty_tariff")
        print("PRESS 9 to exit program", end='\n\n')
        try:
            choice = int(input('Enter: '))
            if (choice == 1): # Employee
                while True:
                    output("Employee")
                    choice_2 = int(input('Enter: '))
                    if (choice_2 == 1):
                        # insert user
                        firstname = input("Enter user Firstname:")
                        lastname = input("Enter user Lastname: ")
                        family_name = input("Enter user Family_name: ")
                        date_birth = input("Enter date of the birt:")
                        id_position = int(input("Enter user ID_Position: "))
                        id_work_graphic = int(input("Enter user ID_Work_graphic: "))
                        db.insert_user(firstname, lastname, family_name, date_birth, id_position, id_work_graphic)
                    elif choice_2 == 2:
                        # display  user
                        db.fetch_user()
                        pass
                    elif choice_2 == 3:
                        # delete user
                        userid = int(input("Enter user id to which you want to delete: "))
                        db.delete_user(userid)
                    elif choice_2 == 4:
                        # update user
                        id = int(input("enter id of user: "))
                        firstname = input("new Firstname:")
                        lastname = input("new user Lastname:")
                        family_name = input("Enter user Family_name: ")
                        date_birth = input("Enter date of the birt:")
                        id_position = int(input("new user ID_Position: "))
                        id_work_graphic = int(input("new user ID_Work_graphic: "))
                        db.update_user(id, firstname, lastname, family_name, date_birth, id_position, id_work_graphic)
                    elif choice_2 == 5:
                        break
                    else:
                        print("Invalid input! Try again")
            elif (choice == 2): # Position
                while True:
                    output("Position")
                    choice_2 = int(input('Enter: '))
                    if (choice_2 == 1):
                        # insert position
                        name = input("Enter name of Position:")
                        db.insert_position(name)
                    elif choice_2 == 2:
                        # display  position
                        db.fetch_position()
                        pass
                    elif choice_2 == 3:
                        # delete position
                        id = int(input("Enter Position id which you want to delete: "))
                        db.delete_position(id)
                    elif choice_2 == 4:
                        # update position
                        id = int(input("enter id of position: "))
                        name = input("Enter new name of Position:")
                        db.update_position(id, name)
                    elif choice_2 == 5:
                        break
                    else:
                        print("Invalid input! Try again")

            elif (choice == 3): # Note
                while True:
                    output("Note")
                    choice_2 = int(input('Enter: '))
                    if (choice_2 == 1):
                        # insert note
                        reason = input("Enter note reason:")
                        status = input("Enter note status:")
                        time = input("Enter time:")
                        db.insert_note(reason, status, time)
                    elif choice_2 == 2:
                        # display note
                        db.fetch_note()
                        pass
                    elif choice_2 == 3:
                        # delete note
                        id = int(input("Enter Note id which you want to delete: "))
                        db.delete_note(id)
                    elif choice_2 == 4:
                        # update note
                        id = int(input("enter id of note: "))
                        reason = input("Enter new note reason:")
                        status = input("Enter new note status:")
                        time = input("Enter new time:")
                        db.update_note(id, reason, status, time)
                    elif choice_2 == 5:
                        break
                    else:
                        print("Invalid input! Try again")

            elif (choice == 4): # Work_graphic
                while True:
                    output("Work graphic")
                    choice_2 = int(input('Enter: '))
                    if (choice_2 == 1):
                        # insert work_graphic
                        t1 = input("Enter start time of working day:")
                        t2 = input("Enter end time of working day:")
                        db.insert_work_graphic(t1, t2)
                    elif choice_2 == 2:
                        # display work_graphic
                        db.fetch_work_graphic()
                        pass
                    elif choice_2 == 3:
                        # delete work_graphic
                        id = int(input("Enter Work graphic id which you want to delete: "))
                        db.delete_work_graphic(id)
                    elif choice_2 == 4:
                        # update work_graphic
                        id = int(input("enter id of work graphic: "))
                        t1 = input("Enter start time of working day:")
                        t2 = input("Enter end time of working day:")
                        db.update_work_graphic(id, t1, t2)
                    elif choice_2 == 5:
                        break
                    else:
                        print("Invalid input! Try again")

            elif (choice == 5): # KPP
                while True:
                    output("KPP")
                    choice_2 = int(input('Enter: '))
                    if (choice_2 == 1):
                        # insert kpp
                        t1 = input("Enter time in of employee:")
                        t2 = input("Enter time out of employee:")
                        id = int(input("Enter id of employee: "))
                        db.insert_kpp(t1, t2, id)
                    elif choice_2 == 2:
                        # display kpp
                        db.fetch_kpp()
                        pass
                    elif choice_2 == 3:
                        # delete kpp
                        id = int(input("Enter KPP id which you want to delete: "))
                        db.delete_kpp(id)
                    elif choice_2 == 4:
                        # update kpp
                        id = int(input("enter id of kpp: "))
                        t1 = input("Enter new time in of employee:")
                        t2 = input("Enter new time out of employee:")
                        id_2 = int(input("Enter new id of employee: "))
                        db.update_kpp(id, t1, t2, id_2)
                    elif choice_2 == 5:
                        break
                    else:
                        print("Invalid input! Try again")

            elif (choice == 6): # Penalty
                while True:
                    output("Penalty")
                    choice_2 = int(input('Enter: '))
                    if (choice_2 == 1):
                        # insert penalty
                        id_1 = int(input("Enter id penalty reason: "))
                        pay = input("Enter payment status:")
                        date = input("Enter penalty date: ")
                        db.insert_penalty(id_1, pay, date)
                    elif choice_2 == 2:
                        # display penalty
                        db.fetch_penalty()
                        pass
                    elif choice_2 == 3:
                        # delete penalty
                        id = int(input("Enter penalty id which you want to delete: "))
                        db.delete_penalty(id)
                    elif choice_2 == 4:
                        # update penalty
                        id = int(input("enter id of penalty: "))
                        id_1 = int(input("Enter new id penalty reason: "))
                        pay = input("Enter new payment status:")
                        date = input("Enter new penalty date: ")
                        db.update_penalty(id, id_1, pay, date)
                    elif choice_2 == 5:
                        break
                    else:
                        print("Invalid input! Try again")

            elif (choice == 7): # Penalty_reason
                while True:
                    output("Penalty reason")
                    choice_2 = int(input('Enter: '))
                    if (choice_2 == 1):
                        # insert penalty_reason
                        name = input("Enter penalty reason:")
                        db.insert_penalty_reason(name)
                    elif choice_2 == 2:
                        # display  penalty_reason
                        db.fetch_penalty_reason()
                        pass
                    elif choice_2 == 3:
                        # delete penalty_reason
                        id = int(input("Enter Penalty reason id which you want to delete: "))
                        db.delete_penalty_reason(id)
                    elif choice_2 == 4:
                        # update penalty_reason
                        id = int(input("enter id of penalty reason: "))
                        name = input("Enter new name of Penalty reason:")
                        db.update_penalty_reason(id, name)
                    elif choice_2 == 5:
                        break
                    else:
                        print("Invalid input! Try again")

            elif (choice == 8): # Penalty_tariff
                while True:
                    output("Penalty tariff")
                    choice_2 = int(input('Enter: '))
                    if (choice_2 == 1):
                        # insert penalty_tariff
                        id = int(input("Enter id of penalty reason: "))
                        sum = float(input("Enter sum of penalty: "))
                        db.insert_penalty_tariff(id, sum)
                    elif choice_2 == 2:
                        # display penalty_tariff
                        db.fetch_penalty_tariff()
                        pass
                    elif choice_2 == 3:
                        # delete penalty_tariff
                        id = int(input("Enter Penalty tariff id which you want to delete: "))
                        db.delete_penalty_tariff(id)
                    elif choice_2 == 4:
                        # update penalty_tariff
                        id = int(input("enter id of penalty tariff: "))
                        id_2 = int(input("Enter new id of penalty reason:"))
                        s = float(input("Enter new sum of penalty:"))
                        db.update_penalty_tariff(id, id_2, s)
                    elif choice_2 == 5:
                        break
                    else:
                        print("Invalid input! Try again")
            elif (choice == 9):
                print('Have a nice day!')
                break
            else:
                print("Invalid input! Try again")
        except Exception as e:
            print(e)
            print("Invalid Details! Try again")


if __name__ == "__main__":
    main()