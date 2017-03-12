import csv

borough_data = {}

class BoroughData:
    def __init__(self, name, recycling_day, recycling_frequency, general_waste_days, general_waste_frequency, food_waste_days, food_waste_frequency, materials_provided, contact):
        self.name = name
        self.recycling_day = recycling_day
        self.recycling_frequency = recycling_frequency
        self.general_waste_days = general_waste_days
        self.general_waste_frequency = general_waste_frequency
        self.food_waste_days = food_waste_days
        self.food_waste_frequency = food_waste_frequency
        self.materials_provided = materials_provided
        self.contact = contact

def find_BoroughData(boroughName):
   	return borough_data.get(boroughName)

def main():

    load_data()

    stored_borough_data = borough_data.get('')

    print stored_borough_data.recycling_day
    print stored_borough_data.recycling_frequency
    print stored_borough_data.general_waste_days
    print stored_borough_data.general_waste_frequency
    print stored_borough_data.food_waste_days
    print stored_borough_data.food_waste_frequency
    print stored_borough_data.materials_provided
    print stored_borough_data.contact

def load_data():
    with open('library.csv', 'rU') as f:

        reader = csv.reader(f)

        for row in reader:

            a_borough_data = BoroughData(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

            borough_data[str(a_borough_data.name).lower()] = a_borough_data

if __name__ == '__main__':
    main()
