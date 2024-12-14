import os
import cmd
from utils import load_csv, is_equal_to, sort_data, write_csv


def display_data(data, header):
    """Display tabular data with proper alignment."""
    if not data or not header:
        print("No data available to display.")
        return

    col_widths = [max(len(str(item)) for item in col) + 5 for col in zip(header, *data)]

    print(" | ".join(f"{title:<{width}}" for title, width in zip(header, col_widths)))
    print("-" * (sum(col_widths) + len(header) * 3))

    for row in data:
        print(" | ".join(f"{str(item):<{width}}" for item, width in zip(row, col_widths)))


class CsvManager(cmd.Cmd):
    """Interactive command-line CSV manager."""
    intro = "Welcome to the CSV Manager! Type 'help' or '?' to list commands."
    prompt = "CSV> "

    def __init__(self):
        super().__init__()
        self.data = []
        self.header = []

    def do_exit(self, _):
        """Exit the program."""
        print("Exiting CSV Manager. Goodbye!")
        return True

    def do_add(self, filepath):
        """Add and merge a CSV file to the dataset. Usage: add <filepath>"""
        filepath = os.path.abspath(filepath.strip() or self._choose_file())
        if not filepath:
            print("No file specified.")
            return

        try:
            header, data = load_csv(filepath)
            if not self.header:
                self.header = header
                self.data.extend(data)
            elif is_equal_to(header, self.header):
                self.data.extend(data)
            else:
                print("Error: CSV headers do not match.")
        except Exception as e:
            print(f"Failed to add CSV file: {e}")

    def do_view(self, _):
        """View the current dataset."""
        display_data(self.data, self.header)

    def do_sort(self, column_name):
        """Sort the dataset by a specified column. Usage: sort <column_name>"""
        column_name = column_name.strip() or self._choose_column()
        if column_name not in self.header:
            print(f"Column '{column_name}' not found in header.")
            return

        reverse = input("Sort in descending order? (y/n): ").lower() == 'y'
        try:
            self.data = sort_data(self.data, self.header, column_name, reverse)
            print("Dataset sorted.")
        except Exception as e:
            print(f"Failed to sort data: {e}")

    def do_export(self, filename):
        """Export the dataset to a CSV file. Usage: export <filename>"""
        filename = filename.strip() or input("Enter filename for export: ")
        if not filename.endswith('.csv'):
            print("Filename must end with '.csv'.")
            return

        try:
            write_csv(filename, self.data, self.header)
            print(f"Data exported to '{filename}'.")
        except Exception as e:
            print(f"Failed to export data: {e}")

    def _choose_file(self):
        """Prompt user to choose a CSV file from the current directory."""
        files = [f for f in os.listdir('.') if f.endswith('.csv')]
        if not files:
            print("No CSV files found in the current directory.")
            return None

        print("Available CSV files:")
        for idx, file in enumerate(files, 1):
            print(f"{idx}. {file}")

        choice = input("Choose a file by number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(files):
            return files[int(choice) - 1]
        print("Invalid selection.")
        return None

    def _choose_column(self):
        """Prompt user to choose a column for sorting."""
        print("Available columns:")
        for idx, col in enumerate(self.header, 1):
            print(f"{idx}. {col}")

        choice = input("Choose a column by number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.header):
            return self.header[int(choice) - 1]
        print("Invalid selection.")
        return None


if __name__ == '__main__':
    CsvManager().cmdloop()
