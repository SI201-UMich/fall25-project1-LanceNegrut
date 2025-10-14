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
    pass

def specific_sex(data, sex):
    specific_sex_ls = []
    for penguin in data:
        if penguin['sex'] == sex:
            specific_sex_ls.append(penguin)
    return specific_sex_ls

def find_min(data, column):
    pass

def find_max(data, column):
    pass

def calculate_ranges(data):
    pass

def generate_findings(averages, ranges):
    with open('adelie_analysis.txt', 'w') as f:
        f.write("Penguin Analysis Report\n")
        f.write("========================\n\n")
        
        f.write("Average Body Mass (g) by Species:\n")
        for species, avg_mass in averages.items():
            f.write(f"- {species}: {avg_mass}g\n")
            
        f.write("\nBill Length Range (mm) by Island:\n")
        for island, range_data in ranges.items():
            f.write(f"- {island}: {range_data['range']}mm (Min: {range_data['min']}, Max: {range_data['max']})\n")

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