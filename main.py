programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          }

# # # Retrieving items from dictionary.

# print(programming_dictionary["Bug"])

# # # Adding new items to dictionary.

# programming_dictionary["Loop"] = "The action of doing something over and over again."

# # # Create an empty dictionary.

# empty_dictionary = {}

# # # Wipe an existing dictionary.

# programming_dictionary = {}

# print(programming_dictionary)

# # # Edit an item in a dictionary.

# programming_dictionary["Bug"] = "A moth in your computer."

# print(programming_dictionary)

# # # Loop through a dictionary.

# for key in programming_dictionary:
#     print(key, programming_dictionary[key])

# / # / # EXERCISE # / # / #

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#     old_score = student_scores[student]
#     if 91 <= old_score:
#         student_grades[student] = "Outstanding"
#     elif 81 <= old_score <= 90:
#         student_grades[student] = "Exceeds Expectations"
#     elif 71 <= old_score <= 80:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades)

# / # / # / # / # / #

# # # Nesting

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# # # Nesting a List in a Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# # # Nesting Dictionary in a Dictionary

# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 24}
# }

# # # Nesting Dictionary in a List

# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 24}
# ]

# / # / # EXERCISE # / # / #

# country = input("Add country name:\n")
# visits = int(input("Number of visits:\n"))
# list_of_cities = eval(input("Create list from formatted string:\n"))

# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 24
#     }
# ]


# def add_new_country(name, times_visited, cities_visited):
#     new_travel_entry = {
#         "country": name,
#         "cities": cities_visited,
#         "visits": times_visited,
#     }

#     travel_log.append(new_travel_entry)


# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")

# / # / # / # / # / #

# / # / # PROJECT OF DAY 9 # / # / #

from replit import clear
from art import logo

print(logo)

secret_list = {}
more_bidders = True


def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${bid_amount}!")


while more_bidders:
    name = input("What is your name?: ").title()
    bid = int(input("What is your bid?: $"))
    secret_list[name] = bid

    ask_for_bidders = input("Are there any other bidders? Type 'yes' or 'no'").lower()

    if ask_for_bidders == "no":
        more_bidders = False
        highest_bidder(secret_list)
    elif ask_for_bidders == "yes":
        clear()
