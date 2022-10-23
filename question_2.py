class dog:
    def __init__(self , name , age , coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        return f"Name : {self.name} \n Age : {self.age}"

    def get_info(self):
        return f"Coat Color : {self.coat_color}"

class JackRusselTerrier(dog):
    def __init__(self , name , age , coat_color , height , weight):
        super().__init__(name , age , coat_color)
        self.height = height
        self.weight = weight

    def get_jrt_features(self):
        return f"\n \n Name : {self.name} \n Age : {self.age} months \n Coat Color : {self.coat_color} \n Height : {self.height}cm \n Weight : {self.weight}kg"

class bulldog(dog):
    def __init__(self , name , age , coat_color , height , weight):
        super().__init__(name , age , coat_color)
        self.height = height
        self.weight = weight

    def conversion(self):
        self.age /= 12
        self.height /= 100
        self.weight *= 2.205
        return self.age , self.height , self.weight

    def get_bd_features(self):
        return f"\n \n Name : {self.name} \n Age : {self.age} years \n Coat Color : {self.coat_color} \n Height in meters : {self.height}m \n Weight in pounds : {self.weight}lbs"

name = input("Enter your dog's name :")
age = int(input("Enter your dog's age in months :"))
coat_color = input("Enter your dog's coat color :")
height = int(input("Enter your dog's height in cm :"))
weight = float(input("Enter your dogs weight in kg :"))
JackRusselTerrier_obj = JackRusselTerrier(name , age , coat_color , height , weight)
print(JackRusselTerrier_obj.get_jrt_features())
age = int(input("Enter your dog's age in months :"))
height = int(input("Enter your dog's height in cm :"))
weight = float(input("Enter your dogs weight in kg :"))
bulldog_obj = bulldog(name , age , coat_color , height , weight)
bulldog_obj.conversion()
print(bulldog_obj.get_bd_features())