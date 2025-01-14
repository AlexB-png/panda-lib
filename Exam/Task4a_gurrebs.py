import pandas as pd
import matplotlib.pyplot as plt

# Displays the main menu and collects choice of menu item


def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Return a graph of the sales that have been made in a day")
        print("3. Print averages of a product over a time period")
        print("4. Calculate Highest/Lowest sales of one product")
        print("5. Graph to compare sale of every product")
        print("6. SORT")
        print("###############################################")

        main_menu_choice = input("Please enter the number of your choice (1-6): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 6:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

# Menu item selection form user and validates it

def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")
        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]
        item_choice = input("Please enter the number of your choice (1-8): ")
        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name

# Gets user input of start of date range
# Converts to a date to check data entry is in correct format and then returns it as a string

def get_start_date():
    flag = True
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    return start_date

# Gets user input of end of date range
# Converts to a date to check data entry is in correct format and then returns it as a string


def get_end_date():
    flag = True
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    return end_date


# imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv("Task4a_data.csv") 
    df4 = pd.read_csv("Task4a_data.csv", usecols=["Menu Item","Service"])
    df4 = df4.loc[df4["Menu Item"] == item]
    df2 = df1.loc[df1['Menu Item'] == item]
    df3 = df2.loc[:, startdate:enddate]
    # df3 = pd.concat([df4,df3],axis=1)
    # df3 = df3.align(other=,axis=1)
    return df3


main_menu = menu()
if main_menu == 1:
    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
    extracted_data = get_selected_item(item, start_date, end_date)
    print("Here is the sales data for {} between dates {} and {}:".format(item, start_date, end_date))
    print("")
    extract_no_index = extracted_data.to_string(index=False)
    df4 = pd.read_csv("Task4a_data.csv", usecols=["Menu Item","Service"])
    df4 = df4.loc[df4["Menu Item"] == item]
    extracted_data = pd.concat([df4, extracted_data], axis=1)
    extracted_data = extracted_data.sum()
    extracted_data = extracted_data.drop(["Menu Item", 'Service'])
    print("The total amount of that product sold is ...")
    print(extracted_data.sum())
