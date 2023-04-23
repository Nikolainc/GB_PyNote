from ..Core.Model.presenter import presenter

class app_01:

    def start_app():
        Pres = presenter()
        print("START")
        Pres.print_note()
        Pres.create_note()