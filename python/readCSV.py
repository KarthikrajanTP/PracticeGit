import csv
multi_row = [
    [1,'Karthik'],
    [2,'Sibi']
]

name = open('names.csv','w',newline='')
writer = csv.writer(name,delimiter=',')
writer.writerows(multi_row)