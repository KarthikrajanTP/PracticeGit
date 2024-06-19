import csv
dict_file = open("names.csv")
reader = csv.DictReader(dict_file)

for data in reader:
    print(data)