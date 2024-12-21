from utils.file_handler import FileHandler
from models.finance_record import FinanceRecord
import datetime

class FinanceService:
    def __init__(self, file_path='data/finance.json'):
        self.file_path = file_path
        self.records = self.load_records()

    def load_records(self):
        file_handler = FileHandler(self.file_path)
        records_data = file_handler.read_json_file()
        return [FinanceRecord(**record_data) for record_data in records_data]

    def save_records(self):
        records_data = [record.to_dict() for record in self.records]
        file_handler = FileHandler(self.file_path)
        file_handler.write_json_file(records_data)

    def add_record(self, record):
        self.records.append(record)
        self.save_records()

    def get_all_records(self, category=None):
        if category:
            return [record.to_dict() for record in self.records if record.to_dict()['category'] == category]
        else:
            return self.records

    def update_record(self, id, updated_record):
        for i in range(len(self.records)):
            if id == self.records[i].to_dict()['id']:
                self.records[i] = updated_record
                self.save_records()

    def delete_record(self, id):
        for i in range(len(self.records)):
            if id == self.records[i].to_dict()['id']:
                del self.records[i]
                self.save_records()

    def generate_report(self, start_date_, end_date_):
        income = 0
        spendings = 0
        start_date = str_to_date(start_date_)
        end_date = str_to_date(end_date_)
        for i in range(len(self.records)):
            date = str_to_date(self.records[i].to_dict()['date'])
            if (start_date <= date) & (date <= end_date):
                amount = self.records[i].to_dict()['amount']
                if amount > 0:
                    income += amount
                else:
                    spendings -= amount
        print(f'Финансовый отчёт за период с {start_date_} по {end_date_}:')
        print(f'- Общий доход: {income}.')
        print(f'- Общие расходы: {spendings}.')
        print(f'- Баланс: {income - spendings}')

    def export_to_csv(self):
        records_data = [record.to_dict() for record in self.records]
        file_handler = FileHandler('export.csv')
        file_handler.export_to_csv(records_data, ['id', 'date', 'amount', 'category', 'description'])

    def import_from_csv(self):
        file_handler = FileHandler('import.csv')
        imported_records = file_handler.import_from_csv(['id', 'date', 'amount', 'category', 'description'])
        for record in imported_records:
            self.add_record(FinanceRecord(record['id'], record['date'], record['amount'], record['category'], record['description']))

def str_to_date(strdate):
    day = strdate[:2]
    month = strdate[3:5]
    year = strdate[6:]
    return datetime.date(year, month, day)