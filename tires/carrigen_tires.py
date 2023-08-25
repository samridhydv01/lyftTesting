from tires.tires import Tires

class CarrigenTires(Tires):
    def __init__(self, wornOut):
        self.worn = False
        for i in wornOut:
            if i >= 0.9:
                self.worn = True

    def needs_service(self):
        return self.worn
