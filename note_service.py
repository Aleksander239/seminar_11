from utils.file_handler import FileHandler
from models.note import Note

class NoteService:
    def __init__(self, file_path='data/notes.json'):
        self.file_path = file_path
        self.notes = self.load_notes()

    def load_notes(self):
        file_handler = FileHandler(self.file_path)
        notes_data = file_handler.read_json_file()
        return [Note(**note_data) for note_data in notes_data]

    def save_notes(self):
        notes_data = [note.to_dict() for note in self.notes]
        file_handler = FileHandler(self.file_path)
        file_handler.write_json_file(notes_data)

    def add_note(self, note):
        self.notes.append(note)
        self.save_notes()

    def get_all_notes(self):
        return self.notes

    def find_note(self, id):
        for i in range(len(self.notes)):
            if id == self.notes[i].to_dict()['id']:
                return self.notes[i].to_dict()

    def update_note(self, id, updated_note):
        for i in range(len(self.notes)):
            if id == self.notes[i].to_dict()['id']:
                self.notes[i] = updated_note
                self.save_notes()

    def delete_note(self, id):
        for i in range(len(self.notes)):
            if id == self.notes[i].to_dict()['id']:
                del self.notes[i]
                self.save_notes()

    def export_to_csv(self):
        notes_data = [note.to_dict() for note in self.notes]
        file_handler = FileHandler('export.csv')
        file_handler.export_to_csv(notes_data, ['id', 'title', 'content', 'timestamp'])

    def import_from_csv(self):
        file_handler = FileHandler('import.csv')
        imported_notes = file_handler.import_from_csv(['id', 'title', 'content', 'timestamp'])
        for note in imported_notes:
            self.add_note(Note(note['id'], note['title'], note['content'], note['timestamp']))
