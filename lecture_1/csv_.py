import csv

data = [
       ["Name", "Age", "City"],
         ["Alice", 30, "New York"],
         ["Bob", 25, "Los Angeles"],
         ["Charlie", 35, "Chicago"],
        ["Alice", 30, "New York"],
         ["Bob", 25, "Los Angeles"],
         ["Charlie", 35, "Chicago"]
]


with open('people.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(data[0])  # Write the header
    writer.writerows(data[1:])  # Write the remaining rows


import pandas as pd
df = pd.read_csv('people.csv')

print(df)
# print(df[["Name", "City"]])
# print('\n')
#
# print(df[df['Age']>30])