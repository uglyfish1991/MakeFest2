#######################################
#                                     #
#          local imports              #
#                                     #
#######################################

from speeds import fast_text, wait_text
from text_colours import *

#######################################
#                                     #
#          library imports            #
#                                     #
#######################################

import random

#######################################
#                                     #
#          variables                  #
#                                     #
#######################################

first_word=["The ", "My ", "His ","Her ","Our ","A ", "Each ", ]
adjective = ["Sleepy ", "Happy ", "Lonely ", "Rainy ", "Cheerful ", "Weary ", "Lost ", "Decayed ", "Secret ", "Hidden ", "Imagined "]
noun = ["Raven", "Window", "Room", "Mirror", "Castle", "Ghost", "Path", "Tree", "Forest", "Mountain", "River", "Relic"]

first_name = ["Matt ", "Jenny ", "David ", "Michael ", "Paul ", "Chris ", "Connor ", "Jon ", "Li ", "Lorraine ", "Keira ", "Liam ", "Jordan "]
last_name = ["Way", "Stumpp", "Coleman", "Walker", "Draper", "King", "Rathbone", "Toro", "Iero", "Smith", "Park", "Kim", "Chen", "Roberts"]

cat = ["Fiction", "Young Adult", "New Adult", "Science Fiction", "Thriller", "Crime"]

n = 0
#######################################
#                                     #
#          function start             #
#                                     #
#######################################
def as_cat():
    global n
    fast_text("Generating 100 assets in system \nPlease wait  \n")
    wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
    fast_text("Generating 100 assets in system \nPlease wait  \n")
    wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")

    for i in range(1,101):
        n +=1
        genre = random.choice(cat)
        title = random.choice(first_word) + random.choice(adjective) + random.choice(noun)
        name = random.choice(first_name) + random.choice(last_name)
        print(f"{bcolors.WARNING}Asset Number:{bcolors.ENDC} {n}")
        print(f"{bcolors.WARNING}Genre:{bcolors.ENDC} {genre}")
        print(f"{bcolors.WARNING}Title:{bcolors.ENDC} {title}")
        print(f"{bcolors.WARNING}Author:{bcolors.ENDC} {name}")
        print("\n\n")

    fast_text("Would you like to generate the next 100 assets?  \nSelect from the following options \n\n1 - Yes \n2 - Return to main menu \n")
    answer = input("     >>    ")

    while answer !="1" and answer !="2":
        fast_text(f"{bcolors.WARNING}Unexpected input \nPlease Try Again {bcolors.ENDC} \nPlease type 1 or 2")
        answer=input("     >>    ")

    if answer=="1":
        as_cat()

        # for i in range(1,101):
        #     n +=1
        #     genre = random.choice(cat)
        #     title = random.choice(first_word) + random.choice(adjective) + random.choice(noun)
        #     name = random.choice(first_name) + random.choice(last_name)
        #     print(f"{bcolors.WARNING}Asset Number:{bcolors.ENDC} {n}")
        #     print(f"{bcolors.WARNING}Genre:{bcolors.ENDC} {genre}")
        #     print(f"{bcolors.WARNING}Title:{bcolors.ENDC} {title}")
        #     print(f"{bcolors.WARNING}Author:{bcolors.ENDC} {name}")
        #     print("\n\n")
    else:
        fast_text("Thank you \nReturning to Main Menu\n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        return
