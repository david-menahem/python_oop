class Parts():
    def __init__(self,fabric,screws):
        self.fabric = fabric
        self.screws = screws

    def print_parts(self):
        print(f'Fabric: {self.fabric}, Screws: {self.screws}')