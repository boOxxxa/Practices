class Dog():
    def __init__(self, name,age):
        self.name=name
        self.age=age
    def Sit(self):
        print("Собака - ",self.name, "Села")
    def Roll_over(self):
        print("Собака - ", self.name, "Перекатилась")
my_dog=Dog("Bebra", 6)
my_dog.Sit()
my_dog.Roll_over()
my_dog=Dog("lucy",3)
my_dog.Sit()
my_dog.Roll_over()
