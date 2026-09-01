class details:
    def __init__(self,name,age,field):
        self.name= name
        self.age= age
        self.field= field
    def show_name(self):
        print(self.name)
    def show_age(self):
        print(self.age)
    def show_field(self):
        print(self.field)
Details= details("Rohit",23,"Data analyst")
Details.show_name()
Details.show_age()
Details.show_field()