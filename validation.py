import re

def validate_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.fullmatch(pattern, email))

def validate_date(date):
    pattern = r'\d{2}-\d{2}-\d{4}'
    return bool(re.fullmatch(pattern, date))

def validate_phone_number(phone_number):
    pattern = r'^\+\d{11}$'
    return bool(re.fullmatch(pattern, phone_number))
