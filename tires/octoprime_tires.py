from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, wornOut):
        self.Totalworn = 0
        for i in wornOut:
                self.Totalworn = self.Totalworn+i

    def needs_service(self):
        return self.Totalworn >=3
