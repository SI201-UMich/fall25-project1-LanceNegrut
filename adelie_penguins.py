# Name: Lance Negrut
# Student ID: 70298465
# Email: lnegrut@umich.edu
# Collaborators: Gemini (I’m not working with other classmates on this project)

import csv
import unittest

def load_data(inFile):
    data = []
    with open(inFile, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            for key in ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']:
                if row[key] and row[key] != 'NA':
                    row[key] = float(row[key])
                else:
                    row[key] = None
            if row.get('sex') and row['sex'] == 'NA':
                    row['sex'] = None
            data.append(row)
    return data  

def specific_species(data, species):
    specific_species_ls = []
    for penguin in data:
        if penguin['species'] == species:
            specific_species_ls.append(penguin)
    return specific_species_ls

def specific_island(data, island):
    specific_island_ls = []
    for penguin in data:
        if penguin['island'] == island:
            specific_island_ls.append(penguin)
    return specific_island_ls

def calculate_averages(data):
    unique_islands = []
    for penguin in data:
        island_name = penguin['island']
        if island_name is not None and island_name not in unique_islands:
            unique_islands.append(island_name)
    adelie_penguins = specific_species(data, 'Adelie')
    averages = {}
    for island in unique_islands:
        adelie_on_this_island = specific_island(adelie_penguins, island)
        if adelie_on_this_island:
            total_mass = 0
            count = 0
            for penguin in adelie_on_this_island:
                if penguin['body_mass_g'] is not None:
                    total_mass += penguin['body_mass_g']
                    count += 1
            if count > 0:
                average = total_mass / count
                averages[island] = round(average, 2)   
    return averages

def specific_sex(data, sex):
    specific_sex_ls = []
    for penguin in data:
        if penguin['sex'] == sex:
            specific_sex_ls.append(penguin)
    return specific_sex_ls

def find_min(data, column):
    if not data:
        return None
    min = None
    for item in data:
        value = item.get(column)
        if value is not None:
            if min is None or value < min:
                min = value
    return min

def find_max(data, column):
    if not data:
        return None
    max = None
    for item in data:
        value = item.get(column)
        if value is not None:
            if max is None or value > max:
                max = value
    return max

def calculate_ranges(data):
    unique_sexes = []
    for penguin in data:
        sex_name = penguin['sex']
        if sex_name is not None and sex_name not in unique_sexes:
            unique_sexes.append(sex_name)
    adelie_penguins = specific_species(data, 'Adelie')
    ranges = {}
    for sex in unique_sexes:
        adelie_of_sex = specific_sex(adelie_penguins, sex)
        min_flipper = find_min(adelie_of_sex, 'flipper_length_mm')
        max_flipper = find_max(adelie_of_sex, 'flipper_length_mm')
        if min_flipper is not None and max_flipper is not None:
            calculated_range = max_flipper - min_flipper
            ranges[sex] = {
                'min': min_flipper,
                'max': max_flipper,
                'range': round(calculated_range, 2)
            }        
    return ranges

def generate_findings(averages, ranges):
    with open('penguin_analysis.txt', 'w') as f:
        f.write("Data Analysis: Size of Adélie Penguins\n")
        f.write("============================\n\n")
        f.write("Calculation 1: For each island, the average body mass(g) of Adélie penguins\n")
        f.write("-----------------------------------------------------------------\n")
        for island, avg_mass in averages.items():
            f.write(f"- {island}: {avg_mass}g\n")
        f.write("\nCalculation 2: For each sex, the range of flipper length(mm) of Adélie penguins\n")
        f.write("---------------------------------------------------------------------\n")
        for sex, range_data in ranges.items():
            f.write(f"- {sex}: {range_data['range']}mm (Min: {range_data['min']}, Max: {range_data['max']})\n")
        f.write("\n(calculations are based on a dataset and not the entire population of Adélie Penguins)\n")

    file_name = "penguin_analysis.txt"
    with open(file_name, "r") as f:
        content = f.read()
        print(content)

class myTests(unittest.TestCase):
    def setUP(self):
        self.inFile = open("penguins.csv")
        self.csv_file = csv.reader(self.inFile)
        self.data = load_data(self.csv_file)
        self.averages = calculate_averages(self.data)
        self.ranges = calculate_ranges(self.data)
        pass
    
    def test_calculate_averages(self):
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        pass

    def test_find_min(self):
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        pass

    def test_find_max(self):
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        pass

    def test_calculate_ranges(self):
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        pass

def main():
    data = load_data("/Users/lance/Desktop/SI201/fall25-project1-LanceNegrut/penguins.csv")
    averages = calculate_averages(data)
    ranges = calculate_ranges(data)
    generate_findings(averages, ranges)
    unittest.main(verbosity=2)

if __name__ == "__main__":
    main()