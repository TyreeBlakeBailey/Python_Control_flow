#control flow with if, elif and else
#loops: while, for

# if statment
# weather = "rain"
#
# if weather == "sunny": #if the boolean value = true then run next line of code
#     print("Enjoy the weather")
# elif weather == "rain":
#     print("Bring an umbrella, its raining")
# elif weather == "cloudy":
#     print("No sun, but lucky no rain yet")
# else:
#     print("Something went wrong")


list_data = [1,2,3,4,5,6]

for list in list_data:
    if list == 3:
        print("I found 3")
    if list == 1:
        print("I found 1")
    if list == 6:
        print("I found 6")
    if list == 2:
        print("I found 2")

#second interations

student_1 = {
    "name" : "Tyree ",
    "key"  : "Value",
    "stream" : "Cyber Security", #string
    "Completed_lessons" : "3", #int
    "Complete_lessons_names":["variables", "operators", "data_collections"] #list


}

for data in student_1.values():
    if data == "Cyber Security":
        break
    print(data)