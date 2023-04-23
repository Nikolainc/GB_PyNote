class data:
    
    def __init__(self, ID, header, body, created_data, last_change):

        self.ID = ID
        self.header = header
        self.body = body
        self.created_data = created_data
        self.last_change = last_change

    def chage_note(self, type_change, text, datetime):

        if type_change == 1:
            self.body = text
            self.last_change = datetime
            return self

        elif type_change == 0:
            self.header = text
            self.last_change = datetime
            return self

        else:
            print("ERROR DATA CHANGE")
            return self

    def raw_note(self):
        return [self.ID, self.header, self.body, self.created_data, self.last_change]

    def __str__(self):
     return f"Заметка N{self.ID}\n{self.header} от {self.created_data}\n{self.body} \x1B[3mпоследнее изменение {self.last_change}\x1B[0m\n"
    
    def __eq__(self, other):
        if isinstance(other, data):
            return self.ID == other.ID
        return False