elif main_menu == 2:
    print("Calculating. . .")
    flag = True
    product = input("What Product")
    while flag is True:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    flag = True
    while flag is True:
        end_date = input('Please enter End date for your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    Data = pd.read_csv("Task4a_data.csv")
    code = Data.loc[Data["Menu Item"] == product]
    Lunch = code.loc[code["Service"] == "Lunch"]
    Dinner = code.loc[code["Service"] == "Dinner"]
    DataFrameLunch = Lunch.loc[:, start_date:end_date]
    DataFrameLunch = DataFrameLunch.sum()
    DataFrameDinner = Dinner.loc[:, start_date:end_date]
    DataFrameDinner = DataFrameDinner.sum()
    print(DataFrameLunch)
    print("")
    print(DataFrameDinner)
    plt.xlabel("Day")
    plt.title("Red = Lunch / Blue = Dinner")
    plt.ylabel("Sales")
    plt.plot(DataFrameLunch, color="red")
    plt.plot(DataFrameDinner, color="blue")
    plt.xscale('linear')
    plt.show()
elif main_menu == 3:
    product = input("What Product")
    flag = True
    while flag is True:
        start_date = input('Please enter start date for' 
                        'your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    flag = True
    while flag is True:
        end_date = input('Please enter End date for' 
                        'your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    Data = pd.read_csv("Task4a_data.csv")
    Data = Data.loc[Data["Menu Item"] == product]
    Data = Data.loc[Data["Service"] == "Lunch"]
    Data = Data.loc[:, start_date:end_date]
    # Data = Data.drop(axis=1,columns=["Menu Item","Service"])
    print(Data)
    print("The Average of those days is...")
    print(Data.mean(axis=1))
elif main_menu == 4:
    flag = True
    while flag == True:
        start_date = input('Please enter start' 
                        'date for your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    flag = True
    while flag == True:
        end_date = input('Please enter End' 
                        'date for your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    Data = pd.read_csv("Task4a_data.csv")
    info = pd.read_csv("Task4a_data.csv", usecols=['Menu Item', 'Service'])
    Data = Data.loc[:, start_date:end_date]
    # print(Data)
    df3 = pd.concat([info, Data],axis=1)
    Lunch = df3.loc[df3["Service"] == 'Lunch']
    Dinner = df3.loc[df3['Service'] == 'Dinner']
    product = input("Input a product")
    time = input("Lunch or Dinner")
    while product != "STOP":
        if time == "Lunch":
            x = Lunch.loc[Lunch["Menu Item"] == product]
            x = x.drop(['Menu Item', 'Service'], axis='columns')
            x = x.sum()
            print(x)
            plt.plot(x, color='blue')
            plt.xlabel("Date")
            plt.ylabel("Sales")
            plt.xscale('linear')
            plt.title('This Graph shows how the'
            'sales of selected product have sold')
            plt.show()
            time = input("Lunch or Dinner")
            product = input("Input a product or STOP to stop")
        elif time == "Dinner":
            x = Dinner.loc[Dinner["Menu Item"] == product]
            print(x)
            time = input("Lunch or Dinner")
            product = input("Input a product or STOP to stop")
        else:
            print("Error")
            time = input("Lunch or Dinner")
elif main_menu == 5:
    flag = True
    while flag is True:
        start_date = input('Please enter start' 
                        'date for your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    flag = True
    while flag == True:
        end_date = input('Please enter End' 
                        'date for your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    time = input("Lunch or Dinner")
    Data = pd.read_csv("Task4a_data.csv")
    Nachos = Data.loc[:, start_date:end_date]
    Nachos = Nachos.loc[Data["Menu Item"] == "Nachos"] 
    Nachos = Nachos.loc[Data["Service"] == time].sum()
    Soup = Data.loc[:, start_date:end_date]
    Soup = Soup.loc[Data["Menu Item"] == "Soup"] 
    Soup = Soup.loc[Data["Service"] == time].sum()
    Burger = Data.loc[:, start_date:end_date]
    Burger = Burger.loc[Data["Menu Item"] == "Burger"] 
    Burger = Burger.loc[Data["Service"] == time].sum()
    Brisket = Data.loc[:, start_date:end_date]
    Brisket = Brisket.loc[Data["Menu Item"] == "Brisket"] 
    Brisket = Brisket.loc[Data["Service"] == time].sum()
    Ribs = Data.loc[:, start_date:end_date]
    Ribs = Ribs.loc[Data["Menu Item"] == "Ribs"] 
    Ribs = Ribs.loc[Data["Service"] == time].sum()
    Corn = Data.loc[:, start_date:end_date]
    Corn = Corn.loc[Data["Menu Item"] == "Corn"] 
    Corn = Corn.loc[Data["Service"] == time].sum()
    Fries = Data.loc[:, start_date:end_date]
    Fries = Fries.loc[Data["Menu Item"] == "Fries"] 
    Fries = Fries.loc[Data["Service"] == time].sum()
    Salad = Data.loc[:, start_date:end_date]
    Salad = Salad.loc[Data["Menu Item"] == "Salad"] 
    Salad = Salad.loc[Data["Service"] == time].sum()

    print("y for Yes / n for No")
    x = input("Nachos?")
    if x == "y":
        plt.plot(Nachos, color="yellow")
        print("Nachos = Yellow")
    x = input("soup?")
    if x == "y":
        plt.plot(Soup, color="brown")
        print("Soup = Brown")
    x = input("Burger?")
    if x == "y":
        plt.plot(Burger, color="orange")
        print("Burger = Orange")
    x = input("Brisket?")
    if x == "y":
        plt.plot(Brisket, color="purple")
        print("Brisket = Purple")
    x = input("Ribs?")
    if x == "y":
        plt.plot(Ribs, color="grey")
        print("Ribs = grey")
    x = input("Corn?")
    if x == "y":
        plt.plot(Corn, color="blue")
        print("Corn = Blue")
    x = input("Fries?")
    if x == "y":
        plt.plot(Fries, color="black")
        print("Fries = Black")
    x = input("Salad?")
    if x == "y":
        plt.plot(Salad, color='green')
        print("Salad = Green")
    plt.xscale('linear')
    plt.show()
elif main_menu == 6:
    product = input("What Product")
    flag = True
    while flag is True:
        start_date = input('Please enter start date for' 
                        'your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    flag = True
    while flag is True:
        end_date = input('Please enter End date for' 
                        'your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    Data = pd.read_csv("Task4a_data.csv")
    Data = Data.loc[Data["Menu Item"] == product]
    time = input("Dinner or lunch")
    Data = Data.loc[Data["Service"] == time]
    Data = Data.drop(["Menu Item","Service"],axis=1).sum()
    Data = Data.sort_values()
    print(Data)


else:
    print('This part of the program is still under development')

