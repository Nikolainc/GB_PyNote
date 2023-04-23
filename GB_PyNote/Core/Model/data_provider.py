class data_provider:

    def __init__(self):
        self.path = "note_sheet/note.csv"
        self.data = self.read()

    def read(self):
        with open(self.path, 'r') as file:
            raw_data = file.read().split('\n')
            data = []
            for note in raw_data:
                data.append(note.split(";"))
            return data

    def write(self, data):
        self.data = data
        with open(self.path, 'w') as file:
            for i in range(len(data)):
                if i < len(data) - 1:
                    file.write(f"{str(data[i][0])};{str(data[i][1])};{str(data[i][2])};{str(data[i][3])};{str(data[i][4])}\n")
                else:
                    file.write(f"{str(data[i][0])};{str(data[i][1])};{str(data[i][2])};{str(data[i][3])};{str(data[i][4])}")  

    def get_data(self):
        return self.data