import pandas as pd
import os
os.system('CLS')

def average_score():
    x = data3.groupby(['Name','Subject','Attendance'])["Score"].mean()
    print("#####")
    print("The average score")
    print(x)
    print("\n")

def average_attendance():
    y=data3.groupby(['Name'])["Attendance"].mean()
    print("#####")
    print("The average attendance")
    print(y)
    print("\n")

def total_score():
    z=data3["Score"].mean()
    print("#####")
    print("The average of all of the scores is..")
    print(z)
    print("\n")

def total_subject():
    z=data3.groupby(["Subject"])["Score"].mean()
    print("#####")
    print("The average of each subject is..")
    print(z)
    print("\n")

data2 = ({'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob', 'Charlie'],
                    'Subject': ['Math', 'Math', 'Math', 'Math', 'English', 'English', 'English'],
                    'Score': [80, 90, 75, 85, 85, 88, 92],
                    'Attendance': [90, 95, 80, 92, 88, 93, 78]})

data3 = pd.DataFrame(data2)

average_score()

average_attendance()

total_score()

total_subject()