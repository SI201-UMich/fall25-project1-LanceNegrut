# Name: Lance Negrut
# Student ID: 70298465
# Email: lnegrut@umich.edu
# Collaborators: Gemini (I’m not working with other classmates on this project. I wrote every function.)
# GenAI Usage: Sought out revision recommendations for my decomposition diagram after I completed a strong draft, generated sample code for each of my functions after developing the structure of my program on my own (critically examining what was generated and making adjustments where needed). I utilized the Discussion 7 assignment and the CSV Runestone assignments as a starting point for my code before I used any GenAI. 

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

# --- UNCOMMENT TO PRINT FILE TEXT ---
#    file_name = "penguin_analysis.txt"
#    with open(file_name, "r") as f:
#        content = f.read()
#        print(content)

class myTests(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {'species': 'Adelie', 'island': 'Torgersen', 'body_mass_g': 4000.0, 'sex': 'Male', 'flipper_length_mm': 200.0},
            {'species': 'Adelie', 'island': 'Torgersen', 'body_mass_g': 3800.0, 'sex': 'Male', 'flipper_length_mm': 190.0},
            {'species': 'Adelie', 'island': 'Biscoe', 'body_mass_g': 3500.0, 'sex': 'Female', 'flipper_length_mm': 180.0},
            {'species': 'Adelie', 'island': 'Biscoe', 'body_mass_g': 3300.0, 'sex': 'Female', 'flipper_length_mm': 172.0},
            {'species': 'Gentoo', 'island': 'Biscoe', 'body_mass_g': 5000.0, 'sex': 'Male', 'flipper_length_mm': 220.0},
            {'species': 'Adelie', 'island': 'Dream', 'body_mass_g': None, 'sex': None, 'flipper_length_mm': None}
        ]

    def test_averages_torgersen(self):
        averages = calculate_averages(self.test_data)
        self.assertEqual(averages['Torgersen'], 3900.0)

    def test_averages_biscoe(self):
        averages = calculate_averages(self.test_data)
        self.assertEqual(averages['Biscoe'], 3400.0)

    def test_averages_no_adelie(self):
        data = [{'species': 'Gentoo', 'island': 'Biscoe', 'body_mass_g': 5000.0}]
        self.assertEqual(calculate_averages(data), {})

    def test_averages_empty_list(self):
        self.assertEqual(calculate_averages([]), {})

    def test_ranges_general_male(self):
        ranges = calculate_ranges(self.test_data)
        self.assertEqual(ranges['Male']['range'], 10.0)

    def test_ranges_general_female(self):
        ranges = calculate_ranges(self.test_data)
        self.assertEqual(ranges['Female']['range'], 8.0)
        self.assertEqual(ranges['Female']['min'], 172.0)

    def test_ranges_no_males(self):
        data = [{'species': 'Adelie', 'sex': 'Female', 'flipper_length_mm': 180.0}]
        ranges = calculate_ranges(data)
        self.assertNotIn('Male', ranges)
        self.assertIn('Female', ranges)

    def test_ranges_no_flipper_data(self):
        data = [{'species': 'Adelie', 'sex': 'Male', 'flipper_length_mm': None}]
        ranges = calculate_ranges(data)
        self.assertEqual(ranges, {})

def main():
    data = load_data("/Users/lance/Desktop/SI201/fall25-project1-LanceNegrut/penguins.csv")
    averages = calculate_averages(data)
    ranges = calculate_ranges(data)
    generate_findings(averages, ranges)
    unittest.main(verbosity=2)

if __name__ == "__main__":
    main()