import os
import csv


def is_equal_to(arr1: list[str], arr2: list[str]) -> bool:
   return arr1 == arr2

#fonction par IA
def load_csv(file: str, delimiter: str = ',') -> tuple[list[str], list[list[str]]]:
    """Load a CSV file and validate its structure and content."""
    if not os.path.isfile(file):
        raise FileNotFoundError(f"CSV file '{file}' does not exist.")

    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        rows = list(reader)

    if not rows:
        raise ValueError(f"CSV file '{file}' is empty.")
    if len(rows[0]) != 4:
        raise ValueError(f"CSV file '{file}' must contain exactly 4 columns in the header.")
    if len(rows) < 2:
        raise ValueError(f"CSV file '{file}' must contain at least one data row.")

    # Add an extra column to the header
    header = rows[0] + ['département']

    # Process rows with validation
    data = []
    for row in rows[1:]:
        if len(row) < 4:
            raise ValueError(f"Row has insufficient columns: {row}")
        try:
            # Convert only the numeric columns to float
            row_data = [
                int(row[0]),  # Convert product_id to int
                row[1],  # Keep product_name as a string
                int(row[2]),  # Convert quantity to int
                float(row[3]),  # Convert price to float
                os.path.splitext(file)[0]  # Add filename as a new column
            ]
            data.append(row_data)
        except ValueError as e:
            raise ValueError(f"Invalid data in row {row}: {e}")

    return header, data

#fonction améliorée par IA
def write_csv(file: str, data: list[list[str]], header: list[str], limiter: str = ',') -> None:
    print(f"Vérification de l'existence de {file} dans {os.getcwd()}...")
    if file in os.listdir('.'):
        print(f"Fichier {file} existe.")
        choix = None
        while choix not in {'yes', 'no'}:
            choix = input('Warning: file exists. Would you overwrite it? (yes/no): ')
        if choix == 'no':
            print("Opération annulée par l'utilisateur.")
            return
    print(f"Écriture dans le fichier {file}...")
    with open(file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=limiter)
        csv_writer.writerow(header)
        csv_writer.writerows(data)
    print(f"Fichier {file} écrit avec succès.")



#fonction par IA
def merge_csv(files: list[str], data: list[list[str]], header: list[str]) -> tuple[list[str], list[list[str]]]:
    for file in files:
        h, d = load_csv(file)
        if not header:
            header, data = h, d
        elif is_equal_to(h, header):
            data.extend(d)
        else:
            raise AttributeError("header does not match between csv file")
    return header, data

#fonction par IA
def sort_data(data: list[list[str]], header: list[str], column: str, reverse: bool = False) -> list[list[str]]:
    if column not in header:
        raise ValueError(f"Column {column} not found in header")
    return sorted(data, key=lambda x: x[header.index(column)], reverse=reverse)