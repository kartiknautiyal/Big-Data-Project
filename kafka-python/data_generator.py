import random 
import string
import csv 
import json
import os 

def generate_message():
    absolute_path = os.path.dirname(__file__)
    relative_path = "../crime_rate_Spain.csv"
    full_path = os.path.join(absolute_path, relative_path)

    with open(full_path,encoding = 'utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            yield row 

# # test 
# if __name__ == '__main__':
#     gen = generate_message()
#     print(generate_message())
#     print(next(gen))