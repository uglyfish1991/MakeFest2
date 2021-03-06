#######################################
#                                     #
#          local imports              #
#                                     #
#######################################
import password #<- easier to bring variable through this way
# from password import login, pin
# from search import search_a, seen
import search_c #<- easier to bring variable through this way
from asset_cat import as_cat
from speeds import fast_text, wait_text
from text_colours import *

#######################################
#                                     #
#          library imports            #
#                                     #
#######################################

import datetime
import os
import time
import sys

#######################################
#                                     #
#          variables                  #
#                                     #
#######################################

start_stamp=datetime.datetime.now()
ans=["1","2","3","4","5","6","7"]
pin="090477"
reboot_select=False

#######################################
#                                     #
#          function order             #
#                                     #
#######################################

def options():
    global pin, reboot_select
    if password.pass_changed and search_c.seen and reboot_select:
        fast_text(f"{bcolors.FAIL}***SYS PING PASSWORD REMOTE JOIN*** Incorrect password enter \nUser has 2 tries remaining \n{bcolors.ENDC} Please select from the following options: \n   1 - Access Asset Catalogue \n   2 - Add New Assets \n   3 - Access System Settings \n   4 - Search System \n   5 - Access Server Management Tools \n   6 - System Reboot\n   7 - Quit \nPlease input 1, 2, 3, 4, 5 or 6. Press 7 to quit \n {bcolors.FAIL}***SYS PING PASSWORD REMOTE JOIN*** Incorrect password enter \nUser has 1 tries remaining {bcolors.ENDC} \n\n{bcolors.FAIL}***SYS PING PASSWORD REMOTE JOIN*** Incorrect password enter \nUser has 0 tries remaining \n \n Fail2Ban Live Log: User 189.56.23.111 has been banned\n\n {bcolors.ENDC}")
        main_option=input("     >>    ")
    else:
        fast_text(f"Please select from the following options: \n   1 - Access Asset Catalogue \n   2 - Add New Assets \n   3 - Access System Settings \n   4 - Search System \n   5 - Access Server Management Tools \n   6 - System Reboot\n   7 - Quit \nPlease input 1, 2, 3, 4, 5 or 6. Press 7 to quit \n")
        main_option=input("     >>    ")

    while main_option not in ans:
        fast_text(f"{bcolors.WARNING}Unexpected input \nPlease Try Again {bcolors.ENDC} \nPlease type 1, 2, 3, 4, 5 or 6. Press 7 to quit \n")
        main_option=input("     >>    ")

    if main_option=="1":
        as_cat()# the random book title generator
        fast_text("What would you like to do? \n")
        options()
    elif main_option=="2":
        fast_text(f"{bcolors.FAIL}Adding new assets is disabled until 23/07/2022 \n{bcolors.ENDC}")
        fast_text("What would you like to do? \n")
        options()
    elif main_option=="3":
        password.login()# the login puzzle
        pin=password.pin
        if search_c.seen and password.pass_changed:
            fast_text(f"{bcolors.FAIL}***SYS PING PASSWORD REMOTE JOIN*** Incorrect password enter \nUser has 999 tries remaining {bcolors.ENDC}\n")
            time.sleep(2)
            fast_text(f"{bcolors.FAIL}***SYS PING PASSWORD REMOTE JOIN*** Incorrect password enter \nUser has 999 tries remaining {bcolors.ENDC}\n")
            fast_text(f"{bcolors.FAIL}***SYS PING PASSWORD REMOTE JOIN*** Incorrect password enter \nUser has 999 tries remaining {bcolors.ENDC}\n")
            time.sleep(2)
            fast_text(f"{bcolors.FAIL}***SYS PING PASSWORD REMOTE JOIN*** Incorrect password enter \nUser has 999 tries remaining {bcolors.ENDC}\n")   
        fast_text("What would you like to do? \n")
        options()
    elif main_option=="4":
        search_c.search_a(start_stamp) # the searching
        if search_c.seen and password.pass_changed:
            fast_text(f"{bcolors.FAIL}***SYS PING PASSWORD REMOTE JOIN*** Incorrect password enter \nUser has 999 tries remaining {bcolors.ENDC}\n")
            time.sleep(2)
            fast_text(f"{bcolors.FAIL}***SYS PING PASSWORD REMOTE JOIN*** Incorrect password enter \nUser has 999 tries remaining {bcolors.ENDC}\n")
            fast_text(f"{bcolors.FAIL}***SYS PING PASSWORD REMOTE JOIN*** Incorrect password enter \nUser has 999 tries remaining {bcolors.ENDC}\n")
            time.sleep(2)
            fast_text(f"{bcolors.FAIL}***SYS PING PASSWORD REMOTE JOIN*** Incorrect password enter \nUser has 999 tries remaining {bcolors.ENDC}\n")   
        fast_text("What would you like to do? \n")
        options()
    elif main_option=="5":
        print(f"{bcolors.WARNING}The Server Management Tools cannot be accessed remotely due to traffic overload. \nPlease access the Server Management Tools at location  {bcolors.ENDC}\n")
        time.sleep(30)
        fast_text("What would you like to do? \n")
        options()
    elif main_option=="6":
        fast_text(f"{bcolors.FAIL} **WARNING** System rebooting, please do not interupt power \n")
        wait_text(f". . . . . . {bcolors.ENDC}")
        os.system('cls' if os.name == 'nt' else 'clear')
        reboot_select=True
        intro()
    elif main_option=="7":
        fast_text("You will be logged out of the LCL system \n Thank you for using LCL System Management")
        sys.exit()
        
def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{bcolors.HEADER}

                                  
                                                            
                                            ..              
                                      :.    ::              
                                      ^..  ::.:             
                                     ::.: .:.:              
                   .:.^::^::...    .:....:..:.              
                   .....:^^^:    .::.......:.               
                .....   .^^^.  .:...... .::.                
                ..     .^^:..:.........:...                 
                    .:^^^. :. ......::....                  
                  ::!Y~:  ^. :^::. .:::..                   
                .^^7&7^. .: :^^::. .::..                    
               .^^^@#:^:.:.:^^^:. .::..                     
               ^^^^@&^^^^:^^^^:.  ....                      
               :^^:?@G^:^^....::::...                       
                :^^:!GB?~^^........                         
                 .:^^:~77~^^:..::..::.                      
                    ..:::^^^^^:. :  :^:                     
                      :::. .^^^.  :  .^:                    
                     .:^^^  :^^^. .   :^                    
                      .^:    .^:      ..                    
                     .^:      ^:      .                     
                    .^.       .^.                           
                .  ::          :^                           
              .:........   .:........                       
                                                            
                                                            
                                                            """
)
    fast_text(f"{bcolors.HEADER}               Welcome To\n Liverpool Central Library Server Management {bcolors.ENDC}\n\n")
    fast_text("Please enter the password\n")
    password=input("     >>    ")
    while password !=pin:
        fast_text(f"{bcolors.FAIL}Incorrect, please try again \nYou have 999 tries remaining {bcolors.ENDC}\n")
        password=input("     >>    ")

    wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
    print(f"{bcolors.OKGREEN} Access Granted \n \n Welcome Admin {bcolors.ENDC}\n\n")
    options()

intro()