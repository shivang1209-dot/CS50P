import sys
import random
import csv
import datetime

class Hat:
    houses = ["Gryffindor","Ravenclaw","Hufflepuff","Slytherin"]
    @classmethod
    def sort(cls,name):
        return random.choice(cls.houses)
    
def main():

    validate_input()
    info = []
    output = []
    try:
        with open(sys.argv[1],"r") as data:
            reader = csv.DictReader(data)
            for row in reader:
                info.append(row)
    except FileNotFoundError:
        sys.exit("Input File Doesn't Exist")

    for row in info:
        house = assign_house(row["name"])
        age = calculate_age(row["birthyear"])
        output.append({"name" : row["name"],"house" : house, "age" : age,"programme" : row["programme"]})
    
    with open(sys.argv[2],"w") as file:
        writer = csv.DictWriter(file, fieldnames = ["name","house","age","programme"])
        writer.writerow({"name": "name", "house" : "house", "age" : "age", "programme" : "programme"})
        for row in output:
            writer.writerow({"name" : row["name"],"house" : row["house"], "age" : row["age"], "programme" : row["programme"]})


def validate_input():
    if len(sys.argv) < 3:
        sys.exit("Very Few Command- Line Arguments \nTry: python file_name input_file output_file")
    if len(sys.argv) > 3:
        sys.exit("Too Many Command-Line Arguments \nTry: python file_name input_file output_file")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not Enough CSV Files Found")

def assign_house(name):
    house = Hat.sort(name)
    return house
    
def calculate_age(birthyear):
    age = datetime.date.today().year - int(birthyear)
    return age

main()