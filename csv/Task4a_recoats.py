import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Outputs the initial menu and checks validates the input
def main_menu():
    flag = True

    while flag:

        print("############## Recoats Adventure Park ##############")

        print("")
        print("########### Please select an option ################")
        print("### 1. Total income by source")
        print("### 2. Sort by payment types")
        print("### 3. Admin password")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            
            if choice != "1" and choice != "2" and choice != "3":
                print('Choice not accepted!')
                
            else:
                print("Choice accepted")
                flag = False

    return choice

# Submenu for totals, provides type check validation for the input
def total_menu ():
    flag = True
    while flag:
        print("############## Total income by source ##############")
        print("")
        print("########## Please select an income source ##########")
        print("### 1. Tickets")   
        print("### 2. Gift Shop") 
        print("### 3. Snack Stand")  
        print("### 4. Pictures")

        choice = input('Enter your number selction here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            if int(choice) <= 0 or int(choice) >=5:
                print("Not within range")
            else:
                print('Choice accepted!')
                flag = False

    return choice   

# takes the total submenu input and converts the number to a string of the source name
def convert_total_men_coice(total_men_choice):
    if total_men_choice == "1":
        tot_choice = "Tickets"
    elif total_men_choice == "2":
        tot_choice = "Gift Shop"
    elif total_men_choice == "3":
        tot_choice= "Snack Stand"
    elif total_men_choice == "4":
        tot_choice = "Pictures"
    else:
        tot_choice = "Fail"
        print("INVALID")
        
    
    return tot_choice

# creates a new dataframe with the selected income source then creates a total row
# outputs the final total in a message
def get_total_data(total_choice):
    
    df = pd.read_csv("Task4a_data.csv")
    
    income = df[["Day", total_choice]]

    total = income[total_choice].sum()

    msg = "The total income from {} was: £{}".format(total_choice, total)
    return msg

def Payment_Type():
    df = pd.read_csv("Task4a_data.csv")
    df.sort_values(["Tickets"]).groupby(["Pay Type","Day"]).sum()
    day = input("What day should you sort by?")
    c=df[df["Day"]==day]
    print(c)
    df.plot(subplots=False, figsize=(6, 6)); plt.legend(loc='best')
    df.plot(subplots=True, figsize=(6, 6)); plt.legend(loc='best')
    
    plt.xticks(np.arange(0, 70, step=10), labels=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
    
    plt.show()

def Admin():
    Admin = input("Whats the admin password")
    if Admin == "Password1":
        print("Correct")
        df = pd.read_csv("Task4a_data.csv")
        import time
        import os
        #tick = sumdf.sort_values(by=["Tickets"],ascending=True)
        #gift = df.sort_values(by=["Gift Shop"],ascending=True)
        #snack = df.sort_values(by=["Snack"],ascending=True)
        #pic = df.sort_values(by=["Pictures"],ascending=True)
        #tick.plot(subplots=False, figsize=(6, 6)); plt.legend(loc='best')
        #gift.plot(subplots=False, figsize=(6, 6)); plt.legend(loc='best')
        #snack.plot(subplots=False, figsize=(6, 6)); plt.legend(loc='best')
        #pic.plot(subplots=False, figsize=(6, 6)); plt.legend(loc='best')
        
        df.plot(subplots=False, figsize=(6, 6)); plt.legend(loc='best')
        df.plot(subplots=True, figsize=(6, 6)); plt.legend(loc='best')
        
        plt.xticks(np.arange(0, 70, step=10), labels=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
        
        plt.show()
        
        #time.sleep(5)
        sumdf = df.sort_values(by=["Day"],ascending=True)
        print(sumdf)
        #time.sleep(5)

        day = input("What day should you sort by?")
        c=df[df["Day"]==day]
        print("\n")
        print("Tickets sorted")
        print(c.sort_values(by=["Tickets"]))
        time.sleep(5)
        os.system("CLS")
        print("Gift sorted")
        print(c.sort_values(by=["Gift Shop"]))
        time.sleep(5)
        os.system("CLS")
        print("Snack sorted")
        print(c.sort_values(by=["Snack Stand"]))
        time.sleep(5)
        os.system("CLS")
        print("Picture sorted")
        print(c.sort_values(by=["Pictures"]))
        time.sleep(5)
        os.system("CLS")


main_menu_choice = main_menu()
if main_menu_choice == "1":
    total_men_choice = total_menu()
    try:
        total_choice = convert_total_men_coice(total_men_choice)
        print(get_total_data(total_choice))
    except:
        print("")
elif main_menu_choice == "2":
    Payment_Type()
elif main_menu_choice == "3":
    Admin()


