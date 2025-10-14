# Name: Lance Negrut
# Student ID: 70298465
# Email: lnegrut@umich.edu
# Collaborators: Gemini (I’m not working with other classmates on this project)

import csv
import unittest

def load_data(csv_file):
    pass  

def specific_species(data, species):
    pass

def specific_island(data, island):
    pass

def calculate_averages(data):
    pass

def specific_sex(data, sex):
    pass

def find_min(data, column):
    pass

def find_max(data, column):
    pass

def calculate_ranges(data):
    pass

def generate_findings(averages, ranges):
    pass

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
    inFile = open("penguins.csv")
    csv_file = csv.reader(inFile)
    unittest.main(verbosity=2)

if __name__ == "__main__":
    main()