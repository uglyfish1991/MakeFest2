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

#######################################
#                                     #
#          variables                  #
#                                     #
#######################################

pin="090477"
done_before=False
login_stamp=datetime.datetime.now()
pass_changed=False

#######################################
#                                     #
#          function start             #
#                                     #
#######################################

def login():
    global pin, done_before, log_pin, new_pin, pass_changed
    fast_text("Sys Login: \n")
    log_pin=input("     >>    ")


    while log_pin !=pin:
        fast_text(f"{bcolors.FAIL}Incorrect, please try again \nYou have 999 tries remaining {bcolors.ENDC}\n")
        log_pin=input("     >>    ")
    
    if done_before:
        fast_text(f"{bcolors.WARNING}Password changed successfully. Returning to main menu \n\n{bcolors.ENDC}")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        pass_changed=True
        return pin, pass_changed

    fast_text(f"{bcolors.WARNING}         **WARNING** \nChanges made here will impact the whole system \nYou may need to log in again after making changes\n {bcolors.ENDC} \n")
    fast_text(f"{bcolors.WARNING}         **NOTE** \nPasswords should be changed regularly.\n Your password was last changed {bcolors.OKGREEN}0 months 0 weeks 0 days 0 hours and 2 minutes ago \n {bcolors.ENDC}")
    wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
    fast_text(f"{bcolors.WARNING}Accessing System Root Password Settings \nCurrent Permissions: \n\n{bcolors.ENDC}")
    print(f"""{bcolors.OKGREEN} if password=="{pin}":
            allow_access(True) {bcolors.ENDC}\n""")
    fast_text("What would you like to change the password to?\n")
    new_pin=input("     >>    ")
    fast_text("Please confirm the password\n")
    new_pin_again=input("     >>    ")
    while new_pin != new_pin_again:
        fast_text(f"{bcolors.FAIL} ***ERRORR** passwords did not match \n {bcolors.ENDC}")
        fast_text("What would you like to change the password to? \n")
        new_pin=input("     >>    ")
        fast_text("Please confirm the password\n")
        new_pin_again=input("     >>    ")

    if new_pin==new_pin_again:
        pin=new_pin
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"{bcolors.WARNING}Current Permissions: \n{bcolors.ENDC}")
        print(f"""{bcolors.OKGREEN} if password=="{pin}":
        allow_access(True) {bcolors.ENDC}\n\n""")
        fast_text(f"{bcolors.OKGREEN} You have successfully changed the password {bcolors.ENDC} \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text("Please log in again with the new password\n\n")
        done_before=True
        login()

#login() remember to comment out this line when going back to main.py