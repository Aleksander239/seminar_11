from utils.file_handler import FileHandler
from models.contact import Contact

class ContactService:
    def __init__(self, file_path='data/contacts.json'):
        self.file_path = file_path
        self.contacts = self.load_contacts()

    def load_contacts(self):
        file_handler = FileHandler(self.file_path)
        contacts_data = file_handler.read_json_file()
        return [Contact(**contact_data) for contact_data in contacts_data]

    def save_contacts(self):
        contacts_data = [contact.to_dict() for contact in self.contacts]
        file_handler = FileHandler(self.file_path)
        file_handler.write_json_file(contacts_data)

    def find_contact(self, name=None, phone=None):
        if name:
            for i in range(len(self.contacts)):
                if name == self.contacts[i].to_dict()['name']:
                    return self.contacts[i].to_dict()
        elif phone:
            for i in range(len(self.contacts)):
                if phone == self.contacts[i].to_dict()['phone']:
                    return self.contacts[i].to_dict()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def get_all_contacts(self):
        return self.contacts

    def update_contact(self, id, updated_contact):
        for i in range(len(self.contacts)):
            if id == self.contacts[i].to_dict()['id']:
                self.contacts[i] = updated_contact
                self.save_contacts()

    def delete_contact(self, id):
        for i in range(len(self.contacts)):
            if id == self.contacts[i].to_dict()['id']:
                del self.contacts[i]
                self.save_contacts()

    def export_to_csv(self):
        contacts_data = [contact.to_dict() for contact in self.contacts]
        file_handler = FileHandler('export.csv')
        file_handler.export_to_csv(contacts_data, ['id', 'name', 'email', 'phone'])

    def import_from_csv(self):
        file_handler = FileHandler('import.csv')
        imported_contacts = file_handler.import_from_csv(['id', 'name', 'email', 'phone'])
        for contact in imported_contacts:
            self.add_contact(Contact(contact['id'], contact['name'], contact['email'], contact['phone']))
