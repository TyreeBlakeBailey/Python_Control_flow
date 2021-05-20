# U, PG, 12, 16, 18+


def AgeChecker(age):
    print("Because you are {} you can see the following".format(age))
    if age >= 18:
        print("You can see 18+ movies")
    if age >= 16:
        print("You can see 16 movies")
    if age >= 12:
        print("You can see 12+ movies")
    if age < 12:
        print("You can watch a PG film with an adult")
        if input("Are you with a adult? Y/N ").upper() == "Y":
            print("You can watch Pg films")


while True:
    try:
        age = int(input("What is your age?  "))
        AgeChecker(age)
        print("You can watch a U film at any age")
        break

    except ValueError:
        print("This is not a valid age.. \nTry again")
