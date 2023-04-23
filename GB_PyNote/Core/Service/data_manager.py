from ..Model.Data import data
from datetime import datetime
import uuid
from ..Model.data_provider import data_provider

class data_manager:

    def __init__(self):
        self.UID = uuid
        self.datetime = datetime
        self.provider = data_provider()
        self.notes = self.read_notes()

    def read_notes(self):
        raw_data = self.provider.get_data()
        read_data = []
        try:
            for i in range(len(raw_data)):
                read_data.append(data(raw_data[i][0], raw_data[i][1], raw_data[i][2], raw_data[i][3], raw_data[i][4]))
            return read_data
        except :
            print("ERROR READ DATA MANAGER")
            return read_data


    def write_notes(self):
        raw_data = []
        for note in self.notes:
            raw_data.append(note.raw_note())
        self.provider.write(raw_data)

    def create_note(self, header, body):
        note = data(str(self.UID.uuid4().int)[0:5], header, body, self.datetime.now().strftime("%d.%m.%y %H:%M:%S"), self.datetime.now().strftime("%d.%m.%y %H:%M:%S"))
        self.notes.append(note)
        self.write_notes()
        return note

    def chage_note(self, data_changing, text, type_change):

        if isinstance(data_changing, data):

            data_changing.chage_note(type_change, text, self.datetime.now().strftime("%d.%m.%y %H:%M:%S"))
            self.write_notes()

        else:
            print("ERROR CHANGE NOTE")
    
    def del_note(self, data_delete):

        new_data = []

        if isinstance(data_delete, data):

            for note in self.notes:

                if data_delete == note:
                    continue

                new_data.append(note)

            self.notes = new_data
            self.write_notes()

        else:

            print("ERROR DELETE NOTE")
