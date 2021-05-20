# U, PG, 12, 16, 18+

Movies = {
    "18+": "Horror",
    "16+": "comedy",
    "12+": "Family",
    "PG": "Animation",
    "U": "Disney"
}


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
            return True
        else:
            print("You need adult supervision to watch PG movies")



def MovieList(age):
    print("Because you are {} the following movies are available".format(age))
    if age >= 18:
        print(Movies["18+"])
    if age >= 16:
        print(Movies["16+"])
    if age >= 12:
        print(Movies["12+"])
    if age < 12:
        print(Movies["PG"]) # add checker to see if the child is with an adult
        print(Movies["U"])

while True:
    try:
        age = int(input("What is your age?  "))
        AgeChecker(age)
        print("You can watch a U film at any age")
        MovieList(age)
        break

    except ValueError:
        print("This is not a valid age.. \nTry again")
