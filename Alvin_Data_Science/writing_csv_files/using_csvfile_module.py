import csv

data = [['Name', 'Age'],['Alice', 20],['Ben', 24]]

with open('output.csv', 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerows(data)