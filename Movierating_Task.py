movie_ratings = {

    "u" : "everyone can watch",
  "pg" : "General viewing, but some scenes may be unsuitable for young children",
  "12" : "Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.",
  "15" : "No one younger than 15 may see a 15 film in a cinema.",
   "18" : "No one younger than 18 may see an 18 film in a cinema."
}


def User_Check(Age):

    if User_rating == "exit":
        return False
    elif User_rating == "u":
        print(movie_ratings["u"])
        return True
    elif User_rating == "pg":
        print(movie_ratings["pg"])
        return True
    elif User_rating == "12":
        print(movie_ratings["12"])
        return True
    elif User_rating == "15":
        print(movie_ratings["15"])
        return True
    elif User_rating == "18":
        print(movie_ratings["18"])
        return True


while True:
    print("You can choose from the following")
    for ratings in movie_ratings.keys():
        print(ratings)
    User_rating = input("What rating do you want to know about?  ").lower()
    if User_rating in movie_ratings.keys():

        if User_Check(User_rating):

            if input("Do you want to see another one? Y/N  ").upper() == "Y":
                print("\n")
                continue
            else:
                break

    elif User_rating == "exit":
        break
    else:
        print("Please enter a valid movie rating")