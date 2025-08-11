import glob
import pandas as pd

# Read Rows from CSV File
def read_csv_file(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        return list(csv.reader(file))


# Write Rows to CSV File

def write_to_csv_file(filename, rows):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)

        writer.writerows(rows)


# Load Multiple CSV to dataframe
csv_files = glob.glob("/content/sample_data/*.csv")

df = [pd.read_csv(filename) for filename in csv_files]


