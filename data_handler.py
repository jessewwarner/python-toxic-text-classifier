import pandas
import zipfile

# Returns data from a csv file within a zipfile as a pandas.read_csv object.
def get_csv_from_zip(zip_file, csv_file):
    # Extract the data from the CSV files within the zip file.
    with zipfile.ZipFile(zip_file, 'r') as train_zip:
        with train_zip.open(csv_file) as train_file:
            csv_data = pandas.read_csv(train_file)

    return csv_data