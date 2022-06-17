# Imports
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

import datetime
import time

#######################################
#                                     #
#          variables                  #
#                                     #
#######################################

seen=False

#######################################
#                                     #
#          function start             #
#                                     #
#######################################

def search_a(timeb): #takes variable from function call in main - couldn't do this any other way without circular imports?
    global seen
    answers=["1","2","3","4"]
    fast_text("\n\nInitiating Search \n\n")
    fast_text(f"{bcolors.WARNING}System Search currently semi-operational \nPlease build your search{bcolors.ENDC} \n\nPlease input your search term\n")
    ans1=input("      >>    ")
    fast_text("Please wait - search building\n")
    wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
    print(f" {bcolors.OKGREEN} if {ans1} in {bcolors.ENDC}")
    fast_text("Where are you searching? \nSelect from the following options: \n\n 1 - System Log \n 2 - System Settings \n 3 - User Database \n 4 - Asset Catalogue \n\n Please type 1, 2, 3 or 4")
    ans2=input("      >>    ")

    while ans2 not in answers: #while loop for unexpected answers
        fast_text(f"{bcolors.WARNING}Unexpected input \n Please Try Again {bcolors.ENDC} \n Please type 1, 2, 3 or 4")
        ans2=input("      >>    ")

# options for if user selects search in sys log
# shows 2 searches for the number given - one is previous users, one is ours
    if ans2=="1":
        search_place="System Log"
        print(f" {bcolors.OKGREEN} if \"{ans1}\" in {search_place} {bcolors.ENDC}")
        print(f" {bcolors.OKGREEN}      print(all_occurences()) {bcolors.ENDC}\n \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"Searching for {ans1} in the {search_place} \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"{bcolors.OKCYAN} 2 matching item(s) found in {search_place}{bcolors.ENDC}")
        our_search=datetime.datetime.now()
        print(f"""
<aa0Exffdo> System clear 300622 11:57:30.76821
<aa0Exffdo> System clear 300622 13:57:30.18236
<aa0Exffdo> System clear 300622 15:57:30.40923
{bcolors.OKCYAN}<aa0ExSEARCH_USER_DB()> "090477" at {timeb} {bcolors.ENDC}
{bcolors.OKCYAN}<aa0ExSEARCH_SYS_LOGS()> "090477" at {our_search} {bcolors.ENDC}

""")
        fast_text("What would you like to do now? \n\n1 - Search Again? \n2 - Quit Search? \n Please type 1 or 2\n")
        again=input("      >>    ")
        while again !="1" and again !="2":
            fast_text(f"{bcolors.WARNING}Unexpected input \n Please Try Again {bcolors.ENDC} \n Please type 1 or 2")
            again=input("      >>    ")

        if again=="1":
            search_a(timeb)
        else:
            fast_text(f"{bcolors.WARNING}Search completed successfully. Returning to main menu \n\n{bcolors.ENDC}")
            return
# options for if user selects search in sys settings
# shows 1 result, the time the hacker changed the password
    elif ans2=="2":
        search_place="System Settings"
        print(f" {bcolors.OKGREEN} if {ans1} in {search_place} {bcolors.ENDC}")
        print(f" {bcolors.OKGREEN}      print(all_occurences()) {bcolors.ENDC}\n \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"Searching for {ans1} in the {search_place} \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"{bcolors.OKCYAN}1 matching item(s) found in {search_place}{bcolors.ENDC}\n")
        print(f"""pass_log: Unkown User set_password({bcolors.OKCYAN} "090477"{bcolors.ENDC} at {timeb})
""")
        fast_text("What would you like to do now? \n\n1 - Search Again? \n2 - Quit Search? \n Please type 1 or 2\n")
        again=input("      >>    ")
        while again !="1" and again !="2":
            fast_text(f"{bcolors.WARNING}Unexpected input \n Please Try Again {bcolors.ENDC} \n Please type 1 or 2")
            again=input("      >>    ")

        if again=="1":
            search_a(timeb)
        else:
            return
