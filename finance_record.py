class FinanceRecord:
    def __init__(self, id, date, amount, category, description):
        self.id = id
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'amount': self.amount,
            'category': self.category,
            'description': self.description
        }

