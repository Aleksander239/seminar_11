import json
import csv
from pathlib import Path

class FileHandler:
    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def read_json_file(self):
        if not self.file_path.exists():
            return []
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def write_json_file(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def export_to_csv(self, data, fields):
        with open('export.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

    def import_from_csv(self, fields):
        data = []
        with open('import.csv', 'r', newline='') as f:
            reader = csv.DictReader(f, fieldnames=fields)
            for row in reader:
                data.append(row)
        return data

