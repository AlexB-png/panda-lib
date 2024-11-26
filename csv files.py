import pandas as pd
import os
test = {
    'English': ["100","81","72"],
    'Maths': ["72","64","32"]
}
x = pd.DataFrame(test, index=["1","2","3"])
print(x)
print("\n")
input = input("What row do you want?")
os.system('CLS')
print(x.iloc[int(input)-1])

x.to_csv("Test.csv", encoding='utf-8', index=False)