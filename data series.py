import pandas
myvar= [10,20,30]



panda=pandas.Series(myvar, index=["one","two","three"])

#prints the entire list
#print(panda)

#Prints first variable in the list
#print(panda[0])

#prints the value under the index#
print(panda["one"])