# options for if user selects search in sys log
# shows 4 results - users with that DOB
    elif ans2=="3":
        search_place="User Database"
        print(f" {bcolors.OKGREEN} if {ans1} in {search_place} {bcolors.ENDC}")
        print(f" {bcolors.OKGREEN}      print(all_occurences()) {bcolors.ENDC}\n \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"Searching for {ans1} in the {search_place} \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"{bcolors.OKCYAN}4 matching item(s) found in {search_place}{bcolors.ENDC}\n")

        print(f"""
        {bcolors.WARNING}Name:{bcolors.ENDC} Batey, Stephen    {bcolors.WARNING}D.O.B:{bcolors.ENDC} 09/04/77     {bcolors.WARNING}User Number:{bcolors.ENDC} LCC0374992     {bcolors.WARNING}Current:{bcolors.ENDC} 0 pending    {bcolors.WARNING}Notes:{bcolors.ENDC} N/A
        {bcolors.WARNING}Name:{bcolors.ENDC} Davies, Kieran    {bcolors.WARNING}D.O.B:{bcolors.ENDC} 09/04/77     {bcolors.WARNING}User Number:{bcolors.ENDC} LCC0600345     {bcolors.WARNING}Current:{bcolors.ENDC} 2 pending    {bcolors.WARNING}Notes:{bcolors.ENDC} N/A
        {bcolors.WARNING}Name:{bcolors.ENDC} Gregor, James     {bcolors.WARNING}D.O.B:{bcolors.ENDC} 09/04/77     {bcolors.WARNING}User Number:{bcolors.ENDC} LCC0998947     {bcolors.WARNING}Current:{bcolors.ENDC} Banned       {bcolors.WARNING}Notes:{bcolors.ENDC} {bcolors.FAIL}7 Unreturned - MAX FINE{bcolors.ENDC}
        {bcolors.WARNING}Name:{bcolors.ENDC} Traynor, Mary     {bcolors.WARNING}D.O.B:{bcolors.ENDC} 09/04/77     {bcolors.WARNING}User Number:{bcolors.ENDC} LCC0967783     {bcolors.WARNING}Current:{bcolors.ENDC} 7 pending    {bcolors.WARNING}Notes:{bcolors.ENDC} Pre-order BIThalo
""")
        fast_text("What would you like to do now? \n\n1 - Search Again? \n2 - Quit Search? \n Please type 1 or 2\n")
        again=input("      >>    ")
        while again !="1" and again !="2":
            fast_text(f"{bcolors.WARNING}Unexpected input \n Please Try Again {bcolors.ENDC} \n Please type 1 or 2")
            again=input("      >>    ")

        if again=="1":
            search_a(timeb)
        else:
            seen=True
            #this section is to make it look like the hacker is trying to log in again - we changed his password. This should lead us to failtoban        
            return seen
    elif ans2=="4":
        search_place="Asset Catalogue"
        print(f" {bcolors.OKGREEN} if {ans1} in {search_place} {bcolors.ENDC}")
        print(f" {bcolors.OKGREEN}      print(all_occurences()) {bcolors.ENDC}\n \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"Searching for {ans1} in the {search_place} \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"{bcolors.OKCYAN}8 matching item(s) found in {search_place}{bcolors.ENDC}\n")

        print(f"""
        {bcolors.WARNING}Title:{bcolors.ENDC} A Study of Benthic Life    {bcolors.WARNING}Author:{bcolors.ENDC} George Esmine     {bcolors.WARNING}ISBN:{bcolors.ENDC} 4839209047789    {bcolors.WARNING}Genre:{bcolors.ENDC} Science/Biology/Marine
        {bcolors.WARNING}Title:{bcolors.ENDC} The Economy of Influence   {bcolors.WARNING}Author:{bcolors.ENDC} Lorraine Suggs    {bcolors.WARNING}ISBN:{bcolors.ENDC} 0090477193471    {bcolors.WARNING}Genre:{bcolors.ENDC} Finance/Self-Help
        {bcolors.WARNING}Title:{bcolors.ENDC} Spanish for Beginners      {bcolors.WARNING}Author:{bcolors.ENDC} Carlos M. Suarez  {bcolors.WARNING}ISBN:{bcolors.ENDC} 0016780904773    {bcolors.WARNING}Genre:{bcolors.ENDC} Language/Spanish
        {bcolors.WARNING}Title:{bcolors.ENDC} Who Made This? A Design    {bcolors.WARNING}Author:{bcolors.ENDC} Linda Sharpe      {bcolors.WARNING}ISBN:{bcolors.ENDC} 0098730904772    {bcolors.WARNING}Genre:{bcolors.ENDC} Art & Design/Study/Analysis
        {bcolors.WARNING}Title:{bcolors.ENDC} A Time of Broken Glass     {bcolors.WARNING}Author:{bcolors.ENDC} Sarah M. Oakley   {bcolors.WARNING}ISBN:{bcolors.ENDC} 0768090477391    {bcolors.WARNING}Genre:{bcolors.ENDC} Thriller/Historic
        {bcolors.WARNING}Title:{bcolors.ENDC} Britsh Hedge Wildlife      {bcolors.WARNING}Author:{bcolors.ENDC} Richard Stringson {bcolors.WARNING}ISBN:{bcolors.ENDC} 0904779826328    {bcolors.WARNING}Genre:{bcolors.ENDC} Science/Biology/Nature
        {bcolors.WARNING}Title:{bcolors.ENDC} Javascript for Design      {bcolors.WARNING}Author:{bcolors.ENDC} James Goodman     {bcolors.WARNING}ISBN:{bcolors.ENDC} 0450904773407    {bcolors.WARNING}Genre:{bcolors.ENDC} Sciene/Technology/Internet
        {bcolors.WARNING}Title:{bcolors.ENDC} A Ride on a Raven          {bcolors.WARNING}Author:{bcolors.ENDC} Hashi Takeyama    {bcolors.WARNING}ISBN:{bcolors.ENDC} 0938090477663    {bcolors.WARNING}Genre:{bcolors.ENDC} Fantasy/New Adult
        """)
        fast_text("What would you like to do now? \n\n1 - Search Again? \n2 - Quit Search? \n Please type 1 or 2\n")
        again=input("      >>    ")
        while again !="1" and again !="2":
            fast_text(f"{bcolors.WARNING}Unexpected input \n Please Try Again {bcolors.ENDC} \n Please type 1 or 2")
            again=input("      >>    ")

        if again=="1":
            search_a(timeb)
        else:
            return

